from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTRATION_EMAIL = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD2 = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")

