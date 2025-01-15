from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os,time


driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(5)
driver.maximize_window() 

#capture cookies from the browser
cookies = driver.get_cookies()

print("cookie count",len(cookies))

# ##print cookie details

# for cookie in cookies:
#     for key,value in cookie.items(): #read values of individual cookie
#         print(key,value)


##add new cookie to the browser

driver.add_cookie({"name":"mycookie","value":"123456"})

cookies= driver.get_cookies()
print("after adding",len(cookies))

##print cookie details

# for cookie in cookies:
#     for key,value in cookie.items(): #read values of individual cookie
#         print(key,value)

## delete specific cookie from browser

# driver.delete_cookie("mycookie") ## specify name of the cookie to delete

# cookies= driver.get_cookies()
# print("after deletion",len(cookies))

# ##print cookie details

# for cookie in cookies:
#     for key,value in cookie.items(): #read values of individual cookie
#         print(key,value)

#delete all the cookies 
driver.delete_all_cookies() ## all cookies 

cookies= driver.get_cookies()
print("after deletion of all cookies ",len(cookies))


