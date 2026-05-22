from pages.upload_page import UploadPage
from config.settings import TEST_IMAGE_PATH
from config.routes import UPLOAD_URL


def test_upload_page(page, actions):
    assert TEST_IMAGE_PATH.exists(), f"File does not exist: {TEST_IMAGE_PATH.resolve()}"

    actions.goto(UPLOAD_URL)

    upload_page = UploadPage(page)

    upload_page.upload_file(TEST_IMAGE_PATH)

    assert upload_page.get_success_text() == "File Uploaded!"
    assert upload_page.get_uploaded_file_name() == TEST_IMAGE_PATH.name
