import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.jd.com/')

#显式等待
wait = WebDriverWait(driver, 10, 1)
wait.until(EC.presence_of_element_located((By.ID,'key')))

driver.find_element(By.ID , 'key').send_keys("华为")
driver.find_element(By.ID , 'key').send_keys(Keys.ENTER)



time.sleep(3)
driver.quit()