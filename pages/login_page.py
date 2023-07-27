from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "accounts/login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login username is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration e-mail is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD1), "Registration password1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD2), "Registration password2 is not presented"