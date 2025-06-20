from flask import Flask, render_template, request, redirect, url_for, send_file
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from werkzeug.utils import secure_filename
import os
import PyPDF2
import gradio as gr
from PIL import Image
import requests
import time

app = Flask(__name__)

def download_from_github_release():
    """Download from GitHub releases with error handling"""
    base_url = "https://github.com/raniadridi/matchmeai/releases/download/v1.0"
    files = ['job_data.csv', 'job_embeddings.npy', 'resume_embeddings.npy', 
             'resume_texts.npy', 'resume_files.npy']
    
    os.makedirs('data', exist_ok=True)
    
    for filename in files:
        filepath = f'data/{filename}'
        if not os.path.exists(filepath):
            print(f"Downloading {filename}...")
            url = f"{base_url}/{filename}"
            
            try:
                response = requests.get(url, timeout=300)  # 5 minute timeout
                response.raise_for_status()  # Raise error for bad status codes
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                print(f"Successfully downloaded {filename} ({len(response.content)} bytes)")
                time.sleep(1)  # Small delay between downloads
                
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
                return False
        else:
            print(f"{filename} already exists")
    
    return True

# Download files before loading them
print("Starting data download...")
if not download_from_github_release():
    print("Failed to download data files!")
    exit(1)

print("Data download completed. Loading files...")

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load precomputed embeddings and data
try:
    resume_embeddings = np.load('data/resume_embeddings.npy')
    resume_texts = np.load('data/resume_texts.npy', allow_pickle=True)
    resume_files = np.load('data/resume_files.npy', allow_pickle=True)
    job_embeddings = np.load('data/job_embeddings.npy')
    job_data = pd.read_csv('data/job_data.csv')
    print("All data files loaded successfully!")
except Exception as e:
    print(f"Error loading data files: {e}")
    exit(1)

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    user_type = request.form['user_type']
    top_k = int(request.form['top_k'])
    uploaded_file = request.files.get('resume_file')
    query = None

    if user_type == 'job_seeker' and uploaded_file:
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        query = extract_text_from_pdf(file_path)
    else:
        query = request.form['query']

    query_embedding = model.encode([query])

    if user_type == 'job_seeker':
        distances = cosine_similarity(query_embedding, job_embeddings)[0]
        top_indices = distances.argsort()[-top_k:][::-1]

        results = [
            {
                "Title": job_data.iloc[idx]['title'],
                "Company": job_data.iloc[idx]['company_name'],
                "Description": job_data.iloc[idx]['description'][:300],
                "Score": distances[idx]
            }
            for idx in top_indices
        ]
    else:
        distances = cosine_similarity(query_embedding, resume_embeddings)[0]
        top_indices = distances.argsort()[-top_k:][::-1]

        results = [
            {
                "File": resume_files[idx],
                "Text Preview": resume_texts[idx][:300],
                "Score": distances[idx]
            }
            for idx in top_indices
        ]

    return render_template('results.html', results=results)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
