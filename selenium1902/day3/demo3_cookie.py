import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.1.241/hdshop/admin/index.php")

#加入cookie
driver.add_cookie({"name":"ECSCP[admin_id]", "value":"1"})
driver.add_cookie({"name":"ECSCP[admin_pass]","value":"fba1e86908f364f5fee205d14dc69ff7"})
driver.add_cookie({"name":"ECS_LastCheckOrder","value":"Thu%2C%2023%20May%202019%2009%3A04%3A49%20GMT"})
time.sleep(5)

#刷新页面
# driver.refresh()
driver.get("http://192.168.1.241/hdshop/admin/index.php")


time.sleep(5)
driver.quit()
