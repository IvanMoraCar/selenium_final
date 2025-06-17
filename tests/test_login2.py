from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_login_success():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Ingresar usuario y contraseña correctos
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    # Esperar 2 segundos para ver resultados (solo durante pruebas iniciales)
    time.sleep(2)

    # Validar redirección y mensaje
    assert "Logged In Successfully" in driver.page_source

    driver.quit()
