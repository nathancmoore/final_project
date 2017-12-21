"""Selenium browser tests."""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


# driver = webdriver.Firefox()
# driver.set_window_size('1024', '768')
# driver.get('https://www.google.com/')
# driver.quit()

class SandwichTest(unittest.TestCase):
    """."""

    def setUp(self):
        """."""
        self.driver = webdriver.Firefox()
        self.driver.get('http://ec2-34-216-126-115.us-west-2.compute.amazonaws.com/')
        self.sandwich_locator = '/span/button[1]'
