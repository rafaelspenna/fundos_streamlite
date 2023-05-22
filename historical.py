from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import zipfile
import os

#Defining paths
chrome_driver_path = '/home/rafael/virtual_enviroments/chromedriver_linux64/chromedriver'
download_path = '/home/rafael/virtual_enviroments/streamlit_funds/downloads'
csv_path = '/home/rafael/virtual_enviroments/streamlit_funds/csv_files'

#Links
cvm_anual = 'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/HIST/'
cvm_24meses = 'https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/'

try:
    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": download_path})
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-gpu')  
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(cvm_anual)
    driver.implicitly_wait(10)
    list_of_download_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "inf_diario")
    
    for link in list_of_download_links:
        ActionChains(driver)\
        .click(link)\
        .perform()
        time.sleep(3)
    
    time.sleep(120)    

    driver.get(cvm_24meses)
    driver.implicitly_wait(10)
    list_of_download_links24 = driver.find_elements(By.PARTIAL_LINK_TEXT, "inf_diario")

    for link in list_of_download_links24:
        ActionChains(driver)\
        .click(link)\
        .perform()
        time.sleep(3)

    time.sleep(120)    

except Exception as err:
    print("An error has ocurred! -> ", str(err))

finally:
    driver.quit()

for file in os.listdir(download_path):
    if file.endswith('.zip'):
        file_path = os.path.join(download_path, file)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(csv_path)


#Create a function to unzip all historical files 
#Create a function to merge all unziped files into a single csv file
#Clean the data
#Copy the csv file into a SQL Database