from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_content(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_content")

    # Esperamos a que se carguen los textos
    contents_before = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content .row .large-10.columns"))
    )

    # Guardamos los textos antes del refresh
    texts_before = [content.text for content in contents_before]

    # Recargamos la página
    driver.refresh()

    # Esperamos nuevamente los nuevos textos
    contents_after = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content .row .large-10.columns"))
    )

    # Guardamos los textos después del refresh
    texts_after = [content.text for content in contents_after]

    # Verificamos si al menos uno de los textos cambió
    cambios = [before != after for before, after in zip(texts_before, texts_after)]

    assert any(cambios), "El contenido no cambió después de recargar la página"
