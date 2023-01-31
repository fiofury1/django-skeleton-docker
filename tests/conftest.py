### tests/conftest.py ###

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    # For Browser
    # browser = webdriver.Chrome()
    # For 'Headless' Browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.quit()