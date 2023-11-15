biblioteca = {'HARRY POTTER: o calice de fogo': ["Ação", 'J.K Rolling', 30.00], 'HARRY POTTER: e a camara secreta': ["Ação", 'J.K Rolling', 40.00], 'Maze Runner': ["aventura", 'James Dashner', 30.00]}

def MenuDeFiltros():
    print("você está no Menu de filtros da sua biblioteca particular!")
    while True:
        print ("pelo oque você deseja filtrar?")
        filtro = input("(para retornar ao menu principal digite 0)1. categoria\n 2. autor\n 3. preço ").lower()

        if filtro == "categoria":
            FiltroPorCategoria()
        elif filtro == 'autor':
            FiltroPorAutor()
        elif filtro == 'Preço':
            FiltroPorPreco()
        elif filtro == '0':
            break

def FiltroPorAutor():

    return()
def FiltroPorCategoria():
    return()

def FiltroPorPreco():
    return()