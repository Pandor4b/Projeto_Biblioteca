import os
os.system("cls")

Livros = {"Fantasia":["Harry Potter", "Senhor dos Anéis"], 
        "Ficção Científica":["1984", "Farenheit 451", "20.000 Léguas Submarinas"],
        "Real":["Maus", "Invencível"]}

Categoria = input("").capitalize()

for livro, categorias in Livros.items():
    if Categoria in categorias:
        print(livro)   