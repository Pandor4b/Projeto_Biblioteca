import os
os.system('cls')

biblioteca = {}


def ler_livros():
    file = open('arquivo.txt', 'r')

    lista = []

    for i in file.readlines(): #Colocando as lines em uma lista

        lista.append(i)
    

#Manipulação da lista para por na biblioteca
    for j in range(len(lista)):
        lista[j] = lista[j].replace("\n", '')

        lista[j] = lista[j].split(',')
 

        biblioteca[lista[j][0]] = [lista[j][1], lista[j][2], float(lista[j][3])]
        

    print(biblioteca)

    file.close()


ler_livros()