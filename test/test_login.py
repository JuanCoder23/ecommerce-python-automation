import pytest
from utils.driver_factory import create_driver
from pages.login_pages import LoginPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()
