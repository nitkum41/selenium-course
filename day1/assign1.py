"""
https://admin-demo.nopcommerce.com/login

admin@yourstore.com

admin

Dashboard / nopCommerce administration is the title

"""



import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service =Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://admin-demo.nopcommerce.com/login")
# driver.implicitly_wait(3)

driver.find_element(by=By.NAME,value="Email").clear()
driver.find_element(by=By.NAME,value="Email").send_keys("admin@yourstore.com")

driver.find_element(by=By.ID,value="Password").clear()
driver.find_element(by=By.ID,value="Password").send_keys("admin")

driver.find_element(by=By.CSS_SELECTOR,value="button").click()


actual_title = driver.title

expected_title = "Dashboard / nopCommerce administration"

if actual_title == expected_title:
    print("Login test passed")
else:
    print("Login test failed")

# driver.close()