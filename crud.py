import os
os.system("cls")

# livros = { 'Nome_do_Livro': ['Categoria', 'Autor', Preço]}
biblioteca = {}
file = open("teste.txt", "a")

def menu():
    
    while True:
        print("Digite qual operação deseja fazer: ")
        print("1 - Cadastrar Novo Livro \n2 - Ler a biblioteca \n3 - Atualizar informações \n4 - Apagar um livro\n 0 - Sair do programa")
        i = input("")

        if i == 0:
            break


def cadastro():

    nome = input("Nome do livro: ")
    categoria = input("Categoria do livro: ")
    autor = input("Autor do livro: ")
    valor = float(input("Nome do livro: "))

    biblioteca[nome] = [categoria, autor, valor]

cadastro()
file.write(biblioteca.keys())
file.close()
print(biblioteca)