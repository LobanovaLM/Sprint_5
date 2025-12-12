"""
Page Object Model для страницы профиля пользователя
"""
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    """Класс для работы со страницей профиля пользователя"""
    
    def __init__(self, driver, url=None):
        super().__init__(driver, url)
        self.locators = ProfilePageLocators()  # Создаем экземпляр локаторов
    