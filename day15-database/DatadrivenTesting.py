from selenium import webdriver
from selenium.webdriver.common.by import By
import excelutils , os , time
import mysql.connector

driver=webdriver.Chrome()

driver.get("https://www.federalbank.co.in/fixed-deposit-calculator")

driver.implicitly_wait(5)
driver.maximize_window()

select_query='select * from calcdata;'

try:
    con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="niteshdb")

    curs = con.cursor() ##cursor is a buffer through which we execute statements

    curs.execute(select_query) # execute query with cursor

    #fetch data from cursor

    for row in curs:

        ## read first row data
        amount = row[0]
        interest = row[1]
        duration =  row[2]
        expectedamount =    row[3]
        ## pass data to application
        driver.find_element(By.XPATH, "//input[@id='loanamount']").send_keys(amount)
        driver.find_element(By.XPATH, "//input[@id='loaninterest']").send_keys(interest)
        driver.find_element(By.XPATH, "//input[@id='loanterm']").send_keys(duration)

        driver.find_element(By.XPATH, "//input[@id='btn_calculate']").click()

        time.sleep(4)

        totalamount = driver.find_element(By.XPATH, "//span[@id='totreceivable']").text

        time.sleep(4)
        print(expectedamount, totalamount)

        ## Validation
        if float(expectedamount) == float(totalamount):
            print("test passed")
        else:
            print("test failed")

        ## clear input fields for next execution
        driver.find_element(By.XPATH, "//input[@id='loanamount']").clear()
        driver.find_element(By.XPATH, "//input[@id='loaninterest']").clear()
        driver.find_element(By.XPATH, "//input[@id='loanterm']").clear()

        time.sleep(3)

    con.close()

    print("Finished.............")
except:
    print("connection unsuccessful")

driver.close()


