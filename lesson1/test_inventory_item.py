from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions

browser = webdriver.Chrome()


def setup_function():
    browser.get('https://www.saucedemo.com')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


# 1. Успешный переход к карточке товара после клика на картинку товара

# i didn't find assert that element doesn't present...
def is_displayed(elem):
    try:
        elem.is_displayed()
    except exceptions.StaleElementReferenceException:
        return False
    return True


def test_move_to_the_inventory_item_after_image_click():
    browser.get('https://www.saucedemo.com/inventory.html')
    # not good - it's better to verify that we add and assert the item with the same text
    backpack_image = browser.find_element(By.ID, 'item_4_img_link')
    backpack_image.click()
    inventory_item_frame = browser.find_element(By.ID, 'inventory_item_container')
    assert inventory_item_frame.is_displayed() is True
    backpack_item_text = browser.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    assert backpack_item_text.text == 'Sauce Labs Backpack'


# 2. Успешный переход к карточке товара после клика на название товара
def test_move_to_the_inventory_item_after_title_click():
    browser.get('https://www.saucedemo.com/inventory.html')
    # not good - it's better to verify that we add and assert the item with the same text
    backpack_title = browser.find_element(By.ID, 'item_4_title_link')
    backpack_title.click()
    inventory_item_frame = browser.find_element(By.ID, 'inventory_item_container')
    assert inventory_item_frame.is_displayed() is True
    backpack_item_text = browser.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    assert backpack_item_text.text == 'Sauce Labs Backpack'


def teardown():
    browser.quit()
