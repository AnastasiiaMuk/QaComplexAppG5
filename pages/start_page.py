from time import sleep

from constants.start_page_consts import StartPageConsts
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts()

    def sign_up(self, username, email, password):
        """Sign up as random user"""
        # Fill username, email, password
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(1)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        sleep(1)

    def verify_button_create_post(self):
        """Verify success Sign Up using button Create Post"""
        self.verify_text(xpath=self.constants.BUTTON_CREATE_POST_XPATH, text="Create Post")

    def verify_button_sign_out(self):
        """Verify success Sign Up using button Sign Out"""
        self.verify_text(xpath=self.constants.BUTTON_SIGN_OUT_XPATH, text="Sign Out")
