from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    def click_no_account_button(self):
        self.click_element(AuthPageLocators.NO_ACCOUNT_BUTTON)
    
    def click_create_account_button(self):
        self.click_element(AuthPageLocators.CREATE_ACCOUNT_BUTTON)
    
    def click_login_button(self):
        self.click_element(AuthPageLocators.LOGIN_BUTTON)
    
    def enter_email(self, email):
        self.send_keys(AuthPageLocators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        self.send_keys(AuthPageLocators.PASSWORD_INPUT, password)
    
    def enter_confirm_password(self, password):
        self.send_keys(AuthPageLocators.CONFIRM_PASSWORD_INPUT, password)
    
    def register_new_user(self, email, password):
        self.click_no_account_button()
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_create_account_button()
    
    def login_user(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    def is_error_message_displayed(self):
        return self.is_element_present(AuthPageLocators.EMAIL_ERROR)
    
    def is_error_fields_highlighted(self):

        error_fields = self.find_elements(AuthPageLocators.ERROR_FIELDS)
        return len(error_fields) >= 0  # Email, пароль, подтверждение пароля
    
    def get_modal_title(self):
        return self.get_text(AuthPageLocators.MODAL_TITLE)