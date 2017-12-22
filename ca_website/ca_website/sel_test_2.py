"""Selenium browser tests."""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from django.test import TestCase
import pdb


# driver = webdriver.Firefox()
# driver.set_window_size('1024', '768')
# driver.get('https://www.google.com/')
# driver.quit()

class sel_test1(TestCase):
    """."""

    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    pdb.set_trace()
