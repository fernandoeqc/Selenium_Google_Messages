
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
import os

caminho = os.path.dirname(os.path.abspath(__file__))

def chrome_drive():
    chrome_op = Options()   
    chrome_op.add_experimental_option("prefs", {
        "download.default_directory": r"C:\PROJETOS\PYTHON\Python_Selenium-BS2\chromedriver_win32",
        "download.Prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    
    b = __file__

    chrome = r'\chromedriver_win32\chromedriver.exe'

    driver = webdriver.Chrome(
        executable_path=caminho + chrome, options=chrome_op
    )
    wait = WebDriverWait(driver, 60)

def edge_drive():
    msedge = r'\edgedriver_win64\msedgedriver.exe'

    driver = webdriver.Edge(
        executable_path=caminho + msedge
    )
    wait = WebDriverWait(driver, 20)


    return driver, wait
# chrome_drive

driver, wait = edge_drive()
#print(caminho)
