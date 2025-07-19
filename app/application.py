from pages.base_page import Page
from pages.community_page import CommunityPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.sign_in_page import SignInPage


class Application(Page):
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.community_page = CommunityPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.sign_in_page = SignInPage(driver)