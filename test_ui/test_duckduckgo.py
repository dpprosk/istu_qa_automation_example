import unittest
from selenium import webdriver
from pages.main_page import MainPage
from pages.results_page import ResultsPage


class TestDuckduckgo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = MainPage(self.driver)
        self.page.open_main_page()
        self.page.check_load()

    def test_search_popup(self):
        """Смок всплывающей подсказки"""

        self.page.enter_search_string('python')
        self.page.check_search_query_elements()
        suggestions = self.page.get_all_suggestions()
        self.assertGreaterEqual(len(suggestions), 1)

    def test_search_from_suggestion(self):
        """Поиск по первой всплывающей подсказке"""

        # Вводим запрос и переходим по первой подсказке
        query = 'javascript'
        self.page.enter_search_string(query)
        self.page.check_search_query_elements()
        suggestions = self.page.get_all_suggestions()
        suggestions[0].click()

        # Проверяем, что строка запроса содержит текст выбранной подсказки
        results_page = ResultsPage(self.driver)
        results_page.check_load()
        query_input = results_page.get_search_input()
        self.assertEqual(query_input, query)

        # Проверяем, что результаты загрузились и первая ссылка содержит текст запроса
        results = results_page.get_results()
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(query in results[0].text.lower())

    def tearDown(self):
        self.driver.quit()