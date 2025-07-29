from selenium.webdriver.common.by import By
from pages.base_pages import BasePage

class CartPage(BasePage):
    # Selectores
    CART_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTONS = (By.CLASS_NAME, "cart_button")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    
    def get_title(self):
        return self.get_text(self.CART_TITLE)

    def get_item_names(self):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]

    def remove_all_items(self):
        while True:
            buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
            if not buttons:
                break
            buttons[0].click()


    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
