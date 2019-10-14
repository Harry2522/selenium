import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

driver.find_element(By.ID, 'kw').send_keys("华为")
driver.find_element(By.XPATH, '//input[@id="su"]').click()
time.sleep(2)
print("第一个窗口：",driver.title)
handles = driver.window_handles
print("所有窗口句柄11111：",handles)

#进入华为官网
driver.find_element(By.LINK_TEXT, '华为- 构建万物互联的智能世界').click()
time.sleep(3)

#切换窗口
current = driver.current_window_handle
print("当前窗口句柄：", current)

handles = driver.window_handles
driver.switch_to.window(handles[-1])
print("第二个窗口：", driver.title)

#进入华为商城
driver.find_element(By.LINK_TEXT,'华为商城').click()
time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
print("第三个窗口：",driver.title)


driver.quit()