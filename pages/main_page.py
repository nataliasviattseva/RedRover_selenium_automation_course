from selenium.webdriver.support.select import Select

from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginLocators()

    def logout(self):
        self.click_to_element(self.main_locators.BURGER_MENU)
        self.click_to_element(self.main_locators.LOGOUT_BTN)

    def check_element_is_displayed(self):
        login_form = self.element_is_visible(self.login_locators.LOGIN_FORM)
        return self.element_is_displayed(login_form)

    def select(self, value):
        locator = self.main_locators.SELECT
        self.select_by_value(locator=locator, value=value)

    def get_price(self):
        return [i.text for i in self.elements_are_visible(self.main_locators.PRICE_VALUE)]

    def get_name(self):
        return [i.text for i in self.elements_are_visible(self.main_locators.NAME_VALUE)]

    def check_filter_by_price(self, value):
        self.select(value)
        return self.get_price()

    def check_filter_by_name(self, value):
        self.select(value)
        return self.get_name()

    def add_to_cart(self):
        self.click_to_element(self.main_locators.ADD_SAUCE_LABS_BACKPACK)
        return self.element_is_visible(self.main_locators.COUNT_ITEMS)

    def remove_from_cart(self):
        self.click_to_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    def check_badge_element_is_not_present(self):
        return self.element_is_not_present(self.main_locators.COUNT_ITEMS)
