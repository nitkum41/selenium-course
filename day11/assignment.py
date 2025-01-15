from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(3)
driver.maximize_window()

#rightclick----------------------------##################################################

# driver.find_element(By.XPATH,"//input[@id='field1']").clear()

# driver.find_element(By.XPATH,"//input[@id='field1']").send_keys("check right click")

# buttonelement = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")


# act=ActionChains(driver)

# act.double_click(buttonelement).perform()

# print(driver.find_element(By.XPATH,"//input[@id='field2']").text)

# time.sleep(5)

##drag and drop ------------------------------------############################################

# source_element = driver.find_element(By.XPATH,"//div[@id='draggable']")

# target_element = driver.find_element(By.XPATH,"//div[@id='droppable']")

# act = ActionChains(driver)

# act.drag_and_drop(source_element,target_element).perform()

# time.sleep(3)

##slider-----------------------##################################

slider = driver.find_element(By.XPATH,"//*[@id='slider']/span")

print("initial location",slider.location)

act = ActionChains(driver)

act.drag_and_drop_by_offset(slider,100,0).perform()
print("initial location",slider.location)

time.sleep(2)

act.drag_and_drop_by_offset(slider,-10,0).perform()
print("initial location",slider.location)

time.sleep(2)