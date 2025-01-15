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

driver.get("https://www.facebook.com/")
# driver.get("https://www.facebook.com/")
driver.maximize_window()

##tag and id #
# driver.find_element(by=By.CSS_SELECTOR,value="input#email").send_keys("nitesh")
driver.find_element(by=By.CSS_SELECTOR,value="#email").send_keys("nitesh@gmail.com")


## tag and class .
# driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext").send_keys("nitesh")
# driver.find_element(by=By.CSS_SELECTOR,value=".inputtext").send_keys("nitesh")

## tag and attribute []
# driver.find_element(by=By.CSS_SELECTOR,value="input[name=email]").send_keys("nitesh")
# driver.find_element(by=By.CSS_SELECTOR,value="[name=email]").send_keys("nitesh")


##tag class attribute.[]
# driver.find_element(by=By.CSS_SELECTOR,value="input.inputtext[id=pass]").send_keys("nitesh")







# driver.close() #close one browser
# driver.quit() #closes all browsers
