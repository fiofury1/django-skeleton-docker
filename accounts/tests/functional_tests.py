import re
import time

import pytest
from django.core import mail
from django.urls import reverse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# Test Log In and Logout
@pytest.mark.django_db
def test_login_and_logout(browser, live_server, test_user, test_user_password):
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
    # Test 'Forgot Password?' Link
    try:
        link = browser.find_element(By.LINK_TEXT, "Forgot Password?")
    except NoSuchElementException:
        assert False, "Log In page should include 'Forgot Password?' link."
    link.click()
    assert (
        browser.title == "Forgot Your Password?"
    ), "Log In page 'Forgot Password?' link should take user to 'Forgot Your Password?' page."
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
    ), "Page title incorrect.  Successful login should redirect to home page'."
    assert (
        "User" in browser.page_source
    ), "Page source incorrect.  Succesful login should redirect to home page with 'User:' displayed."
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


# Test Signup
@pytest.mark.django_db
def test_signup(browser, live_server):
    # Setup
    url = live_server.url + reverse("signup")
    browser.get(url)
    # Test page title
    assert browser.title == "Sign Up", "Title of 'Sign Up' page should be 'Sign Up'."
    # Test url
    assert (
        browser.current_url == live_server.url + "/accounts/signup/"
    ), "'Sign Up' page url should be [live server url]+'/accounts/signup/'."
    # Test 'Cancel' link
    try:
        link = browser.find_element(By.LINK_TEXT, "Cancel")
    except NoSuchElementException:
        assert False, "'Sign Up' page should include 'Cancel' link."
    link.click()
    assert (
        browser.title == "Site Name"
    ), "'Sign Up' page 'Cancel' link should take user to home page."
    browser.back()

    # Test Sign Up form.  Ignore validation as 'partially' covered by Django.  One blind spot is display of validation messages.
    USERNAME = "signup_test_user"
    PASSWORD1 = "my_password123"
    PASSWORD2 = "my_password123"
    EMAIL = "test_user@signup.com"
    username_field = browser.find_element(By.NAME, "username")
    password1_field = browser.find_element(By.NAME, "password1")
    password2_field = browser.find_element(By.NAME, "password2")
    email_field = browser.find_element(By.NAME, "email")
    username_field.send_keys(USERNAME)
    password1_field.send_keys(PASSWORD1)
    password2_field.send_keys(PASSWORD2)
    email_field.send_keys(EMAIL)
    try:
        submit_button = browser.find_element(By.XPATH, '//button[text()="Sign Up"]')
    except NoSuchElementException:
        assert False, "Sign Up page should have 'Sign Up' submit button."
    submit_button.click()
    assert (
        browser.title == "Log In"
    ), "Successful sign up should redirect to 'Log In' page"

    # Test new user can now log in
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD1)
    submit_button = browser.find_element(By.XPATH, '//button[text()="Log In"]')
    submit_button.click()
    assert (
        browser.title == "Site Name"
    ), "Page title incorrect.  Successful login should redirect to home page'."
    assert (
        "User" in browser.page_source
    ), "Page source incorrect.  Succesful login should redirect to home page with 'User:' displayed."


# Test Password Change
@pytest.mark.django_db
def test_password_change(
    authenticated_browser, live_server, test_user_username, test_user_password
):
    # Setup
    url = live_server.url + reverse("password_change")
    browser = authenticated_browser
    browser.get(url)
    # Test page title
    assert (
        browser.title == "Password Change"
    ), "Title of 'Password Change' page should be 'Password Change'."
    # # Test url
    assert (
        browser.current_url == live_server.url + "/accounts/password_change/"
    ), "'Password Change' page url should be [live server url]+'/accounts/password_change/'."
    # Test Password Change form.  Ignore validation as 'partially' covered by Django.  One blind spot is display of validation messages.
    OLD_PASSWORD = test_user_password
    NEW_PASSWORD1 = "my_new_password123"
    NEW_PASSWORD2 = "my_new_password123"
    old_password_field = browser.find_element(By.NAME, "old_password")
    new_password1_field = browser.find_element(By.NAME, "new_password1")
    new_password2_field = browser.find_element(By.NAME, "new_password2")
    old_password_field.send_keys(OLD_PASSWORD)
    new_password1_field.send_keys(NEW_PASSWORD1)
    new_password2_field.send_keys(NEW_PASSWORD2)
    try:
        submit_button = browser.find_element(
            By.XPATH, '//input[@value="Change my password"]'
        )
    except NoSuchElementException:
        assert (
            False
        ), "Password Change page should have 'Change my password' submit button."
    submit_button.click()
    assert (
        browser.title == "Password Change Successful"
    ), "Successful password change should redirect to 'Password Change Successful' page"
    assert (
        browser.current_url == live_server.url + "/accounts/password_change/done/"
    ), "Successful password change should redirect to [live server url]+'password_change/done/'"
    # Test user can now log in with change password
    browser.get(live_server.url + reverse("login"))
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    username_field.send_keys(test_user_username)
    password_field.send_keys(NEW_PASSWORD1)
    submit_button = browser.find_element(By.XPATH, '//button[text()="Log In"]')
    submit_button.click()
    assert (
        browser.title == "Site Name"
    ), "Page title incorrect.  Successful login should redirect to home page'."
    assert (
        "User" in browser.page_source
    ), "Page source incorrect.  Succesful login should redirect to home page with 'User:' displayed."


