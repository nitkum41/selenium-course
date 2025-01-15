from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.implicitly_wait(3)
driver.maximize_window()

act = ActionChains(driver)

for i in range(3,8):

    capital_source=driver.find_element(By.ID,"box"+str(i))

    country_destination=driver.find_element(By.ID,"box10"+str(i))

   

    act.drag_and_drop(capital_source,country_destination).perform()  ##perform drag and drop mouse action

time.sleep(4)