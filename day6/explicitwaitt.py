from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.common.exceptions import NoSuchElementException , ElementNotVisibleException,ElementNotSelectableException
# import time

driver = webdriver.Chrome()

# mywait = WebDriverWait(driver,10)  ## explicit wait declaration #basic syntax


mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException , 
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     Exception])


driver.get("https://www.google.com")

driver.maximize_window()

search_box = driver.find_element(by=By.NAME,value="q")
search_box.send_keys("selenium")

search_box.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))

searchlink.click()

driver.quit()

