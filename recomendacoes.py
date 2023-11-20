import os
from pickle import TRUE
os.system('cls')

recomendacoes= {}
biblioteca = {} 
lista_de_Recomendacoes = []
def recomendations():
    file = open('recomend.txt', 'r', encoding='utf-8')

    lista1 = []

    for i in file.readlines(): #Colocando as lines em uma lista1

        lista1.append(i)
    file.close()

#Manipulação da lista1 para por na biblioteca
    for j in range(len(lista1)):
        lista1[j] = lista1[j].replace("\n", '')

        lista1[j] = lista1[j].split(',')

        recomendacoes[lista1[j][0]] = [lista1[j][1:]]
    while TRUE: #
        gender = input("Digite o genero que deseja recomendações: ").capitalize() #escolhendo o genero para achar recomendações
        
        if gender in recomendacoes:

            print(f"Recomendações do genero {gender}: \n")

            num=0
            for item in recomendacoes.get(gender)[0]: #printando as recomendações
                num+=1
                print(f"{num}. {item}")

            continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper() #perguntando se a função será reiniciada
            if continuar == "N":
                break
            elif continuar == "S":
                os.system('cls')
                continue
        else:
            os.system('cls')
            print("Gênero não encontrado / ou não existem recomendações para este gênero")
            continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper() #perguntando se a função será reiniciada
            if continuar == "N":
                break
            elif continuar == "S":
                os.system('cls')
                continue


recomendations()