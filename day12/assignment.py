from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(3)
driver.maximize_window()

# WebDriverWait(driver, timeout=5).until(title_is,"OrangeHRM")

driver.find_element(by=By.NAME,value="username").send_keys("Admin")
driver.find_element(by=By.NAME,value="password").send_keys("admin123")
driver.find_element(by=By.CSS_SELECTOR,value="button").click()

time.sleep(2)


driver.find_element(By.XPATH,"//ul[@class='oxd-main-menu']//li[2]").click()

time.sleep(4)

driver.find_element(By.XPATH,"//div[@class='oxd-topbar-body']//li[3]").click()

time.sleep(4)

path=os.path.join(os.getcwd(),r"day12\mage.jpg")

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button").send_keys(path)

time.sleep(4)