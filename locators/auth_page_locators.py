from selenium.webdriver.common.by import By


class AuthPageLocators:
    # Форма авторизации
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # Форма регистрации
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    
    # Сообщения об ошибках
    ERROR_FIELDS = (By.CLASS_NAME, "input_inputError__fLUP9")
    EMAIL_ERROR = (By.CSS_SELECTOR, ".input_span__yWPqB")