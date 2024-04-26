USER_NAME = ("css selector", "input[data-test='username']")
PASSWORD = ("css selector", "input[data-test='password']")
LOGIN_BUTTON = ("css selector", "input[data-test='login-button']")
TITLE = ("css selector", "span[data-test='title']")
CARDS = ("css selector", "div[data-test='inventory-item']")


def test_login(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN_BUTTON).click()
    expected_text = "Products"
    actual_text = driver.find_element(*TITLE).text
    assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"


def test_login1(driver):
    driver.get('https://www.saucedemo.com')
    driver.find_element(*USER_NAME).send_keys("standard_user")
    driver.find_element(*PASSWORD).send_keys("secret_sauce")
    driver.find_element(*LOGIN_BUTTON).click()

    cards = driver.find_element()
    expected_text = "Products"
    actual_text = driver.find_element(*TITLE).text
    assert actual_text == expected_text, f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
