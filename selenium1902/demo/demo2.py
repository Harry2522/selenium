import time
from selenium import  webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://192.168.1.241/hdshop/user.php')
driver.find_element_by_css_selector(".searchKey").send_keys("小熊")
time.sleep(2)
driver.find_element_by_css_selector('input[value="搜 索"]').click()

time.sleep(3)
driver.quit()