# Test Password Reset
@pytest.mark.django_db
def test_password_reset(browser, live_server, test_user):
    # Setup
    url = live_server.url + reverse("password_reset")
    browser.get(url)
    # Test 'Password Reset' page form
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys(test_user.email)
    submit_button = browser.find_element(
        By.XPATH, '//input[@value="Send me instructions!"]'
    )
    submit_button.click()
    assert (
        browser.title == "Email Sent"
    ), "'Password Reset' form should redirect to 'Email Sent' page."
    assert (
        browser.current_url == live_server.url + "/accounts/password_reset/done/"
    ), "'Password Reset' form should redirect to [live server url]+'/accounts/password_reset/done/'."
    # Test 'Password Reset' email
    # - Test that one message has been sent.
    assert (
        len(mail.outbox) == 1
    ), "'Password Reset' form submission with legit user email will send password reset email."
    email = mail.outbox[0]
    # - Test 'Password Reset' email subject
    assert (
        email.subject == "Password Reset"
    ), "'Password Reset' email subject should be 'Password Reset'."
    # - Get password reset link from email body, and test that it leads to the 'Password Reset' page.
    password_reset_url = re.findall("http://.+", email.body)[0]
    browser.get(password_reset_url)
    assert (
        browser.title == "Enter new password"
    ), "'Password Reset' link should direct to 'Enter new password' page."
    # - test password reset URL - IGNORE
    # Test 'Password Reset' form
    NEW_PASSWORD1 = "my_new_password123"
    NEW_PASSWORD2 = "my_new_password123"
    new_password1_field = browser.find_element(By.NAME, "new_password1")
    new_password2_field = browser.find_element(By.NAME, "new_password2")
    new_password1_field.send_keys(NEW_PASSWORD1)
    new_password2_field.send_keys(NEW_PASSWORD2)
    try:
        submit_button = browser.find_element(
            By.XPATH, '//input[@value="Change my password"]'
        )
    except NoSuchElementException:
        assert (
            False
        ), "Password Reset page should have 'Change my password' submit button."
    submit_button.click()
    assert (
        browser.title == "Password reset complete"
    ), "Successful password reset should redirect to 'Password reset complete' page"
    assert (
        browser.current_url == live_server.url + "/accounts/reset/done/"
    ), "Successful password reset should redirect to [live server url]+'reset/done/'"
    # Test click link to 'Log In page':
    try:
        link = browser.find_element(By.LINK_TEXT, "Log In page")
    except NoSuchElementException:
        assert False, "'Password reset complete' page should have 'Log In page' link."
    link.click()
    # Test user can now log in with new password
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    username_field.send_keys(test_user.username)
    password_field.send_keys(NEW_PASSWORD1)
    submit_button = browser.find_element(By.XPATH, '//button[text()="Log In"]')
    submit_button.click()
    assert (
        browser.title == "Site Name"
    ), "Page title incorrect.  Successful login should redirect to home page'."
    assert (
        "User" in browser.page_source
    ), "Page source incorrect.  Succesful login should redirect to home page with 'User:' displayed."


# SNIPPETS FOR DEVELOPMENT
# time.sleep(5)
