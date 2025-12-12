import time
import pytest
from pages.auth_page import AuthPage
from pages.create_add_page import CreateAdPage
from pages.profile_page import ProfilePage
from pages.base_page import BasePage
from utils.data import TestData
from selenium.webdriver.support.ui import WebDriverWait


class TestAdvertisement:
    """Тесты создания объявлений"""
    
    def test_create_ad_unauthorized(self, driver, main_page):
        """Создание объявления неавторизованным пользователем"""
        # Пытаемся создать объявление
        main_page.click_create_ad_button()
        
        # Проверяем отображение модального окна
        create_ad_page = CreateAdPage(driver, driver.current_url)
        assert create_ad_page.is_auth_modal_displayed()
        assert "Чтобы разместить объявление, авторизуйтесь" in create_ad_page.get_auth_modal_title()
    
    def test_create_ad_authorized(self, driver, main_page):
        """Авторизация перед тестом создания объявления"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver, driver.current_url)
        
        # Авторизуемся
        auth_page.login_user(
            TestData.EXISTING_USER_EMAIL,
            TestData.EXISTING_USER_PASSWORD
        )
        assert driver.current_url == TestData.LOGIN_URL
        time.sleep(0.5)
        """Создание объявления авторизованным пользователем"""
        # Открываем страницу создания объявления
        main_page.click_create_ad_button()
        create_ad_page = CreateAdPage(driver, driver.current_url)
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
        # main_page.click_profile_link()
        driver.get(TestData.PROFILE_URL)
        profile_page = ProfilePage(driver, driver.current_url)
        
        # Проверяем, что объявление отображается в профиле
        assert profile_page.is_element_present(profile_page.locators.MY_ADS_SECTION)
        ads = profile_page.find_elements(profile_page.locators.AD_ITEM)
        assert len(ads) > 0
        
        # Проверяем заголовок созданного объявления
        ad_titles = profile_page.find_elements(profile_page.locators.AD_TITLE)
        assert any(TestData.AD_TITLE in title.text for title in ad_titles)