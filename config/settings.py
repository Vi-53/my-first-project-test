from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

BASE_URL = "https://the-internet.herokuapp.com"

UPLOADS_DIR = PROJECT_ROOT / "resources" / "uploads"
DOWNLOADS_DIR = PROJECT_ROOT / "resources" / "downloads"

TEST_IMAGE_PATH = UPLOADS_DIR / "test_image.png"