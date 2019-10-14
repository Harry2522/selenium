import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

driver.find_element(By.ID, 'kw').send_keys("华为")
driver.find_element(By.XPATH, '//input[@id="su"]').click()
time.sleep(2)

# driver.find_element(By.LINK_TEXT , '华为- 构建万物互联的智能世界').click()

hw = driver.find_element(By.LINK_TEXT, '华为- 构建万物互联的智能世界').get_attribute('href')
driver.get(hw)
time.sleep(3)

driver.find_element(By.LINK_TEXT,'华为商城').click()
time.sleep(3)


driver.quit()