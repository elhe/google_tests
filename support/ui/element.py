from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'elhe'

WAIT_TIMEOUT = 30
LONG_WAIT_TIMEOUT = 60


class Element():
    def __init__(self, browser, criteria):
        self.criteria = criteria
        self.browser = browser

    def find(self):
        try:
            return self.browser.find_element(*self.criteria)
        except NoSuchElementException:
            assert False, 'No element found with %s %s' % self.criteria

    def find_all(self):
        try:
            return self.browser.find_elements(*self.criteria)
        except NoSuchElementException:
            assert False, 'No elements found with %s %s' % self.criteria

    def click(self):
        self.find().click()

    def type(self, value):
        self.find().send_keys(value)

    def wait(self):
        WebDriverWait(self.browser, WAIT_TIMEOUT).until(
            EC.presence_of_element_located(self.criteria)
        )
