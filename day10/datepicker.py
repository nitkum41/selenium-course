from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0) ## switch to frame sunce one frame index is working

##using input 
# driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2024")
# time.sleep(4)

## use date picker
date="23"
month="November"
year="2021"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

##select month and year

while True:
    actualmonth = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    actualyear = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if month==actualmonth and year==actualyear:
        break
    else:
        if int(actualyear)< int(year):
            driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #click right arrow #future
        else:
            driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() #click left arrow #past


## select date

##inside a table 
listofdates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dte in listofdates:
    if dte.text==date:
        dte.click()
        break


time.sleep(4)

