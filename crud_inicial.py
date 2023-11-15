import os
os.system("cls")

#Dicionatio biblioteca - Atualmente vazio - Usuario insere as informações
#Informações para teste
biblioteca = {'Herding Cats':['Quadrinhos', 'Sarah Andersen', 30.00]} 

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
            cadastro()
        
        elif i == 2:
            print("Função Não encontrada, tente novamente")
        
        elif i == 3:
            atualizar()

        elif i == 4:
            remover()
        
        else:
            print("Função não encontrada por favor tente novamente")

#==================================

#Função de Create/Cadastro de Livros
def cadastro():

    nome = input("Nome do livro: ")
    categoria = input("Categoria do livro: ") #Atualmente só suportamos 1 categoria
    autor = input("Autor do livro: ")
    valor = float(input("Valor gasto no livro: "))
    biblioteca[nome] = [categoria, autor, valor]

#==================================

#Função Update/Atualizar informações de livros
def atualizar():

    print("Qual livro deseja alterar as informações: ")
    key = input("livro: ")
    print("Secção de alterar informações, qual informação deseja alterar? \n1- Alterar Categoria \n2- Alterar Autor \n3- Alterar valor")
    seccao = int(input())
    print("escreva a informação nova: ")
    value = input()

    if seccao == 3:
        value = float(value)

    for i in range(len(biblioteca[key])):
        
        if i+1 == seccao:
            biblioteca[key][i] = value

#==================================

#Função Delete/Remover livro do registro
def remover():
    print("Qual livro deseja retirar a biblioteca?: ")
    key = input("livro: ")

    del biblioteca[key]
    # for i in biblioteca:

        # if i == key:
            # biblioteca[i]


#--------------------------------------------------------

print("Seja bem vindo a sua biblioteca!")


