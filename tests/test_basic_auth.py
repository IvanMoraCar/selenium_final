from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_enviar_usuario_contrasena_auth(driver):

    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    messeger_element = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/p'))
    )

    assert "Congratulations! You must have the proper credentials." in messeger_element.text, "No es el texto esperado"