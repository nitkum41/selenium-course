
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os,time


def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument('--headless') ##add argument for headless mode
    driver = webdriver.Chrome(options=ops)
    return driver

def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument('--headless') ##add argument for headless mode
    driver = webdriver.Edge(options=ops)
    return driver

def headless_firefox():
    ops = webdriver.FirefoxOptions()
    ops.add_argument('--headless') ##add argument for headless mode
    driver = webdriver.Firefox(options=ops)
    return driver



# driver = headless_chrome()

# driver = headless_edge()

driver= headless_firefox()

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.current_url)
print(driver.title)

driver.close()