from selenium.webdriver.common.by import By
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, LOGIN_ERROR_MESSAGE, LOGIN_ERROR_MESSAGE_TEXT
from data import LOGIN, PASSWORD, MAIN_PAGE


def test_login_positive(driver):
    driver.get(MAIN_PAGE)

    # вводим валидный логин в поле "Username"
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    # вводим валидный пароль в поле "Password"
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    # кликаем на кнопку "Login"
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.current_url == f"{MAIN_PAGE}inventory.html"


# 2. Авторизация используя некорректные данные (user, user)
def test_auth_negative(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys('user')
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys('user')
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    assert driver.find_element(By.XPATH, LOGIN_ERROR_MESSAGE).text == LOGIN_ERROR_MESSAGE_TEXT
