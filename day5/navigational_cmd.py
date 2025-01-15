import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.get("https://www.amazon.com")

driver.back()  #go back to first link opened

time.sleep(3)

driver.forward() # again to the second link

time.sleep(3)

driver.refresh()

time.sleep(3)


driver.quit()