from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_WAIT = 10


class Page:

    def __init__(self, driver):
        self.driver = driver

    def element_visible(self, locator, time=MAX_WAIT):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f'Element {locator} is not visible')

    def all_elements_visible(self, locator, time=MAX_WAIT):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f'Element {locator} is not visible')
