import pytest
from utils.driver_factory import create_driver
from pages.login_pages import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_add_and_remove_item_from_cart(driver):
   
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("standard_user", "secret_sauce")

   
    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    assert inventory.cart_count() == "1"

  
    inventory.go_to_cart()

   
    cart = CartPage(driver)
    items = cart.get_item_names()
    assert "Sauce Labs Backpack" in items

    
    cart.remove_all_items()
    assert cart.get_item_names() == []
