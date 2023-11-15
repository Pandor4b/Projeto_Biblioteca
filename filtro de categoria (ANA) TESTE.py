import os
os.system("cls") #Limpa o terminal

Livros = {"Harry Potter":["Fantasia"], 
        "Senhor dos Anéis":["Fantasia"],
        "1984":["Distopia","Ficção Científica"], 
        "Maus":["Real", "HQ"], 
        "20.000 Léguas Submarinas":["Ficção Científica"]}   #Lista genérica de teste. O usuário irá colocar os livros

Categoria = input("") #Input do usuário

for livro, categorias in Livros.items(): 
    #.items() Transforma o dicionário em várias tuplazinhas de fácil compreensão pro código, permitindo a comparação.
    #("livro" são as keys e "categorias" são os valores de cada key)
    if Categoria in categorias:
        print(livro)
    else:
        continue
    #Se o input do usuário tiver dentro do valor da key, mostre a key
    #Se não, ignore e vá pra próxima key