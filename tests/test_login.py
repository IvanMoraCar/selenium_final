from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "radius").click()

def test_login(driver):
    login(driver, "tomsmith", "SuperSecretPassword!")

    flash_messenger = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "You logged into a secure area!" in flash_messenger.text, "Error: el mensaje no es el esperado"

def test_login_error(driver):
    login(driver, "wronguser", "wrongpass")

    flash_messenger = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "Your username is invalid!" in flash_messenger.text, "Error: el mensaje no es el esperado"
