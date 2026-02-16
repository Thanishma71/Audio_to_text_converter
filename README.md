#  AI Audio to Text Converter

An AI-powered speech recognition web application that converts uploaded audio files into text using OpenAI Whisper.

##  Live Demo
🔗 https://huggingface.co/spaces/Thanishma/audio-to-text-whisper

##  Features
- Upload audio files (.wav format)
- Automatic speech-to-text conversion
- Fast processing using Whisper Tiny model
- Clean and simple web interface

##  Tech Stack
- Python
- Flask
- Hugging Face Transformers
- OpenAI Whisper (whisper-tiny)
- PyTorch
- Librosa
- Hugging Face Spaces (Deployment)

##  Project Structure
```
AUDIO_TO_TEXT/
│── static/
│── templates/
│── app.py
│── requirements.txt
│── README.md
```

##  How It Works
1. User uploads an audio file.
2. Audio is processed using Librosa.
3. Whisper model generates transcription.
4. Transcribed text is displayed on the webpage.

## 📦 Installation (Run Locally)

```bash
pip install -r requirements.txt
python app.py
```

Then open:
http://127.0.0.1:5000

## 👨‍💻 Author
Thanishma Bezawada
