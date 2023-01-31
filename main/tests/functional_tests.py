### main/tests/functional_tests.py ###

# Include functional/integration testing at the 'main' app level.

import time

import pytest
from django.urls import reverse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


### Test of django-skeleton's generic home page. ###
#   
# The home page is meant to be customized for the website being build with django-skeleton.
# As a result, the tests below should be updated when the content of the home page is modified.
# 
# Test home page for Unauthenticated User  
@pytest.mark.django_db
def test_home_page_for_unauthenticated_user(browser, live_server):
    # Setup
    url = live_server.url + reverse('main:home')
    browser.get(url)
    # Test page title
    assert browser.title == "Site Name", "Home page title should be 'SITE NAME'."
    # Test url
    assert browser.current_url == live_server.url+'/', "Home page url should be [live server url]+'/'."
    # Test Log in Link
    try:
        link = browser.find_element(By.LINK_TEXT, "Log In")
    except NoSuchElementException:
        assert False, "Home page should include 'Log in' link for unauthenticated user."
    
    link.click()
    assert browser.title == "Log In", "Log In link should lead to Log In Page'."
    browser.back()
    # Test Sign up link
    try:
        link = browser.find_element(By.LINK_TEXT, "Sign Up")
    except NoSuchElementException:
        assert False, "Home page should include 'Sign Up' link for unauthenticated user."
    
    link.click()
    assert browser.title == "Sign Up", "Sign Up link should lead to Sign Up Page'."
    browser.back()
    # Test GitHub repo link - Intentionally ignored

# Test home page for Authenticated User  
@pytest.mark.django_db
def test_home_page_for_authenticated_user(authenticated_browser, live_server):
    # Setup
    url = live_server.url + reverse('main:home')
    browser = authenticated_browser
    browser.get(url)
    # Test page title
    assert browser.title == "Site Name", "Home page title should be 'SITE NAME'."
    # Test url
    assert browser.current_url == live_server.url+'/', "Home page url should be [live server url]+'/'."
    # Test page shows current user - test in test_templates.py
    # Test Log Out Link
    try:
        link = browser.find_element(By.LINK_TEXT, "Log Out")
    except NoSuchElementException:
        assert False, "Home page should include 'Log Out' link for authenticated user."
    link.click()
    assert browser.title == "Site Name", "Home page title should still be 'SITE NAME'."
    # # Test GitHub repo link - Intentionally ignored
