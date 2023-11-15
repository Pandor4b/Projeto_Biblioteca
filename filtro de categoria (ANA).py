import os
os.system("cls") #Limpa o terminal

Livros = {}

while True:
    livro_input = input('\nColoque aqui o nome do livro que gostaria de adicionar à biblioteca (Quando terminar, escreva "Fim")\n')
    if livro_input == 'Fim' or livro_input == 'fim':
        break
    else:
        categoria_input = input("\nE qual(is) é(são) a(s) categoria(s) do livro? (Separe por espaço)\n").split()
        Livros[livro_input] = categoria_input
#Faça um loop. Pergunte ao usuário o nome do livro
#Se o usuario colocar o nome do livro como "fim", encerre e vá para a próxima parte
#Se não, pergunte ao usuário as categorias do livro
#Depois adicione o livro com as suas categorias ao dicionário e volte para o começo

Categoria = input("\n\nGostaria de procurar por livros em que categoria?\n\n").title() #Input do usuário
if Categoria == "Hq":
    Categoria = Categoria.upper() #Pra que funcione com esse gênero porque ele apresenta duas letras maiúsculas

for livro, categorias in Livros.items(): 
    #.items() Transforma o dicionário em várias tuplazinhas de fácil compreensão pro código, permitindo a comparação.
    #("livro" são as keys e "categorias" são os valores de cada key)
    if Categoria in categorias:
        print(livro)
    else:
        continue
    #Se o input do usuário tiver dentro do valor da key, mostre a key
    #Se não, ignore e vá pra próxima key