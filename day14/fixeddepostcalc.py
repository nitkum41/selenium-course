from selenium import webdriver
from selenium.webdriver.common.by import By
import excelutils , os , time
import openpyxl

driver=webdriver.Chrome()

driver.get("https://www.federalbank.co.in/fixed-deposit-calculator")

driver.implicitly_wait(5)
driver.maximize_window() 

file = os.path.join(os.getcwd(),"day14\\testdata.xlsx")

rows = excelutils.getRowCount(file,"Data")

for r in range(2,rows+1):
## read first row data    
    amount = excelutils.readCellData(file,"Data",r,1)
    interest = excelutils.readCellData(file,"Data",r,2)
    duration = excelutils.readCellData(file,"Data",r,3)
    expectedamount = excelutils.readCellData(file,"Data",r,4)
## pass data to application
    driver.find_element(By.XPATH,"//input[@id='loanamount']").send_keys(amount)
    driver.find_element(By.XPATH,"//input[@id='loaninterest']").send_keys(interest)
    driver.find_element(By.XPATH,"//input[@id='loanterm']").send_keys(duration)

    driver.find_element(By.XPATH,"//input[@id='btn_calculate']").click()

    time.sleep(4)

    totalamount=driver.find_element(By.XPATH,"//span[@id='totreceivable']").text

    time.sleep(4)
    print(expectedamount,totalamount)

## Validation
    if float(expectedamount)==float(totalamount):
        print("test passed")
        excelutils.writeCellData(file,"Data",r,6,"passed")
        excelutils.fillGreenColor(file,"Data",r,6)
    else:
        print("test failed")
        excelutils.writeCellData(file,"Data",r,6,"failed")
        excelutils.fillRedColor(file,"Data",r,6)

    ## clear input fields for next execution
    driver.find_element(By.XPATH,"//input[@id='loanamount']").clear()
    driver.find_element(By.XPATH,"//input[@id='loaninterest']").clear()
    driver.find_element(By.XPATH,"//input[@id='loanterm']").clear()

    time.sleep(3)

driver.close()


