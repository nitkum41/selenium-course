from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(3)
driver.maximize_window()

rightclickbutton=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver) #pass driver to actionchains class

act.context_click(rightclickbutton).perform() ## for right click

time.sleep(6)