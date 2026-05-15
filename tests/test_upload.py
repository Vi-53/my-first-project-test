from pages.upload_page import UploadPage
from config.settings import TEST_IMAGE_PATH


def test_upload_page(page):
    upload_page = UploadPage(page)

    upload_page.open()

    upload_page.upload_file(TEST_IMAGE_PATH)

    assert upload_page.get_success_text() == UploadPage.SUCCESS_TEXT
    assert upload_page.get_uploaded_file_name() == TEST_IMAGE_PATH.name

