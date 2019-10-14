from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
sleep(2)
driver.find_element_by_name("wd").send_keys("haha")
driver.find_element_by_class_name("s_btn").click()
sleep(2)
driver.find_element_by_link_text("Haha_百度翻译").click()
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
sleep(3)

driver.find_element_by_class_name("correct-txt").click()

msg = driver.find_element_by_class_name("correct-txt").text
print(msg)
sleep(8)
# driver.find_element_by_xpath('//*[@id="main-outer"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/a[1]/span/label').click()
# driver.find_element_by_css_selector(".correct-txt").click()
# driver.find_element_by_id('kw').send_keys("huawei")
# driver.find_element_by_id("su").click()

# driver.back()
# sleep(2)
# driver.forward()
# sleep(3)  #双击显示灯可以导入变量
driver.quit()

