from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button')

    def open_sign_in(self):
        self.open_url('sign-in')

    def log_in(self, email, password):
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BTN)
        # sleep(1) # For BrowserStack