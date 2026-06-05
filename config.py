from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)