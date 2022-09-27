import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_username, random_email, random_password


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        # Pre-conditions
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1)
        # Steps
        yield StartPage(driver)
        # Post-conditions
        driver.close()

    def test_random_sign_up(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Generate random username, random email, random password
            - Fill username, email, password
            - Click on Sign Up button
            - Verify registration is successful
        """


        # Prepare data
        username_value = random_username()
        email_value = random_email()
        password_value = random_password()

        # Sign Up as a random user
        start_page.sign_up(username_value, email_value, password_value)

        # Verify URL
        start_page.verify_url(BASE_URL)

        # Verify button 'Create Post'
        start_page.verify_button_create_post()

        # Verify button 'Sign Out'
        start_page.verify_button_sign_out()
