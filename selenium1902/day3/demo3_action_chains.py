import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.jd.com/")
driver.implicitly_wait(30) #隐式等待

#鼠标悬浮
locator = driver.find_element(By.LINK_TEXT, '家用电器')
ac = ActionChains(driver)
ac.move_to_element(locator).perform()
driver.find_element(By.LINK_TEXT,'4K超清电视').click()

time.sleep(5)
driver.quit()