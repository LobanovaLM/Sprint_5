from selenium.webdriver.common.by import By


class ProfilePageLocators:
    MY_ADS_SECTION = (By.XPATH, "//h1[contains(text(), 'Мои объявления')]")
    AD_ITEM = (By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div[1]')
    AD_TITLE = (By.XPATH, "//h2[contains(text(), 'Тестовое объявление')]")