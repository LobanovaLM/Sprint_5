import pytest
from pages.auth_page import AuthPage
from pages.create_add_page import CreateAdPage
from pages.profile_page import ProfilePage
from utils.data import TestData


class TestAdvertisement:
    """Тесты создания объявлений"""
    
    def test_create_ad_unauthorized(self, driver, main_page):
        """Создание объявления неавторизованным пользователем"""
        # Пытаемся создать объявление
        main_page.click_create_ad_button()
        
        # Проверяем отображение модального окна
        create_ad_page = CreateAdPage(driver)
        assert create_ad_page.is_auth_modal_displayed()
        assert TestData.WARNING_LOG in create_ad_page.get_auth_modal_title()
    
    def test_create_ad_authorized(self, authenticated_user, main_page):
        """Авторизация перед тестом создания объявления"""
        driver = authenticated_user
        
        """Создание объявления авторизованным пользователем"""
        # Открываем страницу создания объявления
        main_page.click_create_ad_button()
        create_ad_page = CreateAdPage(driver)
        
        # Создаем объявление
        create_ad_page.create_advertisement(
            title=TestData.AD_TITLE,
            description=TestData.AD_DESCRIPTION,
            price=TestData.AD_PRICE,
            category=TestData.AD_CATEGORY,
            city=TestData.AD_CITY,
            condition="new"
        )

        # Переходим в профиль
        driver.get(TestData.PROFILE_URL)
        profile_page = ProfilePage(driver)
        
        # Проверяем, что объявление отображается в профиле
        assert profile_page.is_my_ads_section_visible(), "Раздел 'Мои объявления' не отображается"
        assert profile_page.get_ads_count() > 0, "В профиле нет объявлений"
        assert profile_page.is_ad_with_title_present(TestData.AD_TITLE), \
            f"Объявление с заголовком '{TestData.AD_TITLE}' не найдено в профиле"