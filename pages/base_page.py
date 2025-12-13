from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        if url:
            self.url = url
        else:
            self.url = driver.current_url
    
    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_url_contains(self, text, timeout=10):
        self.wait.until(EC.url_contains(text))
    
    def wait_for_url_to_be(self, url, timeout=10):
        self.wait.until(EC.url_to_be(url))
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def click_element(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def wait_and_click_element(self, locator, timeout=10):
        """Ожидает видимость элемента"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.click()
    
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text
    
    def is_element_present(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False