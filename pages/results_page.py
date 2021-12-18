from selenium.webdriver.common.by import By
from pages.page import Page

class ResultsPage(Page):

    search_input                =  (By.ID,           'search_form_input')
    results_type_bar            =  (By.ID,           'duckbar_static')
    results                     =  (By.CSS_SELECTOR, '.results .result')

    def check_load(self):
        self.element_visible(self.search_input)
        self.element_visible(self.results_type_bar)

    def get_search_input(self):
        el = self.driver.find_element(*self.search_input)
        return el.get_property('value')

    def get_results(self):
        return self.all_elements_visible(self.results)
