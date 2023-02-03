import time

import pytest
from django.urls import reverse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


### Test Log In and Logout ###
@pytest.mark.django_db
def test_login(browser, live_server, test_user, test_user_password):
    # Setup
    url = live_server.url + reverse("login")
    browser.get(url)
    # Test page title.
    assert browser.title == "Log In", "Log In page title should be 'Log In'."
    # Test url
    assert (
        browser.current_url == live_server.url + "/accounts/login/"
    ), "Log In page url should be [live server url]+'/accounts/login/'."
    # Test 'Cancel' link
    try:
        link = browser.find_element(By.LINK_TEXT, "Cancel")
    except NoSuchElementException:
        assert False, "Log In page should include 'Cancel' link."
    link.click()
    assert (
        browser.title == "Site Name"
    ), "Log In page 'Cancel' link should take user to home page."
    browser.back()
    # Test Login - Incorrect credentials
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    username_input.send_keys("bogus_user")
    password_input.send_keys("bogus_password")
    password_input.submit()
    assert (
        "Please enter a correct username and password. Note that both fields may be case-sensitive."
        in browser.page_source
    ), "User should receive error message when attempting to log in with incorrect credentials."
    # Test Login - Correct credentials
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    username_input.clear()
    password_input.clear()
    username_input.send_keys(test_user.username)
    password_input.send_keys(test_user_password)
    password_input.submit()
    assert (
        browser.title == "Site Name"
    ), "Page title incorrect.  Successful login should lead to home page'."
    assert (
        "User" in browser.page_source
    ), "Page source incorrect.  Succesful login should have 'User:' in page source."
    # Test Logout
    url = live_server.url + reverse("logout")
    browser.get(url)
    assert (
        browser.title == "Site Name"
    ), "Page title incorrect.  Logout should redirect to home page'."
    try:
        link = browser.find_element(By.LINK_TEXT, "Log In")
    except NoSuchElementException:
        assert (
            False
        ), "'Log In' link not found.  Logout should redirect to home page with 'Log In' link displayed."


# SNIPPETS FOR DEVELOPMENT
# time.sleep(5)
