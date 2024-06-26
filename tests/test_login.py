from locators.main_locators import MainLocators
from pages.login_page import LoginPage
from src.urls import Urls


class TestLogin:
    main_locators = MainLocators()
    url = Urls()

    def test_login(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open_with_login()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        expected_text = "Products"
        assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"

    def test_login1(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open_with_login()
        page.login()
        expected_len = 6
        cards = page.get_length(self.main_locators.CARDS)
        assert cards == expected_len, f"Expected result: {expected_len}, Actual result: {cards}"
