from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):
    COMMUNITY_OPT = (By.XPATH, "//div[text()='Community']")

    def click_community(self):
        self.wait_for_element_click(*self.COMMUNITY_OPT)