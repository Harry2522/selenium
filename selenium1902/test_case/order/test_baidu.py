import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class BaiduTestCase(unittest.TestCase):
    # def __init__(self):
    #     self.name = "harry"

    def setUp(self):
        print("初始化，准备执行")
        self.name = "harry"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        print("清理，用例执行完成")
        self.driver.quit()

    def test_taobao(self):
        print(self.name)
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, 'kw').send_keys("淘宝")
        self.driver.find_element(By.ID, 'su').click()
        print("淘宝")

    def test_jd(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID,'kw').send_keys("京东")
        self.driver.find_element(By.ID,'su').click()
        print("京东")

    def test_baidu(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID,'kw').send_keys("百度")
        self.driver.find_element(By.ID,'su').click()
        print("百度")

    def test_login(self):

        self.driver.get("http://192.168.1.241/hdshop/user.php")
        self.driver.find_element(By.NAME,'username').send_keys("超超")
        self.driver.find_element(By.NAME,'password').send_keys("123456")
        self.driver.find_element(By.CLASS_NAME,'us_Submit').click()
        time.sleep(3)

        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

    # suit = unittest.TestSuite()
    # suit.addTest(BaiduTestCase("test_baidu"))
    # suit.addTest(BaiduTestCase("test_jd"))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)