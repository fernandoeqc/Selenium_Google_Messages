from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

from time import sleep
from app_data import driver, wait
from input_dados import *

driver.get('https://messages.google.com/web/authentication')

input("espera")

def envioCompleto():
    msg_wait = 'msg-info'
    for i in range(10):
        msg_info = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, msg_wait))
        )
        
        if('SMS' not in msg_info.text):
            print('.',end='')
        else:
            return True
    return False

def chat(tel):
    start_chat = 'fab-label'
    numero_input_class = 'input'
    texto_xpath = '//textarea[@type="text"]'
    
    #try:
    novo_chat = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, start_chat))
    )
    novo_chat.click()
    #except:
    print("Selenium:  Novo Chat de " + tel[0])
    #return False

    #try:
    numero_input = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, numero_input_class))
    )
    numero_input.send_keys(tel[1])
    numero_input.send_keys(u'\ue007')
    #except:
    print("Selenium: colocou numero de " + tel[0])
    #return False

    #try:
    texto = wait.until(
        EC.presence_of_element_located((By.XPATH, texto_xpath))
    )
    #except:
    print("Selenium: procurou box txt de " + tel[0])
    #return False

    #try:
    texto.send_keys('Olá ')
    texto.send_keys(tel[0])
    texto.send_keys(', Este é um teste do Selenium.')
    sleep(0.5)
    texto.send_keys(u'\ue007')
    #except:
    print("Selenium:  enviou txt para " + tel[0])
    #return False

    if envioCompleto() == True:
        print("mensagem para " + tel[0] + " completa.")
    else:
        print("mensagem para " + tel[0] + " não enviada.")
        

    

    #input("espere a msg ser enviada")

    #msg_info = driver.find_elements_by_class_name('msg-info')
    #print(len(msg_info))

    #verificar se msg foi enviada antes de passar pra proxima



sleep(5)

tels = entrada_com_txt('entradas.txt')

for tel in tels:
    if(chat(tel) == False):
        input()
    

input("FIM")
driver.close()
