from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://mypage.rediff.com/login/dologin")

driver.maximize_window()

## opens alert window
driver.find_element(By.XPATH , "//input[@value='Login']").click() #normalize space can havespace bwtween the texts

time.sleep(5)

alertwindow = driver.switch_to.alert.accept() ##object representing the whole alert window

time.sleep(4)

driver.close()




