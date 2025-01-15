from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")

driver.maximize_window()

#frames as a web element

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

time.sleep(2)

#parent frame
outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']") 

driver.switch_to.frame(outerframe)
time.sleep(2)

#child frame
innerframe = driver.find_element(By.XPATH,"//iframe[normalize-space()='<p>Your browser does not support iframes.</p>']") 
driver.switch_to.frame(innerframe)
time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("inside inner frame")
time.sleep(2)

driver.switch_to.parent_frame() ##switch to parent frame form child frame

driver.quit()