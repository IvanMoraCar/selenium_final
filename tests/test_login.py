import logging
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Configurar logging
logging.basicConfig(level=logging.INFO)


# Test de login válido y prueba con jenkies
def test_valid_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    logging.info("Cargando página de login...")
    login_page.load()

    logging.info("Realizando login...")
    login_page.login("standard_user", "secret_sauce")

    logging.info("Verificando que el inventario se haya cargado...")
    assert inventory_page.is_loaded()
