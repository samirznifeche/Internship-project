from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SecondaryPage(Page):
    FILTER_BTN = (By.XPATH, "//div[text()='Filters']")
    WANT_TO_SELL_BTN = (By.XPATH, "//div[text()='Want to sell']")
    APPLY_FILTER_BTN = (By.XPATH, "//a[text()='Apply filter']")
    SALE_TAG = (By.XPATH, "//div[text()='For sale']")

    def verify_page(self):
        self.verify_partial_url('secondary')

    def click_filters(self):
        self.click(*self.FILTER_BTN)

    def filter_by_want_to_sell(self):
        self.click(*self.WANT_TO_SELL_BTN)
        sleep(1)

    def click_apply_filter(self):
        self.click(*self.APPLY_FILTER_BTN)

    def verify_sell_tag(self):
        self.find_element(*self.SALE_TAG)