from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

## opens alert window
driver.find_element(By.XPATH , "//button[normalize-space()='Click for JS Prompt']").click() #normalize space can havespace bwtween the texts

time.sleep(5)

alertwindow = driver.switch_to.alert  ##object representing the whole alert window

print(alertwindow.text) 

alertwindow.send_keys("hello world") #input on alert window

time.sleep(4)

alertwindow.accept()  #close using ok button

# alertwindow.dismiss() #cancel window




