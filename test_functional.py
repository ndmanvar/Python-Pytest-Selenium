# test_functional.py

def test_python_org(browser):
    browser.get('http://python.org')
    assert 'Python' in browser.title

def test_python_org123(browser):
    browser.get('http://python.org')
    assert 'Python' in browser.title
