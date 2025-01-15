from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

listoftickets = driver.find_elements(By.XPATH,"//ul[@id='checkout-products']/li")
for ticket in listoftickets:
    if ticket.text=="Dummy return ticket":
            ticket.click()
            break
    
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Nitesh")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Kumar")


#dob element
driver.find_element(By.XPATH,"//input[@id='dob']").click() #opens date picker

#use select class for dropdowns for month

monthelement = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
monthelement.select_by_visible_text("Oct")

#use select class for dropdowns for year

yearelement = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
yearelement.select_by_visible_text("1991")

#get all dates from table 
alldates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text == "20":
        date.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex_1']").click()

driver.find_element(By.XPATH,"//input[@id='addmorepax']").click()

passengerelt=Select(driver.find_element(By.XPATH,"//select[@id='addpaxno']"))
passengerelt.select_by_visible_text("add 2 more passengers (200%)")

time.sleep(3)
####################################################################################################################

driver.find_element(By.XPATH,"//input[@id='travname2']").send_keys("Rajiv")
driver.find_element(By.XPATH,"//input[@id='travlastname2']").send_keys("Ranjan")


#second passenger dob 
driver.find_element(By.XPATH,"//input[@id='dob2']").click() #opens date picker
monthelement1 = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
monthelement1.select_by_visible_text("Oct")

#use select class for dropdowns for year

yearelement1 = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
yearelement1.select_by_visible_text("1993")

#get all dates from table 
alldates1 = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates1:
    if date.text == "16":
        date.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex2_1']").click()

passengerelt=Select(driver.find_element(By.XPATH,"//select[@id='paxtype2']"))
passengerelt.select_by_visible_text("Adult")

time.sleep(3)

###################################################################################################
 #third passenger 
driver.find_element(By.XPATH,"//input[@id='travname3']").send_keys("Shubham")
driver.find_element(By.XPATH,"//input[@id='travlastname3']").send_keys("Kumar") 

#third passenger dob 
driver.find_element(By.XPATH,"//input[@id='dob3']").click() #opens date picker
monthelement2 = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
monthelement2.select_by_visible_text("Aug")

#use select class for dropdowns for year

yearelement2 = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
yearelement2.select_by_visible_text("1997")

#get all dates from table 
alldates2 = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates2:
    if date.text == "28":
        date.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex3_1']").click()


##trip details

driver.find_element(By.XPATH,"//input[@id='traveltype_1']").click()

driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Ranchi")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Ranchi")


#departure date

driver.find_element(By.XPATH,"//input[@id='departon']").click()



#use select class for dropdowns for year

yearelement3 = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
yearelement3.select_by_visible_text("2025")

monthelement3 = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
monthelement3.select_by_visible_text("Jan")



#get all dates from table 
alldates3 = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates3:
    if date.text == "15":
        date.click()
        break

driver.find_element(By.XPATH,"//textarea[@id='notes']").send_keys("Planning for a holiday with family members")




reasonelt = Select(driver.find_element(By.XPATH,"//select[@id='reasondummy']"))
reasonelt.select_by_visible_text("Visa extension")

driver.find_element(By.XPATH,"//input[@id='deliverymethod_1']").click()


##############################################----billing details---######################

driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("7857066836")

driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("nitesh.kumar@gmail.com")

countryelt = Select(driver.find_element(By.XPATH,"//select[@id='billing_country']"))
countryelt.select_by_visible_text("India")

driver.find_element(By.XPATH,"//input[@id='billing_address_1']").send_keys("Satellite colony Dhurwa Ranchi")

driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("Ranchi")

cityelt = Select(driver.find_element(By.XPATH,"//select[@id='billing_state']"))
cityelt.select_by_visible_text("Jharkhand")

driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("834004")

##table elemet

rows = driver.find_elements(By.XPATH,"//div[@class='opc_order_review']//table//tfoot/tr")

for i in range (1,len(rows)+1):
    header = driver.find_element(By.XPATH,"//div[@class='opc_order_review']//table//tfoot/tr["+str(i)+"]/th")
    data = driver.find_element(By.XPATH,"//div[@class='opc_order_review']//table//tfoot/tr["+str(i)+"]/td")
    print(header.text ,"----", data.text,end="\n")

time.sleep(3)
    
