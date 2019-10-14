import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.1.241/hdshop/admin/index.php')

#后台登录
driver.find_element(By.NAME, 'username').send_keys('admin')
driver.find_element(By.NAME, 'password').send_keys('hdxy2018')
driver.find_element(By.CLASS_NAME, 'btn-a').click()
time.sleep(2)

#进入左侧导航
driver.switch_to.frame('menu-frame')  #切换frame，并进入导航菜单
driver.find_element(By.XPATH,'//ul[@id="menu-ul"]/li[1]').click() #点击【商品管理】
time.sleep(3)
driver.find_element(By.LINK_TEXT, '添加新商品').click()
time.sleep(2)
driver.switch_to.default_content()  #退出导航菜单frame
time.sleep(3)

#进入右侧内容
driver.switch_to.frame('main-frame')
driver.find_element(By.NAME, 'goods_name').send_keys("小茗同学")
#select 下拉框
el = driver.find_element(By.NAME, 'cat_id')
sele = Select(el)
sele.select_by_value("182")
driver.find_element(By.NAME, 'shop_price').clear()
driver.find_element(By.NAME, 'shop_price').send_keys("100")

time.sleep(2)
driver.find_element(By.XPATH ,'//div[@id="tabbody-div"]/form/div/input[2]').click()
driver.switch_to.default_content()
time.sleep(5)

driver.quit()