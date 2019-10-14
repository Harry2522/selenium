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
driver.find_element(By.LINK_TEXT ,'添加新商品').click()
sleep(3)
driver.switch_to.default_content()

#商品添加
driver.switch_to.frame("main-frame")

#页面向下滚动
# driver.execute_script("window.scroll(0,10000)")

#执行js脚本删除促销日期的readonly 属性，便于直接输入时间
js = "window.scroll(0,10000);document.getElementById('promote_start_date').removeAttribute('readonly')"
driver.execute_script(js)
sleep(3)
driver.find_element(By.ID,'promote_start_date').clear()
sleep(2)
driver.find_element(By.ID,'promote_start_date').send_keys('2019-11-11')
#结束日期
end_js="document.getElementById('promote_end_date').removeAttribute('readonly');" \
       "document.getElementById('promote_end_date').value='2019-12-31'"
driver.execute_script(end_js)

#上传文件
driver.find_element(By.NAME, 'goods_img').send_keys("D:/img/1.jpg")
sleep(2)

driver.switch_to.default_content()


#关闭退出浏览器
sleep(5)
driver.quit()