
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.get("https://filebin.net/")

driver.maximize_window()

path=os.path.join(os.getcwd(),r"day12\sample2.pdf")


driver.find_element(By.XPATH,"//input[@id='fileField']").send_keys(path)

time.sleep(4)
