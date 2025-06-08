from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkboxes_selected(driver):
    driver.get("https://the-internet.hackerearth.com/checkboxes")
    wait = WebDriverWait(driver, 3)

    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
        # Esperar hasta que el checkbox esté seleccionado
        wait.until(lambda driver: checkbox.is_selected())
        assert checkbox.is_selected(), f"El checkbox con valor '{checkbox.get_attribute('value')}' no fue marcado"
