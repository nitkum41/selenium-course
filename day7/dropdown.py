from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import NoSuchElementException , ElementNotVisibleException,ElementNotSelectableException

from selenium.webdriver.support.select import Select
import time



driver = webdriver.Chrome()
mywait = WebDriverWait(driver,60,poll_frequency=2,ignored_exceptions=[NoSuchElementException , 
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception])

driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(20)
countryElement = driver.find_element(By.NAME,"country_id")

#get web element having the dropdowns
# countryElementuto = mywait.until(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#pass the web element to select class to convert in to dropdown object
dropdownObject = Select(countryElement)

#1.read case sensitive values

dropdownObject.select_by_visible_text("India")
time.sleep(2)

# #2.read case sensitive values

# dropdownObject.select_by_value("10") #Argentina #value attribute from html
# time.sleep(2)

# #3.read case sensitive values

# dropdownObject.select_by_index(13) #count manually from html
# time.sleep(2)

##4. select all options in the dropdown
totalOptions= dropdownObject.options
print("total options",totalOptions )

for option in totalOptions:
    print(option.text)


##5  select option value without using built in function

for option in totalOptions:
    if option.text=="India":
        option.click()
        break


##6 if select tag is not present then use XPath to get all options 

totalOptions = driver.find_elements(By.XPATH,"//*[@id='input-country']/option")
print("total options",totalOptions )


driver.maximize_window()

driver.quit()