import pytest
from utils.driver_factory import create_driver
from pages.login_pages import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_checkout_flow(driver):
   
    login = LoginPage(driver)
    login.go_to_login()
    login.login("standard_user", "secret_sauce")

    
    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    assert inventory.cart_count() == "1"

    
    inventory.go_to_cart()

   
    cart = CartPage(driver)
    assert "Sauce Labs Backpack" in cart.get_item_names()
    cart.proceed_to_checkout()

    
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form("Juan", "Sandoval", "110111")
    checkout.click_continue()

  
    checkout.click_finish()

   
    message = checkout.get_confirmation_message()
    assert message == "Thank you for your order!"
