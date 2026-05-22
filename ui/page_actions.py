import logging
from collections.abc import Callable

from playwright.sync_api import Dialog, Page, Download
from typing import Literal

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class PageActions:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url:str) -> None:
        """открывает юрл в браузере"""
        logger.info(f"PageActions: goto '{url}'")
        self.page.goto(url)

    def wait_for_load_state(self, state: str | None = None) -> None:
        """ждет пока стр загрузится"""
        logger.info(f"PageActions: wait for load state '{state}'")
        self.page.wait_for_load_state(state)

    def expect_new_page(self):
        """нужен, чтобы после клика открывать новую вкладку"""
        logger.info(f"PageActions: expect new page")
        return self.page.context.expect_page()

    def close_page(self) -> None:
        """закрывает текущую вкладку"""
        logger.info(f"PageActions: close page")
        self.page.close()

    def bring_to_front(self) -> None:
        """делает нужную страницу активной"""
        logger.info(f"PageActions: bring page to front")
        self.page.bring_to_front()

    def run_and_accept_alert(self, action: Callable[[], None]) -> str:
        """выполняет действие, ждет alert/confirm и нажимает ок"""
        logger.info(f"PageActions: accept dialog")
        return self._handle_dialog(action=action, mode="accept")

    def run_and_dismiss_alert(self, action: Callable[[], None]) -> str:
        """выполняет действие, ждёт alert/confirm и нажимает Cancel"""
        logger.info(f"PageActions: dismiss dialog")
        return self._handle_dialog(action=action, mode="dismiss")

    def run_and_accept_prompt(
            self,
            action: Callable[[], None],
            prompt_text: str,
    ) -> str:
        """нужен для prompt — окна, где вводим текст"""
        logger.info(f'PageActions: accept prompt')

        return self._handle_dialog(
            action=action,
            mode="accept",
            prompt_text=prompt_text,
        )

    def _handle_dialog(
            self,
            action: Callable[[], None],
            mode: Literal["accept", "dismiss"],
            prompt_text: str | None = None,
    ) -> str:
        """Чтобы не дублировать один и тот же код три раза"""
        logger.info(f"PageActions: expect dialog")
        message = ""
        dialog_was_shown = False

        def handle_dialog(dialog: Dialog) -> None:
            nonlocal message, dialog_was_shown

            dialog_was_shown = True
            message = dialog.message

            logger.info(f"PageActions: dialog '{dialog.type}' with message '{message}'")

            if mode =="dismiss":
                dialog.dismiss()
                return

            if prompt_text is None:
                dialog.accept()
                return

            dialog.accept(prompt_text)

        self.page.once("dialog", handle_dialog)

        action()

        if not dialog_was_shown:
            raise RuntimeError("Expected dialog was not shown")

        return message

    def run_and_expect_download(self, action: Callable[[], None]) -> Download:
        logger.info(f"PageActions: expect download")

        with self.page.expect_download() as download_info:
            action()

        download = download_info.value

        logger.info(
            f"PageActions: downloaded file '{download.suggested_filename}'"
        )

        return download
