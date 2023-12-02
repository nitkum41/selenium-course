from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

options = Options()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument("--remote-debugging-port=9222")
# options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element(by=By.ID,value="small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# driver.find_element(by=By.NAME,value="q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# driver.find_element(by=By.LINK_TEXT,value="Register").click()

# driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Reg").click()

##multiple elements
answers=driver.find_elements(by=By.CLASS_NAME,value="answer")
print("total answers:",len(answers))

for ans in answers:
    print(ans.text)

links = driver.find_elements(by=By.TAG_NAME,value="a")
print("total links:",len(links))

for link in links:
    print(link.text)


driver.close() #close one browser
# driver.quit() #closes all browsers
