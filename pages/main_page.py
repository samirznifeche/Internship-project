from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SETTINGS_OPT = (By.XPATH, "//div[text()='Settings']")
    MENU_BTN = (By.XPATH, "//*[text()='Menu']")
    SECONDARY_OPT = (By.XPATH, "//div[text()='Secondary']")

    def click_settings(self):
        self.wait_for_element_click(*self.SETTINGS_OPT)
        # sleep(1) # (FIREFOX)

        ### HEADLESS MODE - Verify element is displayed ###
        # element = self.find_element(*self.SETTINGS_OPT)
        # print("Displayed:", element.is_displayed())
        # print("Size:", element.size)
        # print("Location:", element.location)
        #
        # ## HEADLESS MODE - Force the element to be visible then click on it using JAVASCRIPT
        # self.driver.execute_script("""
        #     const menu = document.querySelector('.menu-block');
        #     if (menu) {
        #         menu.style.display = 'block';
        #         menu.style.visibility = 'visible';
        #         menu.style.height = 'auto';
        #         menu.style.width = 'auto';
        #         menu.style.opacity = '1';
        #     }
        # """)
        # sleep(0.5)
        #
        # element = self.find_element(*self.SETTINGS_OPT)
        # self.driver.execute_script("arguments[0].click();", element)

    ### (MOBILE WEB TESTING) ###
    def click_menu(self):
            self.wait_for_element_click(*self.MENU_BTN)

    def click_secondary_option(self):
        self.click(*self.SECONDARY_OPT)

        ### HEADLESS MODE - Verify element is displayed ###
        # element = self.find_element(*self.SECONDARY_OPT)
        # print("Displayed:", element.is_displayed())
        # print("Size:", element.size)
        # print("Location:", element.location)

        ### HEADLESS MODE - Force the element to be visible then click on it using JAVASCRIPT
        # self.driver.execute_script("""
        #     const menu = document.querySelector('.menu-block');
        #     if (menu) {
        #         menu.style.display = 'block';
        #         menu.style.visibility = 'visible';
        #         menu.style.height = 'auto';
        #         menu.style.width = 'auto';
        #         menu.style.opacity = '1';
        #     }
        # """)
        # sleep(0.5)
        #
        # element = self.find_element(*self.SECONDARY_OPT)
        # self.driver.execute_script("arguments[0].click();", element)