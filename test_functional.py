

def test_python_org(browser):
    browser.get("http://www.google.com")
    if not "Google" in browser.title:
        raise Exception("Unable to load google page!")
    elem = browser.find_element_by_name("q")
    elem.send_keys("Sauce Labs")
    elem.submit()
