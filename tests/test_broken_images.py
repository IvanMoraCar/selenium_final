import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_broken_images(driver):
    driver.get("https://the-internet.hackerearth.com/broken_images")

    images = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, 'img'))
    )

    assert len(images) == 3, "No es la cantidad de imágenes esperadas"

    for i, img in enumerate(images, start=1):
        is_broken = driver.execute_script(
            "return arguments[0].complete && arguments[0].naturalWidth > 0;", img
        )
        assert is_broken, f"La imagen {i} está rota o no se carga"

def test_broken_images_status_code(driver):
    driver.get("https://the-internet.hackerearth.com/broken_images")

    images = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "img"))
    )

    assert len(images) == 3, "No es la cantidad de imágenes esperadas"

    for i, img in enumerate(images, start=1):
        src = img.get_attribute("src")
        response = requests.get(src)
        assert response.status_code == 200, f"La imagen {i} con URL {src} no carga correctamente, status code: {response.status_code}"