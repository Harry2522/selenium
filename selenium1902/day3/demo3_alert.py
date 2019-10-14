import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)

driver.maximize_window()

#alert弹框处理
driver.get('http://192.168.1.241/hdshop/')
driver.find_element(By.LINK_TEXT,'收藏本站').click() #弹框
time.sleep(5)
info = driver.switch_to.alert.text #获取弹框文本
print(info)
driver.switch_to.alert.accept() #关闭alert弹框

time.sleep(3)
driver.quit()