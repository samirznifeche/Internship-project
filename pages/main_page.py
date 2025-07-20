from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MainPage(Page):
    SETTINGS_OPT = (By.XPATH, "//div[text()='Settings']")

    def click_settings(self):
        ### Verify element is displayed (Headless Mode)
        element = self.find_element(*self.SETTINGS_OPT)
        print("Displayed:", element.is_displayed())
        print("Size:", element.size)
        print("Location:", element.location)
        ## Force the element to be visible then click on it using JAVASCRIPT (Headless Mode)
        self.driver.execute_script("""
            const menu = document.querySelector('.menu-block');
            if (menu) {
                menu.style.display = 'block';
                menu.style.visibility = 'visible';
                menu.style.height = 'auto';
                menu.style.width = 'auto';
                menu.style.opacity = '1';
            }
        """)
        sleep(0.5)

        element = self.find_element(*self.SETTINGS_OPT)
        self.driver.execute_script("arguments[0].click();", element)
        # self.wait_for_element_click(*self.SETTINGS_OPT) # For normal browser mode
        # sleep(1) # For firefox browser testing