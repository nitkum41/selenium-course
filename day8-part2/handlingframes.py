from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()

#switching frames by name 
# # tags can be frame , iframe , form  

driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("inside frame ")

driver.switch_to.default_content() ##go back to main page

driver.find_element(By.XPATH,"//a[normalize-space()='Home']").click()

# driver.switch_to.frame("name2")
# driver.find_element(By.XPATH,"//input[@name='mytext2']").send_keys("frame 2")
# driver.switch_to.default_content() ##go back to main page


# driver.switch_to.frame("name4")
# driver.find_element(By.XPATH,"//input[@name='mytext4']").send_keys("frame 4")
# driver.switch_to.default_content() ##go back to main page



