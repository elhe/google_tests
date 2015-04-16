import pytest
from selenium import webdriver
from settings import SAUCELAB_URL, APP_URL

__author__ = 'elhe'


@pytest.fixture(scope="function")
def browser(request):
    # TODO use a comman line args
    desired_capabilities = {
        'platform': "Mac OS X 10.9",
        'browserName': "firefox",
        'version': "35",
    }

    driver = webdriver.Remote(desired_capabilities=desired_capabilities, command_executor=SAUCELAB_URL)
    driver.get(APP_URL)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver