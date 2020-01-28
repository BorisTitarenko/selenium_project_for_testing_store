from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL_PART in self.browser.current_url.split("/"), "Login link is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*(LoginPageLocators.LOGIN_FORM)), "Login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*(LoginPageLocators.REGISTER_FORM)), "Register form isn't presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit_button.click()
