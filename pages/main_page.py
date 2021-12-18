from selenium.webdriver.common.by import By
from pages.page import Page


class MainPage(Page):
    base_url = 'https://duckduckgo.com/'

    search_field                   =  (By.CSS_SELECTOR, '.search--home')
    search_button                  =  (By.CSS_SELECTOR, '.search__button')
    search_input                   =  (By.CSS_SELECTOR, '.search--home input')
    clear_search                   =  (By.CSS_SELECTOR, '.search__clear')
    autocomplete                   =  (By.CSS_SELECTOR, '.search__autocomplete')
    suggestions                    =  (By.CSS_SELECTOR, '.search__autocomplete .acp')

    def open_main_page(self):
        self.driver.get(self.base_url)

    def check_load(self):
        self.element_visible(self.search_field)
        self.element_visible(self.search_button)

    def check_search_query_elements(self):
        self.element_visible(self.clear_search)
        self.element_visible(self.autocomplete)

    def enter_search_string(self, query):
        search_field = self.element_visible(self.search_input)
        search_field.send_keys(query)

    def get_all_suggestions(self):
        return self.all_elements_visible(self.suggestions)
