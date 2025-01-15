from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os,time


driver=webdriver.Chrome()

driver.get("https://www.selenium.dev/")

driver.implicitly_wait(5)
driver.maximize_window() 

# ##opens the link on the same window
# # driver.find_element(By.XPATH,"//span[normalize-space()='Documentation']").click() 

# ##opens the link in new tab ## keys combination
# doclink = Keys.CONTROL+Keys.ENTER
# driver.find_element(By.LINK_TEXT,"Documentation").send_keys(doclink)


##selenium 4 switches to new tab and opens url in new tab 

# driver.get("https://www.selenium.dev/")

# driver.switch_to.new_window("tab")

# driver.get("https://www.pythonanywhere.com/")


##selenium 4 switches to new window and opens url in new window

driver.get("https://www.selenium.dev/")

driver.switch_to.new_window("window")

driver.get("https://www.pythonanywhere.com/")

time.sleep(2)