from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()


# windowid=driver.current_window_handle #window id of single browser window
# print("window id:", windowid)

time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

windowids = driver.window_handles #get all window ids

##Method 1
# print("allwindow ids",len(windowids))
# parentwindowid=windowids[0]
# childwindowid=windowids[1]

# driver.switch_to.window(childwindowid) #switch to wondow id
# print("window titel",driver.title) #get title
# time.sleep(2)

# driver.switch_to.window(parentwindowid)
# print("window titel",driver.title)
# time.sleep(2)

# driver.close()

##method 2

for window in windowids:
    driver.switch_to.window(window)
    if driver.title=="OrangeHRM":
        driver.close() #closes down one browser

