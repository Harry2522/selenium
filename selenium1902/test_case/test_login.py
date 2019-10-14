import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By




class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://192.168.1.241/hdshop/admin/")
        self.driver.find_element(By.NAME,'username').send_keys("超超")
        self.driver.find_element(By.NAME,'password').send_keys("123456")
        self.driver.find_element(By.CLASS_NAME,'us_Submit').click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()

