import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



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
    from pages.main_page import MainPage
    from utils.data import TestData
    
    page = MainPage(driver, TestData.BASE_URL)
    page.open()
    return page


@pytest.fixture
def auth_page(driver):
    """Фикстура для страницы авторизации"""
    from pages.auth_page import AuthPage
    from utils.data import TestData
    
    page = AuthPage(driver, TestData.BASE_URL)
    page.open()
    return page