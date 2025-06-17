from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_exit_intent_modal(driver):
    driver.get("https://the-internet.hackerearth.com/exit_intent")

    # Simular movimiento del mouse fuera de la ventana (hacia arriba)
    actions = ActionChains(driver)
    actions.move_by_offset(0, -100).perform()

    try:
        modal = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
        )

        title = modal.find_element(By.CLASS_NAME, "modal-title")
        assert "This is a modal window" in title.text, "❌ El texto del modal no es el esperado"

        close_button = modal.find_element(By.CSS_SELECTOR, ".modal-footer p")
        close_button.click()

        WebDriverWait(driver, 5).until(EC.invisibility_of_element(modal))
        print("✅ Modal se mostró y se cerró correctamente")

    except TimeoutException:
        print("❌ El modal no apareció al mover el mouse fuera de la ventana")

