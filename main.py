from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException

import random
from time import sleep
from app_data import driver, wait
from input_dados import *



def criaMsg(msgs,tel):
    txt_format = []
    linha = random.randrange(0, len(msgs) - 1)

    txt_format = msgs[linha].format(tel[0],tel[2])
    return txt_format


"""     texto.send_keys('Olá ')
    texto.send_keys(tel[0])
    texto.send_keys(', Este é um teste do Selenium.')
    sleep(0.5)
    texto.send_keys(u'\ue007') """

def verificaEnvioCompleto():
    msg_wait = 'msg-info'
    for i in range(20):
        sleep(0.5)
        try:
            msg_info = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, msg_wait))
            )

            if(('SMS' or 'Entregue' or 'Lido') not in msg_info.text):
                print('.',end='')
            else:
                return True
        except:
            print('_',end='')

    return False

def chat(tel,msgs):
    start_chat = 'fab-label'
    numero_input_class = 'input'
    texto_xpath = '//textarea[@type="text"]'
    
    try:
        novo_chat = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, start_chat))
        )
        novo_chat.click()
    except:
        print("Selenium: Erro Novo Chat de " + tel[0])
        #return False

    try:
        numero_input = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, numero_input_class))
        )
        numero_input.send_keys(tel[1])
        #sleep(0.5)
        numero_input.send_keys(u'\ue007')
    except:
        print("Selenium: Não colocou numero de " + tel[0])
        #return False

    try:
        campo_txt = wait.until(
            EC.presence_of_element_located((By.XPATH, texto_xpath))
        )
    except:
        print("Selenium: nao achou box txt de " + tel[0])
        #return False

    try:
        txt_format = criaMsg(msgs,tel)
        campo_txt.send_keys(txt_format)
        print(txt_format)
        #campo_txt.send_keys(u'\ue007')

    except:
        print("Selenium: Não deu enter na mensagem p/ " + tel[0])
        return False

    print("Verificando ")
    if verificaEnvioCompleto() == True:
        print("mensagem para " + tel[0] + " completa.")
    else:
        print("mensagem para " + tel[0] + " não enviada.")
        

    

    #input("espere a msg ser enviada")

    #msg_info = driver.find_elements_by_class_name('msg-info')
    #print(len(msg_info))

    #verificar se msg foi enviada antes de passar pra proxima

def enviaDeArquivo():
    tels = nome_numero('contatos.txt')
    msgs = separaLinhas('mensagens.txt')
    for tel in tels:
        if(chat(tel,msgs) == False):
            input("Mensagem nao enviada. Press pra continuar.")
        
        espera = random.randrange(30,180)
        print(espera)
        sleep(espera)

driver.get('https://messages.google.com/web/authentication')
input("espera")
sleep(5)

enviaDeArquivo()


input("FIM")
driver.close()
