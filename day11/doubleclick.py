from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.implicitly_wait(3)
driver.maximize_window()

driver.switch_to.frame("iframeResult") #switch to frame using frame name

button = driver.find_element(By.XPATH,"//button[normalize-space()='Double-click me']")

act = ActionChains(driver)
act.double_click(button).perform()  ##double click action

print(driver.find_element(By.XPATH,"//p[@id='demo']").text)

time.sleep(2)