class ExamplePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.hackerearth.com/"

    def load(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
