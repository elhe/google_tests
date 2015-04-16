from support.ui.main_page import MainPage
from support.utils import report_result
from support.words_generator import random_word


__author__ = 'elhe'


class TestMainPage():
    def test_random_search(self, browser):
        """
        Search by Google and report first 3 links
        """
        query = random_word()

        page = MainPage(browser)
        result_page = page.search(query)
        results = result_page.get_results_links()

        # TODO make a py.test hook
        report_result(browser, 'Simple search by google', {'links': results[:3], 'query': query})


