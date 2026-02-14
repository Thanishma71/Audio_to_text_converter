from flask import Flask, request, render_template
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa
import os

app = Flask(__name__)

# ✅ Load smaller model (faster & safer)
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return "No file uploaded"

    file = request.files["audio"]

    # Save uploaded file
    filepath = "temp.wav"
    file.save(filepath)

    # Load audio using librosa
    speech, sr = librosa.load(filepath, sr=16000)

    # Process input
    input_features = processor(
        speech,
        sampling_rate=16000,
        return_tensors="pt"
    ).input_features

    # Generate transcription
    with torch.no_grad():
        predicted_ids = model.generate(input_features)

    transcription = processor.batch_decode(
        predicted_ids,
        skip_special_tokens=True
    )[0]

    # Optional: delete temp file
    os.remove(filepath)

    return render_template("index.html", transcription=transcription)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
   