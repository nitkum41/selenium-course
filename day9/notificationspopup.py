from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# serv_obj=Service(r"C:\Drivers\chromedriver_win32\chromedriver.exe")

##options object
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options.add_argument("--disable-notifications--") ##disable notifications pop up

driver = webdriver.Chrome(options=options)

driver.get("https://whatmylocation.com/")
driver.maximize_window()