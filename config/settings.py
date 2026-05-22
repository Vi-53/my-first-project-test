from pathlib import Path

UPLOADS_DIR = Path("resources/uploads")
DOWNLOADS_DIR = Path("resources/downloads")

TEST_IMAGE_PATH = UPLOADS_DIR / "test_image.png"

VIEWPORT = {
    "width": 1440,
    "height": 900,
}

IGNORE_HTTPS_ERRORS = True
ACCEPT_DOWNLOADS = True

DEFAULT_TIMEOUT_MS = 10_000
DEFAULT_NAVIGATION_TIMEOUT_MS = 15_000