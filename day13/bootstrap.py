from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.implicitly_wait(5)
driver.maximize_window()

## if select class not avaialibale 

driver.find_element(By.XPATH,"span//[@id='select2-billing_country-container']").click()

countries = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

for country in countries:
    if country.text=="India":
        country.click()