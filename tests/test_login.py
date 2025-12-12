import pytest
from pages.auth_page import AuthPage
from utils.data import TestData


class TestLogin:
    """Тесты авторизации пользователя"""
    
    def test_successful_login(self, driver, main_page):
        """Успешная авторизация"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver, driver.current_url)
        
        # Авторизуемся
        auth_page.login_user(
            TestData.EXISTING_USER_EMAIL,
            TestData.EXISTING_USER_PASSWORD
        )
        
        # Проверяем, что произошел переход на главную страницу
        assert driver.current_url == TestData.LOGIN_URL
        
        # Проверяем отображение аватара и имени пользователя
        assert main_page.is_user_avatar_displayed()
        assert main_page.is_user_name_displayed()
        assert main_page.get_user_name() == "User."