from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SETTINGS_BTN = (By.XPATH, "//div[text()='Settings']")

    def click_settings(self):
        self.wait_for_element_click(*self.SETTINGS_BTN)