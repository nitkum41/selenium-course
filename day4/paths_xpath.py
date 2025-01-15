from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()

driver.implicitly_wait(10)

#self node

# text = driver.find_element(By.XPATH,".//a[contains(text(),'India Cements Lt')]/self::a").text
# print("text of the self element is :" , text)

#parent
# text = driver.find_element(By.XPATH,".//a[contains(text(),'India Cements Lt')]/parent::td").text
# print("text of the parent element is :" , text) 


#child 
# child_node = driver.find_element(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/child::td").text  #matches only one elemnt

#matches all the elements
# child_nodes = driver.find_elements(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/child::td")
# print("total no f child nodes",len(child_nodes))


# for i in (0,len(child_nodes)-1):
#     print(child_nodes[i].text)


#ancenstor

# text = driver.find_element(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr").text 

# #print entire row values as text
# print("ancestor of the self element is :" , text)


#descendant

# descendants = driver.find_elements(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/descendant::*")
# print("total no f descendents ",len(descendants))  ##10

# #print entire row values as text
# for i in (0,len(descendants)-1):
#     print(descendants[i].text)

##following

# following = driver.find_elements(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/following::*")
# print("total no f following ",len(following))   ##3799

##following siblings

# following_siblings = driver.find_elements(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/following-sibling::tr")
# print("total no f following siblings ",len(following_siblings))  #329

##preceding

precedings = driver.find_elements(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/preceding::tr")
print("total no f preceding ",len(precedings))   ##11


##preceding siblings

preceding_siblings = driver.find_elements(By.XPATH,".//a[contains(text(),'India Cements Lt')]/ancestor::tr/preceding-sibling::tr")
print("total no f preceding siblings ",len(preceding_siblings))  #10







driver.close()


