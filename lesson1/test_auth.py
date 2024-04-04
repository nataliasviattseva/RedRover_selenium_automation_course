from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


# 1. Авторизация используя корректные данные (standard_user, secret_sauce)
def test_auth_positive():
    browser.get('https://www.saucedemo.com')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'


# 2. Авторизация используя некорректные данные (user, user)
def test_auth_negative():
    browser.get('https://www.saucedemo.com')
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('user')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    error_message = browser.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert error_message.text == 'Epic sadface: Username and password do not match any user in this service'


def teardown():
    browser.quit()
