from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_register_button(self):
        self.click_element(MainPageLocators.LOGIN_REGISTER_BUTTON)
    
    def click_create_ad_button(self):
        self.wait_and_click_element(MainPageLocators.CREATE_AD_BUTTON)
    
    def click_logout_button(self):
        self.click_element(MainPageLocators.LOGOUT_BUTTON)
    
    def click_profile_link(self):
        self.click_element(MainPageLocators.PROFILE_LINK)
    
    def is_user_avatar_displayed(self):
        return self.is_element_present(MainPageLocators.USER_AVATAR)
    
    def is_user_name_displayed(self):
        return self.is_element_present(MainPageLocators.USER_NAME)
    
    def is_login_button_displayed(self):
        return self.is_element_present(MainPageLocators.LOGIN_REGISTER_BUTTON)
    
    def get_user_name(self):
        return self.get_text(MainPageLocators.USER_NAME)