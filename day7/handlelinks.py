from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

## 1 click on links

# time.sleep(3)

# # driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"downloads").click()

# time.sleep(3)



## 2 find number of links on the page

# links = driver.find_elements(By.TAG_NAME,'a')

# links = driver.find_elements(By.XPATH,'//a')




##3 print all link text

# for link in links:
#     print(link.text)


# print("total links",len(links))








driver.quit()