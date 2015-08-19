import os
import unittest
import sys
import new
from selenium import webdriver

browsers = [{
      "platform": "Linux",
      "browserName": "chrome",
      "version": "31"
  }, {
      "platform": "Windows 8.1",
      "browserName": "internet explorer",
      "version": "11"
  }, {
      "platform": "OS X 10.9",
      "browserName": "safari",
      "version": "7.0"
  }, {
      "platform": "Windows 7",
      "browserName": "chrome",
      "version": "33.0"
  }]

username = os.environ['SAUCE_USERNAME']
access_key = os.environ['SAUCE_ACCESS_KEY']

# This decorator is required to iterate over browsers
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator

@on_platforms(browsers)
class FirstSampleTest(unittest.TestCase):

    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.driver = webdriver.Remote(
           command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key),
           desired_capabilities=self.desired_capabilities)
        self.driver.implicitly_wait(30)

# This is your test logic. You can add multiple tests here.
    def test_google(self):
        self.driver.get("http://www.google.com")
        if not "Google" in self.driver.title:
            raise Exception("Unable to load google page!")
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("Sauce Labs")
        elem.submit()

    def tearDown(self):
        # This is where you tell Sauce Labs to stop running tests on your behalf.  
        # It is important so that you aren't billed after your test finishes.
        self.driver.quit()