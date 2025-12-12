from pages.base_page import BasePage
from locators.create_add_locators import CreateAdLocators


class CreateAdPage(BasePage):
    def enter_title(self, title):
        self.send_keys(CreateAdLocators.TITLE_INPUT, title)
    
    def enter_description(self, description):
        self.send_keys(CreateAdLocators.DESCRIPTION_INPUT, description)
    
    def enter_price(self, price):
        self.send_keys(CreateAdLocators.PRICE_INPUT, price)
    
    def select_category(self, category):
        # Реализация выбора из dropdown
        self.click_element(CreateAdLocators.CATEGORY_DROPDOWN)
        option_locator = (CreateAdLocators.CATEGORY)
        self.click_element(option_locator)
    
    def select_city(self, city):
        # Реализация выбора из dropdown
        self.click_element(CreateAdLocators.CITY_DROPDOWN)
        option_locator = (CreateAdLocators.CITY)
        self.click_element(option_locator)
    
    def select_condition(self, condition="new"):
        if condition == "new":
            self.click_element(CreateAdLocators.CONDITION_NEW)
        else:
            self.click_element(CreateAdLocators.CONDITION_USED)
    
    def click_publish_button(self):
        self.click_element(CreateAdLocators.PUBLISH_BUTTON)
    
    def create_advertisement(self, title, description, price, category, city, condition="new"):
        self.enter_title(title)
        self.enter_description(description)
        self.enter_price(price)
        self.select_category(category)
        self.select_city(city)
        self.select_condition(condition)
        self.click_publish_button()
    
    def get_auth_modal_title(self):
        return self.get_text(CreateAdLocators.AUTH_MODAL_TITLE)
    
    def is_auth_modal_displayed(self):
        return self.is_element_present(CreateAdLocators.AUTH_MODAL_TITLE)