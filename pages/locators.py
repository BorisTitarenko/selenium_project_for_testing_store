from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_URL_PART = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    BASKET_SUM_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')