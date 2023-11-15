import os
os.system ("cls")


biblioteca = {'HARRY POTTER e o cálice de fogo': ["Ação", 'J. K. Rowling', 30.00],
            'HARRY POTTER e a câmara secreta': ["Ação", 'J. K. Rowling', 40.00], 
            'Maze Runner': ["Aventura", 'James Dashner', 30.00]}


livros_filtrados = []
precos_filtrados = {}

def MenuDeFiltros():
    while True:
        os.system ("cls")
        print("Você está no menu de filtros da sua biblioteca particular!")
        print ("Qual filtro gostaria de usar na sua pesquisa?")
        filtro = input("(Para retornar ao menu principal digite 0) \n 1. Gênero\n 2. Autor\n 3. Preço \n").lower()

        if filtro == "1":
            FiltroPorGenero()
        elif filtro == '2':
            FiltroPorAutor()
        elif filtro == '3':
            FiltroPorPreco()
        elif filtro == '0':
            break


def FiltroPorGenero():
    while True:
        os.system ("cls")
        print('Você está na sessão de filtro por gênero!')
        genero = input("Por qual gênero você deseja filtrar?\n").title()
        if genero == "Hq":
            genero = genero.upper()

        livros_filtrados.clear()

        os.system ("cls")
        for livro, valores in biblioteca.items(): 
            if genero in valores:
                livros_filtrados.append(livro)
        
        if not livros_filtrados:
            print("Nenhum livro com esse gênero encontrado")
        else:
            for livros in livros_filtrados:
                print(livros)

        retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nG = Filtrar por um gênero diferente\n')
        if retorno.upper() == "R": 
            MenuDeFiltros()
            break
        elif retorno.upper() == "G":
            continue


def FiltroPorAutor():
    while True:
        os.system ("cls")
        print('Você está na sessão de filtro por autor!')
        autor = input("Por qual autor você deseja filtrar?\n").title()
        os.system ("cls")

        livros_filtrados.clear()

        for livro, valores in biblioteca.items():
            if autor in valores:
                livros_filtrados.append(livro)
        
        if not livros_filtrados:
            print("Nenhum livro com esse autor encontrado")
        else:
            for livros in livros_filtrados:
                print(livros)

        retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nA = Filtrar por um autor diferente\n')
        if retorno.upper() == "R": 
            MenuDeFiltros()
            break
        elif retorno.upper() == "A":
            continue


def FiltroPorPreco():
    while True:
        os.system ("cls")
        print('Você está na sessão de filtro por preço!')
        preco_min = float(input("Por favor coloque o preço mínimo desejado\n").replace(",","."))
        preco_max = float(input("\nPor favor coloque o preço máximo desejado\n").replace(",","."))
        os.system ("cls")

        precos_filtrados.clear()

        if preco_max < preco_min:
            print("ERRO: Valores inválidos!")
            retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n')
            if retorno.upper() == "R": 
                MenuDeFiltros()
                break
            elif retorno.upper() == "P":
                continue

        elif preco_max > preco_min:
            faixa_do_preco = preco_max - preco_min
            for livro, valores in biblioteca.items(): 
                preco = valores[2]
                if ((preco_max - preco) and (preco - preco_min)) <= faixa_do_preco:
                    precos_filtrados[livro] = preco
        
            if not precos_filtrados:
                print("Nenhum livro com essa faixa de preço encontrado")
            else:
                for livros in precos_filtrados:
                    print(livros)

            retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n')
            if retorno.upper() == "R": 
                MenuDeFiltros()
                break
            elif retorno.upper() == "P":
                continue

MenuDeFiltros()