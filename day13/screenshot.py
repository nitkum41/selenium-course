from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os,time


driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

driver.implicitly_wait(5)
driver.maximize_window() #maximiz the window before the screenshot


##absolute path 
# driver.save_screenshot("C:\\Personal\\Nitesh-HP-Data\\Nitesh-HP\\SeleniumProject\\SeleniumProject\\day13\\file.png")

#save scrrenshot ## path with file name

cwd = os.getcwd()

file_path = os.path.join(cwd,"day13\\file2.png") ## don't use \\ slash in the filepath string
print(file_path)

##relative path
# driver.save_screenshot(file_path)
driver.get_screenshot_as_file(file_path)



## in binary form then decoded

driver.get_screenshot_as_base64()
driver.get_screenshot_as_png()