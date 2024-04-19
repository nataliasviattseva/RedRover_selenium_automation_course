from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators import *
from data import LOGIN, PASSWORD, MAIN_PAGE

browser = webdriver.Chrome()


def setup_function():
    browser.get(MAIN_PAGE)
    browser.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    browser.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    browser.find_element(By.XPATH, LOGIN_BUTTON).click()


# 1. Проверка работоспособности фильтра (A to Z)
def test_a_z_filter():
    browser.get(f'{MAIN_PAGE}inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, FILTER_ELEMENT)
    drop = Select(filtering)
    drop.select_by_visible_text(FILTER_VALUES[0])
    first_item = browser.find_element(By.XPATH, FIRST_ELEMENT)
    assert first_item.text == ITEM_TEXT[0]


# 2. Проверка работоспособности фильтра (Z to A)
def test_z_a_filter():
    browser.get(f'{MAIN_PAGE}inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, FILTER_ELEMENT)
    drop = Select(filtering)
    drop.select_by_visible_text(FILTER_VALUES[1])
    first_item = browser.find_element(By.XPATH, FIRST_ELEMENT)
    assert first_item.text == ITEM_TEXT[1]


# 3. Проверка работоспособности фильтра (low to high)
def test_low_to_high_filter():
    browser.get(f'{MAIN_PAGE}inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, FILTER_ELEMENT)
    drop = Select(filtering)
    drop.select_by_visible_text(FILTER_VALUES[2])
    first_item = browser.find_element(By.XPATH, FIRST_ELEMENT)
    assert first_item.text == ITEM_TEXT[2]


# 4. Проверка работоспособности фильтра (high to low)
def test_high_to_low_filter():
    browser.get(f'{MAIN_PAGE}inventory.html')
    filtering = browser.find_element(By.CLASS_NAME, FILTER_ELEMENT)
    drop = Select(filtering)
    drop.select_by_visible_text(FILTER_VALUES[3])
    first_item = browser.find_element(By.XPATH, FIRST_ELEMENT)
    assert first_item.text == ITEM_TEXT[3]
