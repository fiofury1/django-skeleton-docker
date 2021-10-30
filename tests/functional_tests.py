# Replace this file with project wide functional/integration tests

# Test Selenium setup
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/home/fiofury1/drivers/chromedriver/chromedriver') #If project is cloned, replace with local location. 
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
driver.quit()