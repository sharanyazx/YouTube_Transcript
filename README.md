
# 🎬 YouTube Transcript to Notes Converter

This Streamlit web app takes a YouTube video URL, extracts the transcript using `youtube-transcript-api`, and generates a detailed summary using Google's `gemini-pro` model via the Generative AI API.

---

## 🚀 Features

- ✅ Extracts transcript from any YouTube video with captions
- ✅ Summarizes content using Gemini-Pro LLM
- ✅ Displays video thumbnail automatically
- ✅ Clean and simple UI with Streamlit
- ✅ `.env` support for secure API key management


---

## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [Google Generative AI (gemini-pro)](https://ai.google.dev/) – LLM summarization
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) – Transcript extractor
- [dotenv](https://pypi.org/project/python-dotenv/) – Environment variable support

---

## 📂 Folder Structure

```

YouTube_Transcript/
│
├── app.py                 # Main Streamlit app
├── .gitignore             # Ignored files (e.g., .env, .venv/)
├── .env                   # API key (not tracked by Git)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

````

---

## 🧪 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sharanyazx/YouTube_Transcript.git
cd YouTube_Transcript
````

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file and add your Gemini API key

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

> Get your key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

Make sure the video has **English subtitles/captions** enabled.


## ❗ .gitignore Best Practice

Ensure `.env`, `.venv/`, and other sensitive/system files are not tracked:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```


## 🙋‍♀️ Author

Made with ❤️ by [Sharanya T](https://github.com/sharanyazx)

````

