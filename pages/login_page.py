from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login')

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login_form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register_form is not presented'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_repeat_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_repeat_field.send_keys(password)
        registration_button.click()






