from time import sleep
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://192.168.1.241/hdshop/admin/privilege.php?act=login')

#登录后台
driver.get("http://192.168.1.241/hdshop/admin/")
driver.find_element_by_name("username").send_keys("admin") #输入用户名
driver.find_element_by_name("password").send_keys("hdxy2018") #输入密码
driver.find_element_by_id("remember").click() #保存登录信息
driver.find_element_by_class_name("btn-a").click() #点击登录
sleep(2)

#商品管理-商品列表菜单
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH, '//ul[@id="menu-ul"]/li[1]').click()
driver.find_element(By.LINK_TEXT ,'商品列表').click()
sleep(3)
driver.switch_to.default_content()

#商品删除
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[12]/a[4]/img').click()
sleep(3)
driver.switch_to.alert.dismiss() #点击【取消】关闭弹框
sleep(3)

driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[12]/a[4]/img').click()
sleep(3)
driver.switch_to.alert.accept()#点击【确定】关闭弹框
driver.switch_to.default_content()

#关闭退出浏览器
sleep(5)
driver.quit()