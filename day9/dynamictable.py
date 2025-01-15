from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(3)
driver.maximize_window()

##login

driver.find_element(by=By.NAME,value="username").send_keys("Admin")
driver.find_element(by=By.NAME,value="password").send_keys("admin123")
driver.find_element(by=By.CSS_SELECTOR,value="button").click()
time.sleep(3)

##click on hamburger icon

# driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-list oxd-topbar-header-hamburger']").click()
# time.sleep(2)

#click on admin tab

driver.find_element(By.XPATH,"//a//span[normalize-space()='Admin']").click()
time.sleep(2)

# #find user management tab

driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
time.sleep(2)

# #find users tab 

driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()
time.sleep(2)

##pending users whose status is disbaled 

totalrows=driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']//div[@class='oxd-table-card']")
print("total rows",len(totalrows))

totalcolumns = driver.find_elements(By.XPATH,"//div[@class='oxd-table-header']//div[@role='columnheader']")
print("total columns",len(totalcolumns))

for r in range(1,len(totalrows)+1):
    rowlistdata=[]
    headerlist=[]
    for c in range(2,len(totalcolumns)):
        headerdata = driver.find_element(By.XPATH,"//div[@class='oxd-table-header']//div[@role='columnheader']["+str(c)+"]").text
        data = driver.find_element(By.XPATH,"//div[@class='oxd-table-body']//div[@class='oxd-table-card']["+str(r)+"]//div[@role='cell']["+str(c)+"]").text
        headerlist.append(headerdata)
        rowlistdata.append(data)
        ##printing all data
        # print(headerdata , data ,end="\n")
        ##printing only disabled user
    if rowlistdata[3]=="Enabled":
        print(headerlist[0],rowlistdata[0])
        print(headerlist[1],rowlistdata[1])
        print(headerlist[2],rowlistdata[2])
        print(headerlist[3],rowlistdata[3])

    print("\n")

    




time.sleep(5)







##asignment print ESS role users only from the table


