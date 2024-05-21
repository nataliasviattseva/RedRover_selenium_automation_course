import pytest

from functions.functions import sort_list_price, sort_list_alphabetical
from pages.main_page import MainPage
from src.main_data import MainData
from src.urls import Urls


class TestMainPage:
    url = Urls()
    main_data = MainData()

    def test_logout(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open_with_login()
        page.login()
        page.logout()
        assert driver.current_url == self.url.base_url and page.check_element_is_displayed() is True, \
            "Login form is not displayed"

    @pytest.mark.parametrize("value", main_data.sorting_data_price)
    def test_filtering_by_price(self, driver, value):
        page = MainPage(driver, self.url.base_url)
        page.open_with_login()
        lst = page.check_filter_by_price(value[0])
        assert lst == sort_list_price(lst, value[1]), value[2]

    @pytest.mark.parametrize("value", main_data.sorting_data_name)
    def test_filtering_by_name(self, driver, value):
        page = MainPage(driver, self.url.base_url)
        page.open_with_login()
        lst = page.check_filter_by_name(value[0])
        assert lst == sort_list_alphabetical(lst, value[1]), value[2]

    def test_add_item_to_cart(self, driver):
        expected_value = "1"
        page = MainPage(driver, self.url.base_url)
        page.open_with_login()
        assert page.add_to_cart().text == expected_value, f"Count of added items in not equal to {expected_value} "

    def test_remove_item_from_cart(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open_with_login()
        page.add_to_cart()
        page.remove_from_cart()
        assert page.check_badge_element_is_not_present() is True, "There are items in the cart"
