from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import NoSuchElementException , ElementNotVisibleException,ElementNotSelectableException

from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

# dropdownelement = driver.find_element(By.XPATH,"//select[@id='country']")

# dropdownobject = Select(driver.find_element(By.XPATH,"//select[@id='country']"))

#total options
# print("total options",len(dropdownobject.options))

# for option in dropdownobject.options:
#     print("value of options",option.text)

#by option
# time.sleep(2)
# dropdownobject.select_by_visible_text("United Kingdom")
# time.sleep(2)


#by value
# time.sleep(5) 
# dropdownobject.select_by_value("usa")
# time.sleep(5)

#by index
# time.sleep(5) 
# dropdownobject.select_by_index(2) #index starts from 0
# time.sleep(5)

#without select get all options

dropdownoptions = driver.find_elements(By.XPATH,"//*[@id='country']/option")

print("total options",len(dropdownoptions))

for option in dropdownoptions:
    print(option.text)




driver.quit()
