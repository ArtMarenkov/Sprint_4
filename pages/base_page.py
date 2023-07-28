from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base_page():
    def __init__(self, driver_fixt):
        self.driver = driver_fixt
        driver_fixt.get("https://qa-scooter.praktikum-services.ru/")

    def scroll_to_element(self, by, locator):
        element = self.driver.find_element(by, locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def click_on_element(self, by, locator):
        self.driver.find_element(by, locator).click()

    def wait_for_element(self, by, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((by, locator)))

    def wait_for_element_is_clickable(self, by, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((by, locator)))

    def get_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def send_keys_to_element(self, by, locator, keys):
        self.driver.find_element(by, locator).send_keys(keys)

    def get_element_text(self, by, locator):
        return self.driver.find_element(by, locator).text

    def switch_to_last_tab(self):
        p = self.driver.current_window_handle
        chwd = self.driver.window_handles
        WebDriverWait(self.driver, 10).until(lambda driver: len(self.driver.window_handles) > 1)
        for w in chwd:
            if (w != p):
                self.driver.switch_to.window(w)
                break

    def check_page_url(self, url):
        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_url == url)

    def is_element_displayed(self, by, locator):
        return self.driver.find_element(by, locator).is_displayed()
