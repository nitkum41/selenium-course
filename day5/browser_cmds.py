import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()



driver.find_element(By.XPATH,"//a[contains(text(),'nopCommerce')]").click()

time.sleep(10)

# driver.close()
driver.quit()


time.sleep(10)
