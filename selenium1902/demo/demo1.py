# 登录ecshop网址——点击登录——输入账户——输入密码——点击立即登录
# ——点击钻石——点击小熊手表表链——点击立即购买——刷新当前界面
# ——返回上一个界面——在搜索框输入悟空——点击悟空——点击立即购买
# ——返回上一个界面——关闭当前界面

from time import sleep   #从time中导入sleep资源
from selenium import webdriver  #从selenium中导出webdriver资源

driver = webdriver.Chrome()    #启动谷歌浏览器
driver.maximize_window()                                 #窗口最大化


#以下是浏览器操作
driver.get("http://192.168.1.241/hdshop")                #跳转到ecshop前台页面
sleep(3)                                                 #等待3秒
driver.find_element_by_link_text("登录").click()         #点击右上键的登录并跳转
driver.find_element_by_name("username").send_keys("zhangmengqiang")            #找到用户名输入框,并输入用户名
driver.find_element_by_name("password").send_keys("123456")       #输入密码123456
driver.find_element_by_name("submit").click()                      #点击立即登录
sleep(1)

driver.find_element_by_link_text("钻石").click()         #点击钻石
sleep(2)                                                 #等待2秒
driver.find_element_by_link_text("小熊手表表链").click()  #点击小熊手表表链这个图片
sleep(2)                                                  #等待2秒
driver.find_element_by_css_selector("img[src*='themes/ecmoban_meilishuo/images/goumai2.gif']").click()   #点击立即购买
driver.refresh()                                         #刷新当前界面

sleep(3)                                                  #等待3秒
driver.back()                                             #推到上一个界面
driver.find_element_by_id("keyword").send_keys("悟空")    #在搜索输入框输入悟空
driver.find_element_by_name("imageField").click()         #点击搜索按钮
driver.find_element_by_link_text("悟空").click()          #点击悟空跳转界面
driver.find_element_by_css_selector("[src*='themes/ecmoban_meilishuo/images/goumai2.gif']").click()   #点击立即购买

sleep(3)                                                  #等待3秒
driver.back()                                             #推到上一个界面
sleep(3)                                                  #等待3秒
driver.close()                                            #关闭当前界面
