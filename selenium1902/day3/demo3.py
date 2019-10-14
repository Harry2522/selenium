from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

#进入后台
driver.get("http://192.168.1.241/hdshop/admin/")
driver.find_element_by_name("username").send_keys("admin") #输入用户名
driver.find_element_by_name("password").send_keys("hdxy2018") #输入密码
driver.find_element_by_id("remember").click() #保存登录信息
driver.find_element_by_class_name("btn-a").click() #点击登录
sleep(2)

#进入上方导航
driver.switch_to.frame("header-frame") #切换frame进入上方导航栏
driver.find_element(By.XPATH,'//div[@id="menu-div"]/ul/li[5]/a/span[1]').click() #点击订单管理
driver.switch_to.default_content() #退出导航栏frame
sleep(3)

#进入右侧内容
driver.switch_to.frame("main-frame") #切换frame进入右侧内容
status = driver.find_element(By.ID,'status') #定位订单状态下拉框
wfh = Select(status)
wfh.select_by_value("101") #赋值订单状态为未发货
driver.find_element(By.XPATH,'/html/body/div[1]/form/input[3]').click() #点击搜索
sleep(2)
driver.find_element(By.LINK_TEXT,'查看').click() #点击第一个订单查看
sleep(2)
driver.find_element(By.NAME,'prepare').click() #点击配货
sleep(3)
driver.find_element(By.NAME,'ship').click() #点击生成发货单
sleep(1)
driver.find_element(By.NAME,'delivery_confirmed').click() #点击确认生成发货单
sleep(3)
driver.find_element(By.NAME,'to_delivery').click() #去发货
sleep(1)
driver.find_element(By.LINK_TEXT,'查看').click() #点击查看
sleep(1)
# driver.find_element(By.NAME,'delivery_confirmed').click() #发货
driver.find_element(By.XPATH, '/html/body/div[3]/table/tbody/tr[4]/td[2]/input[1]').click()
sleep(5)
a = driver.find_element(By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]').text
print(a)
sleep(2)
driver.quit()