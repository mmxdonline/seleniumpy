from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/admin/Desktop/Selenium/chromedriver')
        self.driver.get('https://google.com')

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
        input_field.send_keys('Hello')
        input_field.send_keys(Keys.ENTER)





