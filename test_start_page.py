import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_random_sign_up(self):
        """
        -Steps:
            - Create driver
            - Open page
            - Generate random username
            - Fill username
            - Generate random email
            - Fill email
            - Fill password
            - Click button
            - Verify URL
            - Verify button 'Create Post'
            - Verify button 'Sign Out'
            - Close driver
        """

        # Create driver
        driver = webdriver.Chrome("C:\\Users\\dvale\\Documents\\QAAutomation\\QaComplexAppG6\\chromedriver.exe")

        # Open page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Generate random username
        random_username = random.randrange(1000, 9999, 1)

        # Fill username
        username = driver.find_element(By.XPATH, './/input[@placeholder="Pick a username"]')
        username.send_keys('user' + str(random_username))
        sleep(1)

        # Generate random email
        random_email = random.randrange(1000, 9999, 1)

        # Fill email
        email = driver.find_element(By.XPATH, './/input[@placeholder="you@example.com"]')
        email.send_keys(str(random_email) + '@gmail.com')
        sleep(1)

        # Fill password
        password = driver.find_element(By.XPATH, './/input[@placeholder="Create a password"]')
        password.send_keys('999666333999')
        sleep(1)

        # Click button
        button_sign_up = driver.find_element(By.XPATH, '//button[text()="Sign up for OurApp"]')
        button_sign_up.click()

        # Verify URL
        url = "https://qa-complex-app-for-testing.herokuapp.com/"
        get_url = driver.current_url
        assert url == get_url

        # Verify button 'Create Post'
        button_create_post = driver.find_element(By.XPATH, './/a[text()="Create Post"]')
        value_button_create_post = button_create_post.text
        assert value_button_create_post == "Create Post"

        # Verify button 'Sign Out'
        button_sign_out = driver.find_element(By.XPATH, './/button[text()="Sign Out"]')
        value_button_sign_out = button_sign_out.text
        assert value_button_sign_out == "Sign Out"

        # Close driver
        driver.close()
