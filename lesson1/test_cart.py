import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions

browser = webdriver.Chrome()


def setup_function():
    browser.get('https://www.saucedemo.com')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


# 1. Добавление товара в корзину через каталог
def test_add_to_cart_from_catalog():
    browser.get('https://www.saucedemo.com/inventory.html')
    # not good - it's better to verify that we add and assert the item with the same text
    backpack_add_button = browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    backpack_add_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()
    backpack_item = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    assert backpack_item.is_displayed() is True
    assert backpack_item.text == 'Sauce Labs Backpack'


# 2. Удаление товара из корзины через корзину

# i didn't find assert that element doesn't present...
def is_displayed(elem):
    try:
        elem.is_displayed()
    except exceptions.StaleElementReferenceException:
        return False
    return True


def test_delete_from_cart_in_the_cart():
    browser.get('https://www.saucedemo.com/cart.html')
    backpack_item = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    assert backpack_item.is_displayed() is True
    backpack_delete_button = browser.find_element(By.ID, 'remove-sauce-labs-backpack')
    backpack_delete_button.click()
    assert is_displayed(backpack_item) is False


# 3. Добавление товара в корзину из карточки товара
def test_add_to_cart_from_inventory_item():
    browser.get('https://www.saucedemo.com/inventory-item.html?id=4')
    add_to_cart_button = browser.find_element(By.ID, 'add-to-cart')
    add_to_cart_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()
    backpack_item = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    assert backpack_item.is_displayed() is True
    assert backpack_item.text == 'Sauce Labs Backpack'


# 4. Удаление товара из корзины через карточку товара
def test_delete_from_cart_from_inventory_item():
    cart_button = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()
    backpack_item = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    assert is_displayed(backpack_item) is True
    browser.get('https://www.saucedemo.com/inventory-item.html?id=4')
    remove_button = browser.find_element(By.ID, 'remove')
    remove_button.click()
    cart_button = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button.click()
    assert is_displayed(backpack_item) is False


def teardown():
    browser.quit()
