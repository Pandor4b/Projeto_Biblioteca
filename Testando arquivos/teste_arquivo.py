import os
os.system("cls")


biblioteca = {}
# livros = { 'Nome_do_Livro': ['Categoria', 'Autor', Preço]}
# biblioteca = {'Herding Cats':['Quadrinhos', 'Sarah Andersen', 30.00]} 

#==================================
def iniico(): #Por os livros no arquivo na biblioteca
    file = open('arquivo.txt', 'r')

    lista = []

    for i in file.readlines(): #Colocando as lines em uma lista

        lista.append(i)
    

#Manipulação da lista para por na biblioteca
    for j in range(len(lista)):
        lista[j] = lista[j].replace("\n", '')

        lista[j] = lista[j].split(',')
 

        biblioteca[lista[j][0]] = [lista[j][1], lista[j][2], float(lista[j][3])]
        

    file.close()


#==================================

#Função menu agindo corretamente
def menu():
    
    while True:
        print("Digite qual operação deseja fazer: ")
        print("\n1 - Cadastrar Novo Livro \n2 - Ler a biblioteca \n3 - Atualizar informações \n4 - Apagar um livro \n0 - Sair do programa")
        i = int(input(""))
        print("-----------")

        if i == 0:
            break
        elif i == 1:
            cadastro_livros()
        
        elif i == 2:
            ler_livros()
        
        elif i == 3:
            atualizar_livros()

        elif i == 4:
            remover_livros()
        
        else:
            print("Função não encontrada por favor tente novamente")

#==================================

#Função de Create/Cadastro de Livros
def cadastro_livros():
    file = open('arquivo.txt', 'a')

    nome = input("Nome do livro: ")
    categoria = input("Categoria do livro: ") #Atualmente só suportamos 1 categoria
    autor = input("Autor do livro: ")
    valor = float(input("Valor gasto no livro: "))
    biblioteca[nome] = [categoria, autor, valor]
 
    # lista = list(biblioteca[nome])
    file.write(f"{nome}, {categoria}, {autor}, {valor}\n")

    # file.writelines(f"{biblioteca}")

    file.close()

#==================================

def ler_livros():
    print(biblioteca)

    
#==================================

#Função Update/Atualizar informações de livros
def atualizar_livros():
    
    print("Qual livro deseja alterar as informações: ")
    key = input("livro: ")
    print("Secção de alterar informações, qual informação deseja alterar? \n1- Alterar Nome \n2- Alterar Categoria \n3- Alterar Autor \n4- Alterar valor")
    seccao = int(input())
    print("escreva a informação nova: ")
    value = input()

    if seccao == 4:
        value = float(value)

    if seccao == 1:
        
        biblioteca[value] = biblioteca[key]
        del biblioteca[key]

    else: 
        for i in range(len(biblioteca[key])):
            
            if i+1 == seccao:
                biblioteca[key][i] = value
    
    file = open('arquivo.txt', '+r')

    file.close()

#==================================

#Função Delete/Remover livro do registro
def remover_livros():
    file = open('arquivo.txt', '+r')
    
    print("Qual livro deseja retirar a biblioteca?: ")
    key = input("livro: ")

    
    del biblioteca[key]


    
    file.close()



#--------------------------------------------------------
iniico()
print("Seja bem vindo a sua biblioteca!")

menu()