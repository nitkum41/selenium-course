import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com")

driver.maximize_window()


###locator matching single web element   ##find_element()

# element= driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("cricket")

###locator matching multiple web elements
 
# element= driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)  ##although pointing to multiple web elements it returns the first one

###locator not on web page
 
# element= driver.find_element(By.XPATH,"//div[@class='footer']//tr")
# print(element.text)  ##although pointing to multiple web elements it returns the first one




#################---------------########################




###locator matching single web element   ##find_elements()

# elements= driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))
# elements[0].send_keys("cricket") ## error as it always retirns a list collection

###locator matching multiple web elements
 
# elements= driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))  ##returns list of all links
# for element in elements:
#     print(element.text)



###locator not on web page
 
elements= driver.find_elements(By.XPATH,"//div[@class='footer']//tr")
print(len(elements))  ##although pointing to multiple web elements it returns the first one