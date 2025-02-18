

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.co.in/")


driver.find_element(By.ID,"APjFqb").send_keys("Python")

driver.close()