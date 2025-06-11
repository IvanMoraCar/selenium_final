from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_catch_alert_messenger(driver):

    driver.get("https://the-internet.herokuapp.com/context_menu")

    hot_spot = WebDriverWait(driver, 10). until(
        EC.visibility_of_element_located((By.ID, "hot-spot"))
    )

    actions = ActionChains(driver)
    actions.context_click(hot_spot).perform()

    alert = driver.switch_to.alert
    alert_text = alert.text

    assert "You selected a context menu" in alert_text, "No el texto no es correcto"


