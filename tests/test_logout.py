import pytest
from pages.auth_page import AuthPage
from utils.data import TestData


class TestLogout:
    """Тесты выхода из системы"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, main_page):
        """Авторизация перед каждым тестом"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver, driver.current_url)
        
        # Авторизуемся
        auth_page.login_user(
            TestData.EXISTING_USER_EMAIL,
            TestData.EXISTING_USER_PASSWORD
        )
        yield
    
    def test_successful_logout(self, driver, main_page):
        """Успешный выход из системы"""
        # Выходим из системы
        main_page.click_logout_button()
        
        # Проверяем, что отображается кнопка "Вход и регистрация"
        assert main_page.is_login_button_displayed()