#imports
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

with open('/home/rafael/virtual_enviroments/streamlit_funds/paths_links.json') as file:
    data = json.load(file)

chrome_driver_path = data["driverPath"]
download_path = data["downloadPath"]
cvm_link = data["dayliPath"]

def download_cvm() -> None:
    try:
        options = Options()
        options.add_experimental_option("prefs", {"download.default_directory": download_path})
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(cvm_link)
        driver.implicitly_wait(10)
        list_of_download_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "inf_diario")
        ActionChains(driver)\
        .click(list_of_download_links[-1])\
        .perform()

        time.sleep(60)

    except Exception as err:
        print("An error has ocurred! -> ", str(err))
        
    
    finally:
        driver.quit()





download_cvm()

#Unzip e and m