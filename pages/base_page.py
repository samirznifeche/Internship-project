from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.base_url = 'https://soft.reelly.io/'

    def open_url(self, end_url=''):
        url = f'{self.base_url}{end_url}'
        logger.info(f'Opening url: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'Searching for {locator}')
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        logger.info(f"Entering {text} in {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def click(self, *locator):
        logger.info(f'Clicking on {locator}')
        self.driver.find_element(*locator).click()

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def wait_for_element(self, *locator):
        logger.info(f'Waiting for {locator}')
        self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Element by {locator} not found"
        )

    def wait_for_element_clickable(self, *locator):
        logger.info(f'Waiting for {locator} to be clickable')
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        )

    def wait_for_element_click(self, *locator):
        logger.info(f'Waiting and clicking on {locator}')
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by {locator} not clickable"
        ).click()

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        logger.info(f'Verifying current URL: {actual_url}')
        assert actual_url == expected_url, \
            f"Expected URL '{expected_url}' did not match current URL '{actual_url}'"

    def verify_partial_url(self, partial_url):
        actual_url = self.driver.current_url
        logger.info(f'Verifying partial URL: {partial_url}')
        assert partial_url in actual_url,\
            f"Expected partial url '{partial_url}' not in actual URL {actual_url}"