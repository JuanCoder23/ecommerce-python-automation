import pytest
from utils.driver_factory import create_driver
from pages.login_pages import LoginPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("invalid_user", "wrong_password")

   
    error_message = login_page.get_error_message()
    assert "Epic sadface" in error_message
