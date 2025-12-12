import pytest
from pages.auth_page import AuthPage
from utils.data import TestData


class TestLogout:
    """Тесты выхода из системы"""
    
    def test_successful_logout(self, authenticated_user, main_page):
        self.driver = authenticated_user
        """Успешный выход из системы"""
        # Выходим из системы
        main_page.click_logout_button()
        
        # Проверяем, что отображается кнопка "Вход и регистрация"
        assert main_page.is_login_button_displayed()