from selenium.webdriver.common.by import By
from pages.base_pages import BasePage

class InventoryPage(BasePage):
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        xpath = (By.XPATH, self.ADD_TO_CART_BUTTON.format(product_name))
        self.click(xpath)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [el.text for el in elements]
