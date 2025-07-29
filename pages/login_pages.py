from selenium.webdriver.common.by import By
from pages.base_pages import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

    def go_to_login(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.write(self.USERNAME, username)
        self.write(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_logged_in(self):
        return "inventory" in self.driver.current_url
    
    
