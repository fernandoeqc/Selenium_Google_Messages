# -*- coding: UTF-8 -*-

#a = open('dados_cliente.txt','r',encoding='utf8')

def entrada_com_txt(arq):
    a = open(arq,'r',encoding='utf8')
    b = []
    c = []

    for i in a:
        b.append(i)
    a.close()

    for i in range(len(b)):
        c.append(b[i].split('	'))

    return c
'''
     
'''
    

if __name__ == "__main__":
    c = entrada_com_txt('entradas.txt')

    def printSeparado(): 
        for i in range(len(c)):
            for j in range(len(c[i])):
                print(c[i][j],'-',j)
            print("**********************************")
    
    def printJunto():
        print(c)
    
    printJunto()
