from selenium.webdriver.common.by import By


class CreateAdLocators:
    # Поля формы
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[placeholder='Описание товара']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")
    CATEGORY_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[1]/button')
    CATEGORY = (By.XPATH, "//span[contains(text(), 'Книги')]")
    CITY_DROPDOWN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[1]/button')
    CITY = (By.XPATH, "//span[contains(text(), 'Санкт-Петербург')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

    # Radio buttons
    CONDITION_NEW = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/fieldset/div/div[1]/div')
    CONDITION_USED = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/fieldset/div/div[2]/div')
    
    # Модальное окно для неавторизованных
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")