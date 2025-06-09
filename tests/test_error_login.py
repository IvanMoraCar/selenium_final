from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_error(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    username_textbox = driver.find_element(By.ID, "username")
    username_textbox.send_keys("wronguser")

    password_textbox = driver.find_element(By.ID, "password")
    password_textbox.send_keys("wrongpass")

    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()

    flash_messenger = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )

    assert "Your username is invalid!" in flash_messenger.text, "Error: el mensaje no es el esperado"
