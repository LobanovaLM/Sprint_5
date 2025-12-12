import pytest
from pages.auth_page import AuthPage
from utils.data import TestData
from utils.helpers import generate_random_email, generate_random_password


class TestRegistration:
    """Тесты регистрации пользователя"""
    
    def test_successful_registration(self, driver, main_page):
        """Регистрация нового пользователя"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver)
        
        # Регистрируем нового пользователя
        email = generate_random_email()
        password = generate_random_password()
        auth_page.register_new_user(email, password)
        
        # Проверяем, что произошел переход на главную страницу
        assert driver.current_url == TestData.INPUT_URL
        
        # Проверяем отображение аватара и имени пользователя
        assert main_page.is_user_avatar_displayed()
        assert main_page.is_user_name_displayed()
        assert main_page.get_user_name() == "User."
    
    def test_registration_with_invalid_email(self, driver, main_page):
        """Регистрация с email не по маске"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver)
        
        # Нажимаем "Нет аккаунта"
        auth_page.click_no_account_button()
        
        # Заполняем поле email невалидным значением
        auth_page.enter_email(TestData.INVALID_EMAIL)
        
        # Нажимаем "Создать аккаунт"
        auth_page.click_create_account_button()
        
        # Проверяем выделение полей красным
        assert auth_page.is_error_fields_highlighted()
        
        # Проверяем отображение сообщения об ошибке
        assert auth_page.is_error_message_displayed()
    
    @pytest.mark.parametrize("email,password", [
        (TestData.EXISTING_USER_EMAIL, TestData.EXISTING_USER_PASSWORD),
    ])
    def test_registration_existing_user(self, driver, main_page, email, password):
        """Регистрация уже существующего пользователя"""
        # Открываем страницу авторизации
        main_page.click_login_register_button()
        auth_page = AuthPage(driver)
        
        # Пытаемся зарегистрировать существующего пользователя
        auth_page.register_new_user(email, password)
        
        # Проверяем выделение полей красным
        assert auth_page.is_error_fields_highlighted()
        
        # Проверяем отображение сообщения об ошибке
        assert auth_page.is_error_message_displayed()