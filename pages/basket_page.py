from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*(BasketPageLocators.BASKET_FORM)), "Basket isn't empty"

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*(BasketPageLocators.BASKET_EMPTY_MESSAGE)).text
        assert message == "Your basket is empty. Continue shopping", message + "isn't correct"
