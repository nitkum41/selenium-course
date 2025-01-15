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

    preferences = {
            "download.default_directory":location, ##create custom download location
            "plugins.always_open_pdf_externally":True, ##download pdf externally
            "profile.managed_default_content_settings.javascript": 2 #disable ads
            } 
    ops.add_experimental_option("prefs",preferences)  ## add experimantal option using prefs keyword
   

    driver = webdriver.Chrome(options=ops)  ##pass options object as parameter
    return driver


##edge browser

def edge_setup():
    ops = webdriver.EdgeOptions() ##chrome options object

    root_dir = os.getcwd()  ##get current directory path
    location = os.path.join(root_dir,"day12")

    preferences = {
        "download.default_directory":location, ##create custom download location
        "plugins.always_open_pdf_externally":True, ##download pdf externally
        "profile.default_content_setting_values.javascript": 2 #disable ads
        } 
    ops.add_experimental_option("prefs",preferences)  ## add experimantal option using prefs keyword
    
    
  

    driver = webdriver.Edge(options=ops)  ##pass options object as parameter
    return driver

## firefox browser

def firefox_setup():
    ops = webdriver.FirefoxOptions() ##chrome options object

    root_dir = os.getcwd()  ##get current directory path
    location = os.path.join(root_dir,"day12")

    #settings to avoid download manager in firefox
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf") ##mime types for the file 
    ops.set_preference("browser.download.manager.showWhenStarting",False) ##so that the download manger does not appear
    ops.set_preference("javascript.enabled",False) ## disable ads on the page 

    ##setting for custom download location
    ops.set_preference("browser.download.folderList",2) #0 - desktop  #1 -default location #2 desired location
    ops.set_preference("browser.download.dir",location)  ##if we select option 2 above
    
    ops.set_preference("pdfjs.disabled",True) #for pdf download

    driver = webdriver.Firefox(options=ops)  ##pass options object as parameter
    return driver


try:
    # driver = chrome_setup()

    # driver = edge_setup()

    driver = firefox_setup()

    driver.get("https://filesamples.com/formats/pdf")

    driver.maximize_window()

    time.sleep(2)

    driver.find_element(By.XPATH,"//div[@class='md:col-span-3 col-span-4']//div[2]//a[1]").click()


    time.sleep(10)

finally:
    driver.quit()


