from selenium.webdriver.common.by import By


class Links():
    PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_URL_PART = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name = 'registration_submit']")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner p')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(1) strong')
    BASKET_SUM_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-child(3) strong')


class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
