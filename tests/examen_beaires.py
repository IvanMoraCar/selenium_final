from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class MainMethod:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())

        self.driver = webdriver.Chrome(service=service, options=options)

    def fetch_title(self):
        self.driver.get("https://the-internet.hackerearth.com/")
        title = self.driver.title
        return {"title": title}

    def click_redirect_link(self):
        """
            Task:
            1. Navigate to the URL: https://the-internet.hackerearth.com/.
            2. Find the link with the text "Redirect Link" and click on it.
            3. Retrieve the heading text from the redirected page.
            4. Return the heading as an object in the format {"redirector_heading": <heading_value>}.
        """

        self.driver.get("https://the-internet.hackerearth.com/")
        link_redirect = self.driver.find_element(By.LINK_TEXT, "Redirect Link")
        link_redirect.click()
        time.sleep(2)
        heading_text = self.driver.find_element(By.TAG_NAME, "h3")
        heading = heading_text.text
        return {"redirector_heading": heading}

    def fetch_codes(self):
        '''
            Task:
            1. On the redirection page, find and click the button to proceed to the next page.
            2. Wait for the redirection to complete.
            3. Retrieve all the codes displayed on the page.
            4. Return the codes as a list in the format {"codes": <list_of_codes>}.
        '''
        proceed_button = self.driver.find_element(By.ID, "redirect")
        proceed_button.click()
        time.sleep(2)
        code_elements = self.driver.find_elements(By.CSS_SELECTOR, "#content a")
        codes = [elem.text for elem in code_elements if elem.text.isdigit()]
        return {"codes": codes}

    def click_code_500(self):
        '''
            Task:
            1. From the list of codes, find and click on the link corresponding to "500".
            2. Wait for the page to load.
            3. Retrieve the displayed text from the page.
            4. Return the text as an object in the format {"text": <text_value>}.
        '''

        link_500 = self.driver.find_element(By.LINK_TEXT, "500")
        link_500.click()
        try:
            paragraphs = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "p"))
            )
            texts = [p.text for p in paragraphs if p.text.strip() != ""]
            text_combined = " ".join(texts)
        except Exception as e:
            text_combined = f"[Error al obtener el texto: {e}]"

        return {"text": text_combined}

    def quit_driver(self):
        self.driver.quit()


if __name__ == "__main__":
    main_obj = MainMethod()
    print("Title:", main_obj.fetch_title())  # {"title": "..."}
    print("Redirector Heading:", main_obj.click_redirect_link())  # {"redirector_heading": "Redirection"}
    print("Codes:", main_obj.fetch_codes())  # {"codes": ["200", "301", "404", "500"]}
    print("500 Text:", main_obj.click_code_500())  # {"text": "..."}
    main_obj.quit_driver()


