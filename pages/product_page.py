from .locators import ProductPageLocators
from selenium import webdriver
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        submit = self.browser.find_element(*(ProductPageLocators.ADD_BUTTON))
        submit.click()

    def should_be_product_name_in_message(self):
        product_name = self.browser.find_element(*(ProductPageLocators.PRODUCT_NAME)).text
        message = self.browser.find_element(*(ProductPageLocators.PRODUCT_ADDED_MESSAGE)).text
        assert product_name == message, "Added to basket product name isn't presented"

    def should_be_product_price_in_message(self):
        product_price = self.browser.find_element(*(ProductPageLocators.PRODUCT_PRICE)).text
        message = self.browser.find_element(*(ProductPageLocators.BASKET_SUM_MESSAGE)).text
        assert product_price == message, "Basket sum isn't correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message is presented"


    def should_message_disapear(self):
        assert self.is_disappeared(*(ProductPageLocators.PRODUCT_ADDED_MESSAGE)), "Message is still on the page"