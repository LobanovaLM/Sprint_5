"""
Page Object Model для страницы профиля пользователя
"""
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):
    """Класс для работы со страницей профиля пользователя"""

    def __init__(self, driver, url=None):
        super().__init__(driver, url)
        self.locators = ProfilePageLocators()

    def is_my_ads_section_visible(self):
        """Проверяет видимость раздела 'Мои объявления'"""
        return self.is_element_visible(self.locators.MY_ADS_SECTION)
    
    def get_ads_count(self):
        """Возвращает количество объявлений в профиле"""
        ads = self.find_elements(self.locators.AD_ITEM)
        return len(ads)
    
    def is_ad_with_title_present(self, title):
        """Проверяет наличие объявления с заданным заголовком"""

        ad_titles = self.find_elements(self.locators.AD_TITLE)
        for ad_title in ad_titles:
            if title in ad_title.text:
                return True
        
        return False