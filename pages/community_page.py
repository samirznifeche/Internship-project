from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By


class CommunityPage(Page):
    SUPPORT_BTN = (By.CSS_SELECTOR, "a.support-fixed-button")

    def verify_page_opens(self):
        self.verify_partial_url('community')

    def verify_contact_support(self):
        self.wait_for_element_clickable(*self.SUPPORT_BTN)