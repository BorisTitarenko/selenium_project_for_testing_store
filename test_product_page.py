import pytest
import faker
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import Links


@pytest.mark.with_registration
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Links.LOGIN_PAGE)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = f.password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Links.PRODUCT_PAGE)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Links.PRODUCT_PAGE)
        page.open()
        page.add_to_basket()
        page.should_be_product_name_in_message()
        page.should_be_product_price_in_message()


base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
@pytest.mark.skip
@pytest.mark.parametrize('link', [f"{base_link}{i}" for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_message()
    page.should_be_product_price_in_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.add_to_basket()
    page.should_message_disapear()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.add_to_basket()
    page.should_be_product_name_in_message()
    page.should_be_product_price_in_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, Links.PRODUCT_PAGE)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_empty_basket_message()
