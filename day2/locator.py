from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# options = Options()
# options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# options.add_argument("--remote-debugging-port=9222")
# # options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window() #maximize the browser window

# driver.find_element(by=By.ID,value="small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# driver.find_element(by=By.NAME,value="q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# driver.find_element(by=By.LINK_TEXT,value="Register").click() ##text of the link

# driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Reg").click()  ##partial text of the link

##multiple elements
answers=driver.find_elements(by=By.CLASS_NAME,value="answer")  #return multiple elements so find_elements
print("total answers:",len(answers))

for ans in answers:
    print(ans.text)

links = driver.find_elements(by=By.TAG_NAME,value="a")
print("total links:",len(links))

for link in links:
    print(link.text)


driver.close() #close one browser
# driver.quit() #closes all browsers
