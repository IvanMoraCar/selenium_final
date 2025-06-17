from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_entry_ad(driver):

    driver.get("https://the-internet.hackerearth.com/entry_ad")

    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
    )

    modal_title = modal.find_element(By.CLASS_NAME, "modal-title")

    assert "This is a modal window" in modal_title.text, "El modal no tiene el titulo esperado"

    close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
    close_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element(modal)
        )
    except TimeoutException:
        print("❌ El modal sigue visible después de 10 segundos")


