# -*- coding: UTF-8 -*-

#a = open('dados_cliente.txt','r',encoding='utf8')

def nome_numero(arq):
    arquivo = open(arq,'r',encoding='utf8')
    texto = []
    matriz = []

    for linha in arquivo:
        texto.append(linha)
    arquivo.close()

    for linha in range(len(texto)):
        x = texto[linha].split('	')
        x[0] = x[0].split()[0]
        matriz.append(x)

    return matriz

def entrada_com_txt(arq):
    arquivo = open(arq,'r',encoding='utf8')
    texto = []
    matriz = []

    for linha in arquivo:
        texto.append(linha)
    arquivo.close()

    for linha in range(len(texto)):
        x = texto[linha].split('	')
        matriz.append(x)



    return matriz

if __name__ == "__main__":
    texto = entrada_com_txt('entradas.txt')
    mensagens = entrada_com_txt('mensagens.txt')

    def printLinha(arq):
        for linha in arq:
            for coluna in linha:
                print(coluna,end='')
            input("*")

    def printSeparado(arq): 
        for linha in arq:
            for coluna in linha:
                print(coluna)
                input()

            print("**********************************")
    
    def printJunto(arq):
        print(texto)
    
