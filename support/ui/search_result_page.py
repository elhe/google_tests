from selenium.webdriver.common.by import By
from support.ui.element import Element

__author__ = 'elhe'


class SearchResultPage():
    RESULT_ENTRY = (By.CSS_SELECTOR, '#ires * h3.r > a')

    def __init__(self, driver):
        self.driver = driver

    def get_results_links(self):
        elements = Element(self.driver, self.RESULT_ENTRY)
        elements.wait()

        return [link.get_attribute('href') for link in elements.find_all()]
