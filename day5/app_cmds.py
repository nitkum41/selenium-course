from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

page_title=driver.title
print("page title is",page_title)

print("page url is",driver.current_url)

print("page source is",driver.page_source) #validations on the html


driver.close()

