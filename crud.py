import os
os.system("cls")

# livros = { 'Nome_do_Livro': ['Categoria', 'Autor', Preço]}

#Dicionatio biblioteca - Atualmente vazio - Usuario insere as informações
biblioteca = {'Herding Cats':['Quadrinhos', 'Sarah Andersen', 30.00]}


#Função menu ainda não funciona corretamente (while true infinito)
def menu():
    
    while True:
        print("Digite qual operação deseja fazer: ")
        print("1 - Cadastrar Novo Livro \n2 - Ler a biblioteca \n3 - Atualizar informações \n4 - Apagar um livro\n 0 - Sair do programa")
        i = input("")

        if i == 0:
            break
        elif i == 1:
            return cadastro()


#Função de Create/Cadastro de Livros
def cadastro():

    nome = input("Nome do livro: ")
    categoria = input("Categoria do livro: ") #Atualmente só suportamos 1 categoria
    autor = input("Autor do livro: ")
    valor = float(input("Valor gasto no livro: "))
    biblioteca[nome] = [categoria, autor, valor]

# def read(): #Atualmente sem ideia de como executar


#Função Update/Atualizar informações de livros
def update():

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


#--------------------------------------------------------
cadastro()
print(biblioteca)

update()
print(biblioteca)