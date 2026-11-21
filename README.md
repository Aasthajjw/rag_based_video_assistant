# AI Video Assistant

Website - https://ragbasedvideoassistant-6bhcsmagyiyqyhwfhwc83m.streamlit.app/

An AI-powered application that converts YouTube videos and audio into meaningful, structured information. It helps users understand lengthy videos and meetings through automatic transcription, summarization, key-point extraction, and an interactive question-answering system.

The application combines speech recognition, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG) to make video content easier to understand and explore.

## Features

- **YouTube Audio Extraction:** Extracts audio from YouTube videos for further processing.
- **Automatic Transcription:** Converts audio into text using Whisper and Sarvam AI.
- **Multilingual Transcription:** Supports Hinglish transcription through Sarvam AI.
- **AI-Powered Summarization:** Generates concise and structured summaries of lengthy transcripts.
- **Meeting Title Generation:** Automatically creates short, professional titles.
- **Information Extraction:** Supports extracting useful meeting information such as action items and decisions.
- **Interactive Q&A:** Allows users to ask questions about video content using a RAG-based question-answering system.
- **Semantic Search:** Uses vector embeddings to retrieve relevant sections of the transcript.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Programming Language | Python |
| Speech Recognition | OpenAI Whisper |
| Hinglish Transcription | Sarvam AI |
| LLM Integration | XKIRO API |
| Language Model | Mistral Large |
| Embeddings | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| Text Processing | LangChain |
| Audio Extraction | yt-dlp, FFmpeg |
| Audio Processing | Pydub |

## Project Workflow

1. **Input:** User provides a YouTube video URL or supported audio input.
2. **Audio Extraction:** Audio is extracted using yt-dlp and processed into manageable chunks.
3. **Transcription:** Audio chunks are converted into text using Whisper or Sarvam AI.
4. **Text Processing:** The transcript is split into smaller chunks for efficient processing.
5. **Summarization:** XKIRO-powered Mistral Large generates a structured summary.
6. **Vectorization:** Sentence Transformers converts transcript chunks into numerical embeddings.
7. **Storage:** Embeddings are stored in ChromaDB.
8. **Question Answering:** Relevant transcript sections are retrieved and passed to the language model to generate context-based answers.

## Project Structure

```text
AI-Video-Assistant/
│
├── app.py                  # Streamlit application
├── main.py                 # Main processing entry point
├── test.py                 # Testing utilities
├── requirements.txt        # Python dependencies
├── packages.txt            # System dependencies for deployment
├── .gitignore              # Files excluded from Git
├── .env                    # Environment variables (not uploaded)
│
├── core/
│   ├── llm_client.py       # XKIRO LLM configuration
│   ├── transcriber.py      # Audio transcription
│   ├── summarizer.py       # Transcript summarization
│   ├── extractor.py        # Information extraction
│   ├── rag_engine.py       # Retrieval-Augmented Generation
│   └── vector_store.py     # Embeddings and vector storage
│
└── utils/                  # Supporting utility functions
```

*Note: The structure above describes the main project components. Your local repository may contain additional files.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aasthajjw/rag_based_video_assistant.git
cd AI-Video-Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg and FFprobe are required for audio processing.

Download FFmpeg from:

https://ffmpeg.org/download.html

Make sure the FFmpeg `bin` directory is added to your system PATH.

### 5. Configure API Keys

Create a `.env` file in the root directory:

```env
XKIRO_API_KEY=your_xkiro_api_key
SARVAM_API_KEY=your_sarvam_api_key

WHISPER_MODEL=small
SARVAM_STT_MODEL=saaras:v2.5
```

Replace the placeholder values with your actual API keys.

**Important:** Never upload your `.env` file or expose your API keys publicly.

### 6. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## Deployment on Streamlit Community Cloud

1. Push the project to a GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Select **Create App**.
4. Connect your GitHub repository.
5. Choose the deployment branch, usually `main`.
6. Set the main file path to `app.py`.
7. Add your API keys and configuration variables under **App Settings → Secrets**.

Use the following secrets configuration:

```toml
XKIRO_API_KEY = "your_xkiro_api_key"
SARVAM_API_KEY = "your_sarvam_api_key"
WHISPER_MODEL = "small"
SARVAM_STT_MODEL = "saaras:v2.5"
```

Ensure that `requirements.txt` and `packages.txt` are present in the repository root. The `packages.txt` file should contain:

```text
ffmpeg
```

## Environment Variables

| Variable | Description |
|---|---|
| `XKIRO_API_KEY` | API key for LLM-based processing |
| `SARVAM_API_KEY` | API key for Sarvam transcription |
| `WHISPER_MODEL` | Whisper model selection |
| `SARVAM_STT_MODEL` | Sarvam speech-to-text model |

## Future Improvements

- Support for additional video platforms.
- More multilingual transcription options.
- Improved transcript search and retrieval.
- Export summaries and extracted information into PDF and DOCX formats.
- Support for longer recordings and improved processing efficiency.
- Enhanced user interface and processing status indicators.
.

