# conftest.py

import os
import pytest
from selenium import webdriver

username = os.environ['SAUCE_USERNAME']
access_key = os.environ['SAUCE_ACCESS_KEY']

WEBDRIVER_ENDPOINT = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key)

@pytest.yield_fixture
def browser(request):
    driver = webdriver.Remote(
        command_executor = WEBDRIVER_ENDPOINT,
        desired_capabilities = {
        	'browserName': 'chrome',
        	'version': 41,
        	'platform': 'XP'
        }
    )
    yield driver
    driver.quit()
