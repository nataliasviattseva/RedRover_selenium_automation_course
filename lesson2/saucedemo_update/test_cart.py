import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from locators import *
from data import LOGIN, PASSWORD, MAIN_PAGE

browser = webdriver.Chrome()


def setup_function():
    browser.get(MAIN_PAGE)
    browser.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    browser.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    browser.find_element(By.XPATH, LOGIN_BUTTON).click()


# 1. Добавление товара в корзину через каталог
def test_add_to_cart_from_catalog():
    browser.get(f'{MAIN_PAGE}inventory.html')
    # not good - it's better to verify that we add and assert the item with the same text
    backpack_add_button = browser.find_element(By.ID, BACKPACK_ADD_BUTTON)
    backpack_add_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, CART_BUTTON)
    cart_button.click()
    backpack_item = browser.find_element(By.XPATH, BACKPACK_ITEM)
    assert backpack_item.is_displayed() is True
    assert backpack_item.text == ITEM_TEXT[0]


# 2. Удаление товара из корзины через корзину

# i didn't find assert that element doesn't present...
def is_displayed(elem):
    try:
        elem.is_displayed()
    except exceptions.StaleElementReferenceException:
        return False
    return True


def test_delete_from_cart_in_the_cart():
    browser.get(f'{MAIN_PAGE}cart.html')
    backpack_item = browser.find_element(By.XPATH, BACKPACK_ITEM)
    assert backpack_item.is_displayed() is True
    backpack_delete_button = browser.find_element(By.ID, BACKPACK_DELETE_BUTTON)
    backpack_delete_button.click()
    assert is_displayed(backpack_item) is False


# 3. Добавление товара в корзину из карточки товара
def test_add_to_cart_from_inventory_item():
    browser.get(f'{MAIN_PAGE}inventory-item.html?id=4')
    add_to_cart_button = browser.find_element(By.ID, ADD_TO_CART)
    add_to_cart_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, CART_BUTTON)
    cart_button.click()
    backpack_item = browser.find_element(By.XPATH, BACKPACK_ITEM)
    assert backpack_item.is_displayed() is True
    assert backpack_item.text == ITEM_TEXT[0]


# 4. Удаление товара из корзины через карточку товара
def test_delete_from_cart_from_inventory_item():
    cart_button = browser.find_element(By.CLASS_NAME, CART_BUTTON)
    cart_button.click()
    backpack_item = browser.find_element(By.XPATH, BACKPACK_ITEM)
    assert is_displayed(backpack_item) is True
    browser.get(f'{MAIN_PAGE}inventory-item.html?id=4')
    remove_button = browser.find_element(By.ID, REMOVE_BUTTON)
    remove_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, CART_BUTTON)
    cart_button.click()
    assert is_displayed(backpack_item) is False


def teardown():
    browser.quit()
