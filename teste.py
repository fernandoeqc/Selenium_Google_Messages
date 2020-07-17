import random
from input_dados import *

def criaMsg(msgs,tel):
    txt_format = []
    linha = random.randrange(0, len(msgs) - 1)

    txt_format = msgs[linha].format(tel[0],tel[2])
    return txt_format

def enviaDeArquivo():
    tels = nome_numero('contatos.txt')
    msgs = separaLinhas('mensagens.txt')

    for tel in tels:
        a = criaMsg(msgs,tel)
        print(a)
        input()
    

enviaDeArquivo()
