import os
from pickle import TRUE
os.system('cls')

recomendacoes= {}
biblioteca = {'Herding Cats':['Quadrinhos', 'Sarah Andersen', 30.00]} 
def recomendations():
    file = open('recomend.txt', 'r', encoding='utf8')

    lista1 = []

    for i in file.readlines(): #Colocando as lines em uma lista1

        lista1.append(i)


#Manipulação da lista1 para por na biblioteca
    for j in range(len(lista1)):
        lista1[j] = lista1[j].replace("\n", '')

        lista1[j] = lista1[j].split(',')

        recomendacoes[lista1[j][0]] = [lista1[j][1:]]
    while TRUE:
        gender = input("Digite o genero que deseja recomendações: ").capitalize()
        if gender in recomendacoes:

            tamanho = 0
            for K in range (len(lista1)):
                tamanho = (len(lista1[K]))
            morte = (str(next(iter(biblioteca))))

            if tamanho != 0:
                print(f"Recomendações do genero {gender}: \n")
                for i in range (tamanho): 

                    if i > 0:
                        if str(lista1[j][i]) != morte:
                            print(f"{i}. ",lista1[j][i])

                continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper()
                if continuar == "N":
                    break
                elif continuar == "S":
                    os.system('cls')
                    continue
        else:
            os.system('cls')
            print("Genero não encontrado")
            continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper()
            if continuar == "N":
                break
            elif continuar == "S":
                os.system('cls')
                continue
            
                        
                    
        
        

    file.close()


recomendations()