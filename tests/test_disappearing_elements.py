from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_disappearing_elements(driver):
    driver.get("https://the-internet.herokuapp.com/disappearing_elements")

    # Esperar hasta que al menos un enlace sea visible
    links = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#content a"))
    )

    # Crear una lista de los textos visibles
    visible_link_texts = [link.text for link in links]

    # Verificar los enlaces esperados (excepto el opcional 'Gallery')
    assert "Home" in visible_link_texts, "'Home' no está presente"
    assert "About" in visible_link_texts, "'About' no está presente"
    assert "Contact Us" in visible_link_texts, "'Contact Us' no está presente"
    assert "Portfolio" in visible_link_texts, "'Portfolio' no está presente"

    # Verificar si 'Gallery' aparece esta vez
    if "Gallery" in visible_link_texts:
        print("El enlace 'Gallery' está presente esta vez")
    else:
        print("El enlace 'Gallery' no está presente esta vez")
