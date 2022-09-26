from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def wait_until_displayed(self, xpath):
        """Wait until element is displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located(By.XPATH, xpath))

    def wait_until_clickable(self, xpath):
        """Wait until element is clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable(By.XPATH, xpath))

    def fill_field(self, xpath, value):
        """Find, Clear and fill field"""
        element = self.wait_until_clickable(xpath=xpath)
        # element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click"""
        self.wait_until_clickable(xpath=xpath).click()
        # self.driver.find_element(by=By.XPATH, value=xpath).click()

    def verify_url(self, expected_url):
        """Verify success Sign Up using URL"""
        assert expected_url == self.driver.current_url

    def verify_text(self, xpath, text):
        """Verify success Sign Up using button"""
        element = self.driver.find_element(By.XPATH, xpath)
        assert element.text == text
