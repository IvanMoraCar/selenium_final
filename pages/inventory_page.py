class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_container = "inventory_container"

    def is_loaded(self):
        return self.driver.find_element("id", self.inventory_container).is_displayed()
