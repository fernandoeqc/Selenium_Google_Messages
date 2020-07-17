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
        #print(x)
        #y = x.split()[0]
        matriz.append(x)
        #print(texto[linha].split('	'))
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
        y = x[0].split()[0]
        matriz.append(x)



    return matriz

if __name__ == "__main__":
    texto = entrada_com_txt('entradas.txt')

    def printSeparado(): 
        for linha in texto:
            for coluna in linha:
                print(coluna)
                input()

            print("**********************************")
    
    def printJunto():
        print(texto)
    
    print(nome_numero('entradas.txt'))
