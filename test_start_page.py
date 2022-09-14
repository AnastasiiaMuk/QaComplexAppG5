import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_random_login(self):
        driver = webdriver.Chrome("C:\\Users\\dvale\\Documents\\QAAutomation\\QaComplexAppG6\\chromedriver.exe")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        username = driver.find_element(By.XPATH, './/input[@placeholder="Pick a username"]')
        random_username = random.randrange(1000, 9999, 1)
        username.send_keys('user' + str(random_username))
        sleep(1)

        email = driver.find_element(By.XPATH, './/input[@placeholder="you@example.com"]')
        random_email = random.randrange(1000, 9999, 1)
        email.send_keys(str(random_email) + '@gmail.com')
        sleep(1)

        password = driver.find_element(By.XPATH, './/input[@placeholder="Create a password"]')
        password.send_keys('999666333999')
        sleep(1)

        button_sign_up = driver.find_element(By.XPATH, '//button[text()="Sign up for OurApp"]')
        button_sign_up.click()

        url = "https://qa-complex-app-for-testing.herokuapp.com/"
        get_url = driver.current_url
        assert url == get_url

        button_create_post = driver.find_element(By.XPATH, './/a[text()="Create Post"]')
        value_button_create_post = button_create_post.text
        assert value_button_create_post == "Create Post"

        button_sign_out = driver.find_element(By.XPATH, './/button[text()="Sign Out"]')
        value_button_sign_out = button_sign_out.text
        assert value_button_sign_out == "Sign Out"

        sleep(5)
