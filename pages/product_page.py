from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_add_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "add_to_basket_button is not presented"

    def item_is_added_to_basket(self):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGES)
        name_book_in_basket = messages[0].text
        price_in_basket = messages[-1].text
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert name_book_in_basket == name_book and price_in_basket == book_price, 'Возникла ошибка при добавлении товара в корзину'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGES), \
            "Success message is presented, but should not be"

    def access_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGES)