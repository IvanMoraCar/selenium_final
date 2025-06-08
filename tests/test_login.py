from selenium.webdriver.common.by import By
import time

def test_login_invalid_credentials(driver):
    driver.get("https://the-internet.hackerearth.com/login")

    # Ingresar usuario y contraseña inválidos
    driver.find_element(By.ID, "username").send_keys("usuario_falso")
    driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)  # Esperar brevemente la aparición del mensaje

    # Verificar que aparece el mensaje de error
    mensaje = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in mensaje
