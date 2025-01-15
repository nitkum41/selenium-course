from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("https://www.awwwards.com/websites/scrolling/")
driver.implicitly_wait(3)
driver.maximize_window()


#1. using JS script 

# driver.execute_script("window.scrollBy(0,3000)","")  #scroll 3000 pixels using JS function
# time.sleep(2)
# value = driver.execute_script("return window.pageYOffset;")

# print("Number of pixels moved",value)

# time.sleep(5)

#2. scroll down the page till the element is visible 

# targetelement=driver.find_element(By.XPATH,"//img[@alt='Atlas']")
# driver.execute_script("arguments[0].scrollIntoView();",targetelement)

# time.sleep(4)

# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved",value)

#3 scroll til the end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(4)

value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved",value) #4311.33349609375 total pixel moved

#4 scroll to the start of the page

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")

time.sleep(4)

value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved",value) #0 becomes zero when it is back