import os
os.system   ("cls")
biblioteca = {'HARRY POTTER: o calice de fogo': ["Ação", 'J.K Rolling', 30.00], 'HARRY POTTER: e a camara secreta': ["Ação", 'J.K Rolling', 40.00], 'Maze Runner': ["aventura", 'James Dashner', 30.00]}

def MenuDeFiltros():
    print("você está no Menu de filtros da sua biblioteca particular!")
    while True:
        os.system   ("cls")
        print ("pelo oque você deseja filtrar?")
        filtro = input("(para retornar ao menu principal digite 0) \n 1. Genero\n 2. autor\n 3. preço \n").lower()

        if filtro == "genero":
            FiltroPorGenero()
        elif filtro == 'autor':
            FiltroPorAutor()
        elif filtro == 'Preço':
            FiltroPorPreco()
        elif filtro == '0':
            break

def FiltroPorAutor(autor):

    return()
def FiltroPorGenero():
    while True:
        os.system ("cls")
        print('você está na sessão de filtro por Genero!')
        categoria = input("por qual genero você desaja filtrar?")
        os.system ("cls")
        for livro, categorias in biblioteca.items(): 

            if categoria in categorias:
                print(livro, "\n")
        retorno = input("\nR para voltar ao menu de filtros\nM para retornar ao Menu pincipal \nG para filtrar por um genero diferente\n")
        if retorno.upper == "R": 
            break
        elif retorno.upper == "G":
            continue
        

def FiltroPorPreco():
    return()

MenuDeFiltros()