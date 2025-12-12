# Тестовые данные
class TestData:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru"
    INPUT_URL = "https://qa-desk.stand.praktikum-services.ru/regiatration"
    LOGIN_URL = "https://qa-desk.stand.praktikum-services.ru/login"
    CREATE_URL = "https://qa-desk.stand.praktikum-services.ru/create-lisiting"
    PROFILE_URL = "https://qa-desk.stand.praktikum-services.ru/profile"
    # Существующий пользователь для тестов
    EXISTING_USER_EMAIL = "lobanova_28@gmail.com"
    EXISTING_USER_PASSWORD = "1234567890"
    
    # Данные для создания объявления
    AD_TITLE = "Тестовое объявление"
    AD_DESCRIPTION = "Описание тестового объявления"
    AD_PRICE = "1000"
    AD_CATEGORY = "Книги"
    AD_CITY = "Санкт-Петербург"
    
    # Невалидные данные
    INVALID_EMAIL = "invalid-email"
    SHORT_PASSWORD = "123"

    WARNING_LOG = "Чтобы разместить объявление, авторизуйтесь"