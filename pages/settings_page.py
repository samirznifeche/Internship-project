from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SettingsPage(Page):
    COMMUNITY_OPT = (By.XPATH, "//div[text()='Community']")

    def click_community(self):
        self.wait_for_element_click(*self.COMMUNITY_OPT)  # For normal browser mode

        ###  Click element on step 4 similarly to the fix for step 3
        # sleep(0.5)
        # self.driver.execute_script("""
        #         const menu = document.querySelector('.menu-block');
        #         if (menu) {
        #             menu.style.display = 'block';
        #             menu.style.visibility = 'visible';
        #             menu.style.height = 'auto';
        #             menu.style.width = 'auto';
        #             menu.style.opacity = '1';
        #         }
        #     """)
        # sleep(0.5)
        #
        # element = self.find_element(*self.COMMUNITY_OPT)
        # self.driver.execute_script("arguments[0].click();", element)