🎯 MatchMe AI - Intelligent Job & Resume Matching Platform

A powerful Flask web application that uses AI-powered semantic similarity to match job seekers with relevant job opportunities and help employers find the perfect candidates using advanced NLP models.

## 🌟 Live Demo

**🚀 [Try MatchMe AI Live](https://matchmeai.onrender.com)**

## 📊 Features

- **🤖 AI-Powered Matching**: Uses SentenceTransformers for semantic similarity matching
- **📄 PDF Resume Processing**: Extract and analyze text from PDF resumes automatically
- **💼 Dual User Experience**: Separate interfaces for job seekers and employers
- **🎯 Smart Recommendations**: Get top-K relevant matches based on semantic similarity
- **📈 Cosine Similarity Scoring**: Advanced similarity scoring for accurate matching
- **💻 Modern UI**: Responsive design with elegant styling and animations
- **⚡ Fast Processing**: Pre-computed embeddings for lightning-fast results
- **🔒 Secure File Handling**: Safe PDF upload and processing
- **📱 Mobile Friendly**: Fully responsive design for all devices

## 🏗️ Project Structure

```
matchme-ai/
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
├── resumes-embeddings-preparation.ipynb
├── job-postings-embeddings-preparation.ipynb
├── data/
│   ├── job_data.csv
│   ├── job_embeddings.npy
│   ├── resume_embeddings.npy
│   ├── resume_texts.npy
│   └── resume_files.npy
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   └── bf.jpg
└── uploads
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/matchme-ai.git
   cd matchme-ai
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create necessary directories**
   ```bash
   mkdir -p uploads
   mkdir -p data
   mkdir -p static
   mkdir -p templates
   ```

5. **Data files will be downloaded automatically**
   - The app will automatically download data files from GitHub releases on first run
   - Alternatively, run the notebooks to generate your own data:
     - Run `resumes-embeddings-preparation.ipynb` to process resume data
     - Run `job-postings-embeddings-preparation.ipynb` to process job data
   - Add background image `bf.jpg` to `static/` folder

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   ```
   http://localhost:5000
   ```

## 🔬 Usage

### For Job Seekers

- Select "Job Seeker" from the dropdown
- Upload your resume (PDF format)
- Choose number of job recommendations
- Get AI-matched job opportunities with similarity scores

### For Employers

- Select "Employer" from the dropdown
- Enter detailed job description
- Specify number of candidate results
- Receive best-matched resumes with relevance scores

### API Endpoints

- `GET /` - Main application interface
- `POST /results` - Process matching requests and return results

## 📈 How It Works

### AI Matching Algorithm

1. **🧠 Text Embedding**: Uses SentenceTransformers 'all-MiniLM-L6-v2' model
2. **📊 Similarity Calculation**: Computes cosine similarity between embeddings
3. **🎯 Ranking System**: Ranks matches by similarity scores
4. **⚡ Fast Retrieval**: Pre-computed embeddings for instant results

### Data Processing Pipeline

- **📄 PDF Text Extraction**: PyPDF2 for resume text extraction
- **🔍 Semantic Analysis**: Advanced NLP for understanding context
- **📈 Embedding Generation**: Vector representations of text content
- **🎯 Similarity Matching**: Mathematical similarity scoring

## 📚 Technology Stack

- **Backend**: Flask (Python)
- **ML/AI**: SentenceTransformers, scikit-learn, NumPy
- **Data Processing**: Pandas, PyPDF2
- **Frontend**: HTML5, CSS3, JavaScript
- **File Handling**: Werkzeug, Pillow
- **Deployment**: Render, Gunicorn
- **Version Control**: Git, GitHub

## 🛠️ Data Requirements

### Job Data CSV Format
Your `job_data.csv` should contain:
- `title`: Job title
- `company_name`: Company name
- `description`: Job description

### Pre-computed Files
- **job_embeddings.npy**: Embeddings for job descriptions
- **resume_embeddings.npy**: Embeddings for resume texts
- **resume_texts.npy**: Processed resume text content
- **resume_files.npy**: Resume file names/identifiers

## 📓 Data Preparation

**📁 Data files are automatically downloaded from GitHub releases when you run the app.**

### Manual Data Generation (Optional)

### Resume Processing
**`resumes-embeddings-preparation.ipynb`** - Processes PDF resumes and generates embeddings for the matching system.

### Job Data Processing  
**`job-postings-embeddings-preparation.ipynb`** - Processes job postings data and creates embeddings for job descriptions.

## 📊 Performance Optimization

- **🚀 Pre-computed Embeddings**: Eliminates real-time embedding generation
- **📈 Efficient Similarity Search**: Optimized cosine similarity calculations
- **💾 Memory Management**: Efficient NumPy array handling
- **⚡ Fast File Processing**: Streamlined PDF text extraction

## 🛡️ Security Features

- **🔒 Secure File Upload**: Werkzeug secure filename handling
- **📄 PDF-Only Uploads**: Restricted file type validation
- **🗂️ Temporary Storage**: Automatic cleanup of uploaded files
- **🛡️ Input Validation**: Form data sanitization

## 📚 Tips for Better Matching

### For Job Seekers
- **📄 Clear Resume Format**: Use standard PDF format with readable text
- **🎯 Relevant Keywords**: Include industry-specific terms
- **📊 Complete Information**: Provide comprehensive skill descriptions

### For Employers
- **📝 Detailed Descriptions**: Write comprehensive job descriptions
- **🔍 Specific Requirements**: Include technical skills and qualifications
- **🎯 Clear Expectations**: Define role responsibilities clearly

## 📞 Dependencies

- **Flask**: Web framework
- **sentence-transformers**: AI embedding models
- **scikit-learn**: Machine learning utilities  
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **PyPDF2**: PDF text extraction
- **werkzeug**: WSGI utilities
- **Pillow**: Image processing

## 📞 Contact

- **👨‍💻 Developer**: Rania Dridi
- **📧 Email**: raniadridi42@gmail.com
- **🔗 LinkedIn**: [Rania Dridi](https://linkedin.com/in/raniadridii)
- **🐙 GitHub**: [Rania Dridi](https://github.com/raniadridi)

---

**⭐ Star this repository if you found it helpful!**

Made with ❤️ for connecting talent with opportunities