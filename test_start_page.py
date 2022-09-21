from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_username, random_email, random_password


class TestStartPage:

    def test_random_sign_up(self):
        """
        -Steps:
            - Create driver
            - Open page
            - Generate random username, random email, random password
            - Fill username, email, password
            - Click on Sign Up button
            - Verify registration is successful
            - Close driver
        """

        # Create driver
        driver = webdriver.Chrome(DRIVER_PATH)

        # Open page
        driver.get(BASE_URL)

        start_page = StartPage(driver)

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

        # Close driver
        driver.close()
