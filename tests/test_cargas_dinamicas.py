from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_load(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    button_start = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="start"]/button'))
    )
    button_start.click()

    # Espera a que desaparezca el spinner de carga
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )

    # Ahora espera a que aparezca el texto
    text_hello = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'finish'))
    )

    assert "Hello World!" in text_hello.text, "No es el texto esperado"
