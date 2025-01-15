from selenium import webdriver
from selenium.webdriver.common.by import By

# import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)  #applicable for all driver elements defined after this statement so at start # value in seconds

driver.get("https://www.google.com")

driver.maximize_window()

search_box = driver.find_element(by=By.NAME,value="q")
search_box.send_keys("selenium")

search_box.submit()

# time.sleep(5) #wherever we observe delay

driver.find_element(by=By.XPATH,value="//h3[text()='Selenium']").click()
