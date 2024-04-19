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


# 1. Успешный переход к карточке товара после клика на картинку товара

# i didn't find assert that element doesn't present...
def is_displayed(elem):
    try:
        elem.is_displayed()
    except exceptions.StaleElementReferenceException:
        return False
    return True


def test_move_to_the_inventory_item_after_image_click():
    browser.get(f'{MAIN_PAGE}inventory.html')
    # not good - it's better to verify that we add and assert the item with the same text
    backpack_image = browser.find_element(By.ID, BACKPACK_IMAGE)
    backpack_image.click()
    inventory_item_frame = browser.find_element(By.ID, INVENTORY_ITEM_FRAME)
    assert inventory_item_frame.is_displayed() is True
    backpack_item_text = browser.find_element(By.XPATH, BACKPACK_ITEM_TEXT)
    assert backpack_item_text.text == ITEM_TEXTS[0]


# 2. Успешный переход к карточке товара после клика на название товара
def test_move_to_the_inventory_item_after_title_click():
    browser.get(f'{MAIN_PAGE}inventory.html')
    # not good - it's better to verify that we add and assert the item with the same text
    backpack_title = browser.find_element(By.ID, BACKPACK_TITLE)
    backpack_title.click()
    inventory_item_frame = browser.find_element(By.ID, INVENTORY_ITEM_FRAME)
    assert inventory_item_frame.is_displayed() is True
    backpack_item_text = browser.find_element(By.XPATH, BACKPACK_ITEM_TEXT)
    assert backpack_item_text.text == ITEM_TEXTS[0]


def teardown():
    browser.quit()
