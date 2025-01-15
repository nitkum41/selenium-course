from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## imprt requests module

import requests as requests


driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

totallinks = driver.find_elements(By.TAG_NAME,"a")
count=0

for link in totallinks:
    url= link.get_attribute('href')

    try:
        res=requests.head(url) #hit url in backend #gives server errors so use try except block 
    except:
        None
        print("error")

    if res.status_code >= 400:
        print(url , "is broken link")
        count+=1
    else:
        print(url , "is valid link")


print("total broken links: ",count)

