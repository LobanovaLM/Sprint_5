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
    
    def test_create_ad_authorized(self, driver, main_page):
        """Авторизация перед тестом создания объявления"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver)
        
        # Авторизуемся
        auth_page.login_user(
            TestData.EXISTING_USER_EMAIL,
            TestData.EXISTING_USER_PASSWORD
        )
        main_page.is_user_avatar_displayed()
        
        """Создание объявления авторизованным пользователем"""
        # Открываем страницу создания объявления
        main_page.click_create_ad_button()
        create_ad_page = CreateAdPage(driver)

        assert driver.current_url == TestData.CREATE_URL
        
        # Создаем объявление
        create_ad_page.create_advertisement(
            title=TestData.AD_TITLE,
            description=TestData.AD_DESCRIPTION,
            price=TestData.AD_PRICE,
            category=TestData.AD_CATEGORY,
            city=TestData.AD_CITY,
            condition="new"
        )
        assert driver.current_url == TestData.CREATE_URL
        # Переходим в профиль
        driver.get(TestData.PROFILE_URL)
        profile_page = ProfilePage(driver)
        
        # Проверяем, что объявление отображается в профиле
        assert profile_page.is_element_present(profile_page.locators.MY_ADS_SECTION)
        ads = profile_page.find_elements(profile_page.locators.AD_ITEM)
        assert len(ads) > 0
        
        # Проверяем заголовок созданного объявления
        ad_titles = profile_page.find_elements(profile_page.locators.AD_TITLE)
        assert any(TestData.AD_TITLE in title.text for title in ad_titles)