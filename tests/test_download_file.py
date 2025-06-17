# en tu test
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_downloadfile(driver):
    driver.get("https://the-internet.hackerearth.com/download")

    link_file = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "some-file.txt"))
    )
    link_file.click()

    # Espera activa más fiable que sleep:
    WebDriverWait(driver, 10).until(
        lambda d: os.path.exists(r"C:\Users\sombi\Downloads\some-file.txt")
    )

    assert os.path.exists(r"C:\Users\sombi\Downloads\some-file.txt"), \
        "❌ El archivo 'some-file.txt' no fue descargado"
