from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.implicitly_wait(3)
driver.maximize_window()

minm_slider_elt = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
maxm_slider_elt = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Before Moving-------------------")

print(minm_slider_elt.location) #location attribute to get location of any web element {'x': 59, 'y': 250}
print(maxm_slider_elt.location) #location attribute to get location of any web element {'x': 510, 'y': 250}


act = ActionChains(driver)

act.drag_and_drop_by_offset(minm_slider_elt,159,0).perform()
act.drag_and_drop_by_offset(maxm_slider_elt,-159,0).perform()


print("After Moving-------------------")
print(minm_slider_elt.location) #{'x': 217, 'y': 250}
print(maxm_slider_elt.location) #{'x': 352, 'y': 250}

time.sleep(4)