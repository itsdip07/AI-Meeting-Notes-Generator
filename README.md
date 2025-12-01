<h1 align="center">🎙️ AI Meeting Notes Generator</h1>
<p align="center">
  <strong>Record → Transcribe → Understand → Summarize</strong><br>
  End-to-end intelligent meeting assistant powered by Whisper, FastAPI, Streamlit, and a custom Chrome extension.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Chrome-Extension-4285F4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenAI-Whisper-black?style=for-the-badge" />
</p>

---

# 📌 Overview  
AI Meeting Notes Generator is an end-to-end system that:

- Records **Google Meet audio** via a Chrome extension  
- Uploads the recording to a **FastAPI backend**  
- Transcribes speech using **OpenAI Whisper**  
- Detects topics using **AI clustering**  
- Generates **AI summaries and action items**  
- Displays results beautifully in a **Streamlit UI**

---

#  System Workflow

┌──────────────────┐ ┌─────────────────┐ ┌────────────────────────┐
│ Chrome Extension │────▶│ FastAPI Backend │────▶│ Whisper Transcription │
└──────────────────┘ └─────────────────┘ └────────────────────────┘
│
▼
┌──────────────────────────┐
│ Topic Clustering (UMAP) │
└──────────────────────────┘
│
▼
┌──────────────────────────┐
│ AI Summary + Action Items │
└──────────────────────────┘
│
▼
┌─────────────────┐
│ Streamlit UI │
└─────────────────┘

markdown
Copy code

---

# 🛠️ Tech Stack

### **Frontend**
- Streamlit  
- HTML/CSS (Extension UI)

### **Backend**
- FastAPI  
- Whisper (ASR)  
- Python 3.9  
- FFmpeg  
- UMAP + HDBSCAN (Topic Clustering)  

### **Chrome Extension**
- Manifest V3  
- MediaRecorder  
- getDisplayMedia API  

---

#  Features

### 🎧 Chrome Extension
- Start/Stop recording  
- Captures Google Meet audio  
- Uploads directly to backend API  

###  AI Backend
- Whisper transcription  
- Auto language detection  
- Audio conversion `.webm → .wav`  
- Timestamped segments  

###  Topic Clustering
- SBERT embeddings  
- UMAP reduction  
- HDBSCAN clustering  
- Keyword-based topic names  

###  Meeting Notes Generation
- Executive summary  
- Bullet points  
- Action items  
- Topic-wise segmentation  

###  UI (Streamlit)
- Upload audio  
- View transcript  
- View topic clusters  
- Download notes  

---

# 📂 Project Structure

AI-Meeting-Notes-Generator/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── asr.py
│ │ ├── clustering.py
│ │ └── init.py
│ └── requirements.txt
│
├── frontend/
│ ├── streamlit_app.py
│ └── requirements.txt
│
├── extension/
│ ├── manifest.json
│ ├── popup.html
│ ├── popup.js
│ └── content_inject.js
│
├── data/
├── docs/
├── .gitignore
└── README.md

yaml
Copy code

---

# ⚙️ Setup Instructions

#  Backend Setup (FastAPI)

### 1. Create virtual environment
```bash
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run backend
bash
Copy code
uvicorn app.main:app --reload --port 8000
API documentation:

 http://localhost:8000/docs

 Frontend Setup (Streamlit)
1. Create virtual environment
bash
Copy code
cd frontend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run Streamlit UI
bash
Copy code
streamlit run streamlit_app.py
UI opens at:

 http://localhost:8501

 Chrome Extension Setup
1️. Open chrome://extensions
2️. Enable Developer Mode
3️. Click Load Unpacked
4️. Select the extension/ folder
5️. Extension icon appears in toolbar

Start a Google Meet → click extension → Record.

📡 API Endpoints
POST /upload
Upload meeting audio:

bash
Copy code
curl -X POST "http://localhost:8000/upload" -F "file=@meeting.webm"
Response:

json
Copy code
{
  "status": "ok",
  "transcript": {
    "text": ".....",
    "segments": [...]
  }
}
🛣️ Roadmap
Speaker diarization (WhisperX)

Real-time transcription

Multilingual support

PDF export

Cloud deployment

Authentication & user dashboard

🤝 Contributing
Contributions are welcome!

Steps:

Fork repo

Create feature branch

Commit changes

Open pull request

📜 License
MIT License © 2025
Created by @itsdip07

