from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains ##import this class for mouse hover actions
import time
import os

##download files in one location 

def chrome_setup():
    ops = webdriver.ChromeOptions() ##chrome options object

    root_dir = os.getcwd()  ##get current directory path
    location = os.path.join(root_dir,"day12")

    preferences = {"download.default_directory":location} ##create custom download location
    ops.add_experimental_option("prefs",preferences)  ## add experimantal option using prefs keyword

    driver = webdriver.Chrome(options=ops)  ##pass options object as parameter
    return driver


##edge browser

def edge_setup():
    ops = webdriver.EdgeOptions() ##chrome options object

    root_dir = os.getcwd()  ##get current directory path
    location = os.path.join(root_dir,"day12")

    preferences = {"download.default_directory":location } ##create custom download location
    ops.add_experimental_option("prefs",preferences)  ## add experimantal option using prefs keyword

    driver = webdriver.Edge(options=ops)  ##pass options object as parameter
    return driver

## firefox browser

def firefox_setup():
    ops = webdriver.FirefoxOptions() ##chrome options object

    root_dir = os.getcwd()  ##get current directory path
    location = os.path.join(root_dir,"day12")

    #settings to avoid download manager in firefox
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/excel") ##mime types for the file 
    ops.set_preference("browser.download.manager.showWhenStarting",False) ##so that the download manger does not appear
    ops.set_preference("javascript.enabled",False) ## disable ads on the page 

    ##setting for custom download location
    ops.set_preference("browser.download.folderList",2) #0 - desktop  #1 -default location #2 desired location
    ops.set_preference("browser.download.dir",location)  ##if we select option 2 above
    

    driver = webdriver.Firefox(options=ops)  ##pass options object as parameter
    return driver



# driver = chrome_setup()

# driver = edge_setup()

driver = firefox_setup()

driver.get("https://filesampleshub.com/format/document/xls")

driver.maximize_window()


driver.find_element(By.XPATH,"//li[1]//a[1]").click()

# driver.switch_to.alert.accept()
time.sleep(2)

