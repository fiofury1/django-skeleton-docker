# conftest.py
# Includes fixtures used globally across entire project.

import pytest
from mixer.backend.django import mixer
from selenium import webdriver

from accounts.models import CustomUser


@pytest.fixture
def browser():
    """Return a browser instance"""
    # For Browser
    # browser = webdriver.Chrome()
    # For 'Headless' Browser
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def authenticated_browser(authenticated_user, browser, client, live_server):
    """Return a browser instance with logged-in user session."""
    sessionid = client.cookies["sessionid"]
    browser.get(live_server.url)
    browser.add_cookie(
        {"name": "sessionid", "value": sessionid.value, "secure": False, "path": "/"}
    )
    browser.refresh()
    return browser


TESTUSER_USERNAME = "test_user"
TESTUSER_PASSWORD = "my_password123"


@pytest.fixture
def test_user_username():
    return TESTUSER_USERNAME


@pytest.fixture
def test_user_password():
    return TESTUSER_PASSWORD


@pytest.fixture
def test_user():
    user = mixer.blend(CustomUser, username=TESTUSER_USERNAME)
    user.set_password(TESTUSER_PASSWORD)
    user.save()
    return user


@pytest.fixture
def authenticated_user(client):
    user = mixer.blend(CustomUser, username=TESTUSER_USERNAME)
    user.set_password(TESTUSER_PASSWORD)
    user.save()
    client.login(username=TESTUSER_USERNAME, password=TESTUSER_PASSWORD)
    return user
