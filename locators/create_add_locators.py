from selenium.webdriver.common.by import By


class CreateAdLocators:
    # Поля формы
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    CATEGORY = (By.XPATH, "//span[contains(text(), 'Книги')]")
    CITY_DROPDOWN = (By.XPATH, "//input[@value='Москва' and @name='city']/following-sibling::button")
    CITY = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

    # Radio buttons
    CONDITION_NEW = (By.XPATH, "//div[.//input[@value='Новый'] and contains(@class, 'radioUnput_shell__Wtdwe')]")
    CONDITION_USED = (By.XPATH, "//div[.//input[@value='Б/У'] and contains(@class, 'radioUnput_shell__Wtdwe')]")
    
    # Модальное окно для неавторизованных
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")