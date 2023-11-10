import os
os.system("cls")

Livros = {"Harry Potter":["Fantasia"], "Senhor dos Anéis":["Fantasia"], "1984":["Distopia", "Ficção Científica"], "Maus":["Real", "HQ"], "20.000 Léguas Submarinas":["Ficção Científica"]}

Categoria = input("")

for livro, categorias in Livros.items():
    if Categoria in categorias:
        print(livro)
    else:
        continue