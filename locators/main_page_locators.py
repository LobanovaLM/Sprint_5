from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

    # Элементы пользователя
    USER_AVATAR = (By.CSS_SELECTOR,
        "button.circleSmall, .circleSmall svg, [class*='circleSmall']")
    USER_NAME = (By.CSS_SELECTOR,
        "h3.profiletext.name, h3[class*='profiletext'], h3[class*='name']")
    
    # Навигация
    PROFILE_LINK = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/button')