from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#1 select one checkbox

# driver.find_element(By.XPATH,"//input[@id='checkBoxOption1']").click()

#2 select all checkboxes ## type and id combination
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkBoxOption')]")

# print("length",len(checkboxes))

# for checkbox in checkboxes:
#     checkbox.click()
#     time.sleep(1)

#3 select multiple checkboxes by choice
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkBoxOption')]")

# print("length",len(checkboxes))

# for checkbox in checkboxes:
#     box=checkbox.get_attribute('id')
#     if box == "checkBoxOption1" or box == "checkBoxOption3":
#          checkbox.click()
#          time.sleep(1)

#4 select last two checkboxes
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkBoxOption')]")

# print("length",len(checkboxes))

# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
#     time.sleep(1)

#5 clear all the selected checkboxes

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkBoxOption')]")

print("length",len(checkboxes))

for checkbox in checkboxes:
        checkbox.click()
        time.sleep(1)

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
        time.sleep(1)
    
    


driver.quit()


