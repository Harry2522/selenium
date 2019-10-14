import time
from selenium import  webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://192.168.1.241/hdshop/user.php')
driver.find_element_by_xpath('//input[@name="keywords"]').send_keys("小熊")
time.sleep(2)
driver.find_element_by_xpath('//input[@value="搜 索"]').click()
time.sleep(2)

#清空输入框
driver.find_element_by_xpath('//input[@name="keywords"]').clear()
time.sleep(3)
#重新搜索
driver.find_element_by_xpath('//input[@class="searchKey" and @id="keyword"]').send_keys("悟空")
driver.find_element_by_xpath('//input[@type="submit1" or @value="搜 索"]').click()
time.sleep(3)
#获取元素属性
price = driver.find_element_by_xpath('//form[@id="compareForm"]/div/div/font').text
title = driver.find_element_by_xpath('//form[@id="compareForm"]/div/div/p/a').text
print("%s  商品的价格为 %s" % (title, price))

val = driver.find_element_by_xpath('//form[@id="searchForm"]/span[2]/input').get_attribute('value')
print("input 按钮的值为 %s " % val)

url = driver.current_url

print("当前URL %s" % url )


# 再次搜索
driver.find_element_by_xpath('//input[contains(@class, "searchKey")]').send_keys("八戒")
driver.find_element_by_xpath('//input[contains(@type ,"submit")]').click()

driver.find_element_by_xpath('//input[@id="keyword"]').send_keys("唐神")

driver.get(url)

time.sleep(3)
driver.quit()


