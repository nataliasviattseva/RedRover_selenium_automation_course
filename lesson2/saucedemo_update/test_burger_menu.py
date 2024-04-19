from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from data import LOGIN, PASSWORD, MAIN_PAGE
from selenium.common import exceptions


browser = webdriver.Chrome()


def setup_function():
    browser.get(MAIN_PAGE)
    browser.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    browser.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    browser.find_element(By.XPATH, LOGIN_BUTTON).click()


# 1. Выход из системы
def test_burger_menu_logout():
    browser.get(f'{MAIN_PAGE}inventory.html')
    browser.find_element(By.ID, BURGER_MENU).click()
    browser.find_element(By.ID, BURGER_MENU_ITEMS[2]).click()
    assert browser.find_element(By.XPATH, LOGIN_BUTTON).is_displayed() is True


# 2. Проверка работоспособности кнопки "About" в меню
def test_burger_menu_about():
    browser.get(f'{MAIN_PAGE}inventory.html')
    browser.find_element(By.ID, BURGER_MENU).click()
    browser.find_element(By.ID, BURGER_MENU_ITEMS[1]).click()
    assert browser.current_url == 'https://saucelabs.com/'


# 3. Проверка работоспособности кнопки "Reset App State"

def is_displayed(elem):
    try:
        elem.is_displayed()
    except exceptions.StaleElementReferenceException:
        return False
    return True

def test_burger_menu_reset():
    browser.get(f'{MAIN_PAGE}inventory.html')
    # add item to cart
    backpack_add_button = browser.find_element(By.ID, BACKPACK_ADD_BUTTON)
    backpack_add_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, CART_BUTTON)
    cart_button.click()
    cart_badge = browser.find_element(By.XPATH, CART_LOGO_BADGE)
    # assert that number of items in the cart is displayed
    assert is_displayed(cart_badge) is True
    browser.find_element(By.ID, BURGER_MENU).click()
    browser.find_element(By.ID, BURGER_MENU_ITEMS[3]).click()
    # assert that number of items in the cart is not displayed
    assert is_displayed(cart_badge) is False


def teardown():
    browser.quit()
