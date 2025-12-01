import whisper
import subprocess
from pathlib import Path

_model = None

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("small")  # small model for fast testing
    return _model

def convert_to_wav(in_path):
    out = str(Path(in_path).with_suffix(".wav"))
    cmd = f'ffmpeg -y -i "{in_path}" -ar 16000 -ac 1 "{out}"'
    subprocess.run(cmd, shell=True, check=True)
    return out

def transcribe_file(path):
    ext = Path(path).suffix.lower()
    wav = path
    if ext in [".webm", ".mp4", ".mkv", ".mov"]:
        wav = convert_to_wav(path)

    model = get_model()
    return model.transcribe(wav)
