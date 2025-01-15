from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#dob element
driver.find_element(By.XPATH,"//input[@id='dob']").click() #opens date picker

#use select class for dropdowns for month

monthelement = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
monthelement.select_by_visible_text("Oct")

#use select class for dropdowns for year

yearelement = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
yearelement.select_by_visible_text("1991")

#get all dates from table 
alldates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text == "20":
        date.click()
        break







