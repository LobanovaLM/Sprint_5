import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from utils.data import TestData
from pages.auth_page import AuthPage

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    # Настройки Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    # Создаем драйвер
    driver = webdriver.Chrome()
    
    yield driver
    
    # Закрываем драйвер после теста
    driver.quit()


@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    
    page = MainPage(driver)
    page.open(TestData.BASE_URL)
    return page

@pytest.fixture
def auth_page(driver):
    """Фикстура для страницы авторизации"""
    
    return AuthPage(driver)

@pytest.fixture
def authenticated_user(driver, main_page):
    
    # Открываем страницу авторизации
    main_page.click_login_register_button()
    auth_page = AuthPage(driver)
    
    # Авторизуемся
    auth_page.login_user(
        TestData.EXISTING_USER_EMAIL,
        TestData.EXISTING_USER_PASSWORD
    )
    
    # Ждем подтверждения авторизации
    main_page.is_user_avatar_displayed()
    
    print("Авторизация выполнена успешно")
    
    yield driver