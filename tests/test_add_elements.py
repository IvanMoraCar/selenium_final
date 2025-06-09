from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_elements(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    button_add = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Add Element']"))
    )

    button_add.click()
    button_add.click()
    button_add.click()

    # Esperar hasta que haya 3 botones "Delete"
    WebDriverWait(driver, 5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#elements .added-manually")) == 3
    )

    # Ahora sí obtenemos la lista
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements .added-manually")
    assert len(delete_buttons) == 3, "No hay 3 botones como se esperaba"

    # Hacemos clic en el primero
    delete_buttons[0].click()

    # Esperamos a que queden solo 2
    WebDriverWait(driver, 5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#elements .added-manually")) == 2
    )

    # Verificamos
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, "#elements .added-manually")
    assert len(delete_buttons) == 2, "No hay 2 botones como se esperaba"
