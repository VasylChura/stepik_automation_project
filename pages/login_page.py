from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        #login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        #login_link.click()
        login_url = self.browser.current_url
        assert "login" in login_url, "This is not login link!!!"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        #login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        #login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "There is no login form!!!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        #login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        #login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "There is no register form!!!"