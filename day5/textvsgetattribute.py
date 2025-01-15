import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

driver.maximize_window()

# emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")

# emailbox.clear()
# emailbox.send_keys("abc@gmail.com")


# print("text of email: ",emailbox.text) ### returns inner text of the element

# print("get_attribute of  email: ",emailbox.get_attribute('value')) #returns value of any attribute present in the element

# print("get_attribute of  type: ",emailbox.get_attribute('type'))

# print("get_attribute of  id: ",emailbox.get_attribute('id'))




#############----------------------------#####################


loginbutton=driver.find_element(By.XPATH,"//button[@type='submit']")



print("text of loginbutton: ",loginbutton.text) ### returns inner text of the element

print("get_attribute of  class: ",loginbutton.get_attribute('class')) #returns value of any attribute present in the element

print("get_attribute of  type: ",loginbutton.get_attribute('type'))

print("get_attribute of  value: ",loginbutton.get_attribute('value')) # no value since this attribute is not present in web element so empty






