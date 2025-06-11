from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_controles_dinamicos_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    button_remove = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[onclick='swapCheckbox()']"))
    )

    button_remove.click()

    # Espera hasta que el checkbox desaparezca
    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.ID, "checkbox")) == 0
    )

    message_text = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert "It's gone!" in message_text.text, "No es el mensaje deseado"

    button_remove.click()

    WebDriverWait(driver, 10).until(
        lambda d: len(d.find_elements(By.ID, "checkbox")) == 1
    )

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.ID, "message"), "It's back!")
    )

    message_text = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert "It's back!" in message_text.text, "No es el mensaje deseado"


def test_controles_dinamicos_textbox(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    text_box = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text']"))
    )

    assert text_box.get_attribute("disabled") is not None, "No está deshabilitado el campo"

    enable_button = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button[onclick='swapInput()']"))
    )

    enable_button.click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )

    # Recapturamos el text_box porque puede haberse reconstruido
    text_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    assert text_box.is_enabled(), "No se puede escribir en el campo"

    text_box.send_keys("Prueba test case 14")

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert "It's enabled!" in message.text, "No es el mensaje deseado"

    enable_button.click()

    WebDriverWait(driver, 5).until(
        lambda d: d.find_element(By.CSS_SELECTOR, "input[type='text']").get_attribute("disabled") is not None
    )

    message = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )
    assert "It's disabled!" in message.text, "No es el mensaje deseado"
