import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.jd.com/")
driver.implicitly_wait(30) #隐式等待

#鼠标悬浮
locator = driver.find_element(By.LINK_TEXT, '家用电器')
ac = ActionChains(driver)
ac.move_to_element(locator).perform()
driver.find_element(By.LINK_TEXT, '4K超清电视').click()

#窗口切换
handles = driver.window_handles
driver.switch_to.window(handles[-1])

#搜索商品
driver.find_element(By.ID,'key').send_keys("华为手机")
driver.find_element(By.ID,'key').send_keys(Keys.ENTER)
time.sleep(3)
driver.execute_script("window.scroll(0,1000)")
#获取第一个产品的标题
title = driver.find_element(By.XPATH,'//div[@id="J_goodsList"]/ul/li[1]/div/div[4]/a').text
print("第一个产品的标题为：%s " % title)

#保存截图
driver.save_screenshot("D:/img/jd.png")

time.sleep(5)
driver.quit()