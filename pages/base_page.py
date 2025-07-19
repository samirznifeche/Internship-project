from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.base_url = 'https://soft.reelly.io/'

    def open_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_for_element_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        )

    def wait_for_element_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        ).click()

    def verify_partial_url(self, partial_url):
        actual_url = self.driver.current_url
        assert partial_url in actual_url,\
            f"Expected partial url '{partial_url}' not in actual URL {actual_url}"