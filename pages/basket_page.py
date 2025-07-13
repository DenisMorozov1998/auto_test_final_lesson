from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .login_page import LoginPage
from .locators import BasketLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_should_be_empty(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketLocators.BASKET_IS_EMPTY_TEXT).text

    def basket_should_not_content_any_items(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS), 'basket is not empty'



    def should_be_basket_page(self):
        assert 'basket' in self.browser.current_url






