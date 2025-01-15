from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

##count total no of rows and column in the table

totalrows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print("total rows",len(totalrows))

totalcolumns = driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print("total columns",len(totalcolumns))

##read specific row and column data

# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]//td[1]") ##5th rowm 1st column ##pass them as indexes
# print(data.text)

## read all data 

# for row in range(2,len(totalrows)+1):
#     for column in range(1,len(totalcolumns)+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]//td["+str(column)+"]")
#         print(data.text,end='|')

#     print("\n")

#### read data based on condition---- ##list book author is mukesh

for r in range(2,len(totalrows)+1):
        author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[2]")
        if author.text=="Mukesh":
                print("book name :",driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[1]").text)
                print("price :",driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[4]").text)




