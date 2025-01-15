from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

#bypass authentication pop up

driver.get("https:admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()








