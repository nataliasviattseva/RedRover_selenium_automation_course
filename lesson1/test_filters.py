from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common import exceptions

browser = webdriver.Chrome()


def setup_function():
    browser.get('https://www.saucedemo.com')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


# 1. Проверка работоспособности фильтра (A to Z)

def test_a_z_filter():
    browser.get('https://www.saucedemo.com/inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    drop = Select(filtering)
    drop.select_by_visible_text('Name (A to Z)')
    first_item = browser.find_element(By.XPATH, '(//*[@data-test="inventory-item-name"])[1]')
    assert first_item.text == 'Sauce Labs Backpack'


# 2. Проверка работоспособности фильтра (Z to A)
def test_z_a_filter():
    browser.get('https://www.saucedemo.com/inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    drop = Select(filtering)
    drop.select_by_visible_text('Name (Z to A)')
    first_item = browser.find_element(By.XPATH, '(//*[@data-test="inventory-item-name"])[1]')
    assert first_item.text == 'Test.allTheThings() T-Shirt (Red)'


# 3. Проверка работоспособности фильтра (low to high)
def test_low_to_high_filter():
    browser.get('https://www.saucedemo.com/inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    drop = Select(filtering)
    drop.select_by_visible_text('Price (low to high)')
    first_item = browser.find_element(By.XPATH, '(//*[@data-test="inventory-item-name"])[1]')
    assert first_item.text == 'Sauce Labs Onesie'


# 4. Проверка работоспособности фильтра (high to low)
def test_high_to_low_filter():
    browser.get('https://www.saucedemo.com/inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    drop = Select(filtering)
    drop.select_by_visible_text('Price (high to low)')
    first_item = browser.find_element(By.XPATH, '(//*[@data-test="inventory-item-name"])[1]')
    assert first_item.text == 'Sauce Labs Fleece Jacket'
