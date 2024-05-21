import pytest

from pages.order_page import OrderPage
from src.order_data import OrderData
from src.urls import Urls


class TestOrder:
    url = Urls()
    data = OrderData()

    def test_order_with_valid_credentials(self, driver):
        page = OrderPage(driver, self.url.base_url)
        page.open_with_login()
        page.login()
        expected_text = self.data.successful_message
        actual_text = page.order_with_valid_credentials(self.data.user_data_with_valid_credentials)

        assert expected_text == actual_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"

    @pytest.mark.parametrize("lst_data", data.user_data_with_invalid_credentials)
    def test_order_with_wrong_credentials(self, driver, lst_data):
        page = OrderPage(driver, self.url.base_url)
        page.open_with_login()
        page.login()
        expected_text = lst_data[3]
        actual_text = page.order_with_wrong_credentials(lst_data)
        assert expected_text == actual_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
