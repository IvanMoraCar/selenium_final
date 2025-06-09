from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_dropdown_options(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Esperar que el dropdown sea visible
    dropdown_element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "dropdown"))
    )

    # Crear objeto Select
    select = Select(dropdown_element)

    # Obtener lista de opciones
    options = select.options

    # Validar textos de las opciones (índices 0, 1, 2)
    assert "Please select an option" == options[0].text, "Texto de la opción inicial inválido"
    assert "Option 1" == options[1].text, "Texto de option 1 inválido"
    assert "Option 2" == options[2].text, "Texto de option 2 inválido"

    # Seleccionar "Option 2"
    select.select_by_visible_text("Option 2")

    # Verificar que "Option 2" está seleccionada
    selected_option = select.first_selected_option
    assert selected_option.text == "Option 2", "La opción seleccionada no es Option 2"
