from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time


driver = webdriver.Chrome()

driver.get("https://practice.expandtesting.com/hovers")
driver.implicitly_wait(3)
driver.maximize_window()


figurelist=driver.find_elements(By.XPATH,"//div[@class='figure']")

for i in range(1,len(figurelist)+1):
    element = driver.find_element(By.XPATH,"//div[@class='figure']["+str(i)+"]//img")


    #mouse hover actions

    actchain = ActionChains(driver) ##pass driver instance to class

    actchain.move_to_element(element).perform()
    time.sleep(2)
    link = driver.find_element(By.XPATH,"//div[@class='figure']["+str(i)+"]//div[@class='figcaption']/a")
    print(link.text)
    actchain.move_to_element(link).click().perform()
    time.sleep(2)
    break
    #perform to execute  action
