from sauceclient import SauceClient
from settings import SAUCELAB_USER, SAUCELAB_KEY

__author__ = 'elhe'


def report_result(browser, test_name, custom_data):
    sauce_client = SauceClient(SAUCELAB_USER, SAUCELAB_KEY)
    sauce_client.jobs.update_job(browser.session_id, passed=True, name=test_name,
                                 custom_data=custom_data)