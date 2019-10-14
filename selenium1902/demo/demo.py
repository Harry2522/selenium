from time import sleep
from selenium import webdriver

#浏览器操作
driver = webdriver.Chrome()
driver.maximize_window()  #窗口最大化

url = "http://www.baidu.com"
driver.get(url)
sleep(3)

# driver.find_element_by_id('kw').send_keys("华为")
# driver.find_element_by_name('wd').send_keys("淘宝")
driver.find_element_by_css_selector('#kw').send_keys("淘宝")
sleep(3)

# driver.find_element_by_id('su').click()
# driver.find_element_by_class_name('s_btn').click()
driver.find_element_by_css_selector('.s_btn').click()
sleep(3)


driver.find_element_by_link_text('淘宝网 - 淘!我喜欢').click()
# driver.find_element_by_partial_link_text('淘!我喜欢').click()



# sleep(2)                  #强制等待5s
# # driver.set_window_size(600, 400)
# driver.get("http://www.taobao.com")
# sleep(5)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)

# driver.quit()
