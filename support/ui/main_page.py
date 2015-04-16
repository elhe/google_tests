from selenium.webdriver.common.by import By
from support.ui.element import Element
from support.ui.search_result_page import SearchResultPage

__author__ = 'elhe'


class MainPage():
    QUERY_INPUT = (By.NAME, 'q')
    SEARCH_BTN = (By.NAME, 'btnG')

    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        Element(self.driver, self.QUERY_INPUT).type(query)
        Element(self.driver, self.SEARCH_BTN).click()
        return SearchResultPage(self.driver)
