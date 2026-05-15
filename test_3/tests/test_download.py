from pages.download_page import DownloadPage


def test_download_third_file(page):
    download_page = DownloadPage(page)

    download_page.open()

    assert download_page.get_files_count() >= 3

    expected_file_name = download_page.get_file_name_by_index(
        DownloadPage.THIRD_FILE_INDEX,
    )

    actual_file_name = download_page.download_file_by_index(
        DownloadPage.THIRD_FILE_INDEX,
    )

    assert actual_file_name == expected_file_name