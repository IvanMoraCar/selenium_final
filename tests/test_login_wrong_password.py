from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_login_wrong_password():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("wrongPass123")
    driver.find_element(By.ID, "submit").click()

    error_msg = driver.find_element(By.ID, "error").text
    assert error_msg == "Your password is invalid!"
    driver.quit()
