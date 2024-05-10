from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_locators import LoginLocators
from src.user_data import UserData


class BasePage:
    timeout = 10
    login_locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def login(self):
        self.element_is_visible(self.login_locators.USER_NAME).send_keys(self.user.standard_user)
        self.element_is_visible(self.login_locators.PASSWORD).send_keys(self.user.password)
        self.element_is_clickable(self.login_locators.LOGIN_BUTTON).click()

    def get_text(self, locator):
        return self.element_is_visible(locator).text

    def get_length(self, locator):
        return len(self.elements_are_visible(locator))

    def click_to_element(self, locator):
        self.element_is_clickable(locator).click()

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
