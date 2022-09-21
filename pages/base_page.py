from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, xpath, value):
        """Find, Clear and fill field"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.clear()
        element.send_keys(value)

    def click(self, xpath):
        """Find and click"""
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def verify_url(self, expected_url):
        """Verify success Sign Up using URL"""
        assert expected_url == self.driver.current_url

    def verify_text(self, xpath, text):
        """Verify success Sign Up using button"""
        element = self.driver.find_element(By.XPATH, xpath)
        assert element.text == text
