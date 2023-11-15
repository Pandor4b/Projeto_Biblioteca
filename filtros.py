import os
os.system ("cls") #Limpa o terminal

#Eu odeio elif mas não sei de que maneira isso seria feito
#Código de base por Gabriel
#Modificado por João Marcelo

biblioteca = {'HARRY POTTER e o cálice de fogo': ["Ação", 'J. K. Rowling', 30.00],
            'HARRY POTTER e a câmara secreta': ["Ação", 'J. K. Rowling', 40.00], 
            'Maze Runner': ["Aventura", 'James Dashner', 30.00]} #Dicionário genérico de teste. O usuário irá colocar os livros


livros_filtrados = [] #Lista onde os livros dentro do filtro são colocados
precos_filtrados = {} #Dicionário onde os livros e preços dentro da faixa monetária são colocados


def MenuDeFiltros():
    comando_invalido = False #Esse boleano checa se o usuário mandou um comando inválido. Se sim, loopa o código e manda uma mensagem de erro
    while True:
        os.system ("cls")

        print("Você está no menu de filtros da sua biblioteca particular!")
        if comando_invalido == True:
            os.system ("cls")
            print("ERRO: Comando inválido! Por favor coloque um número de 0 a 3")
            comando_invalido = False #Isso garante que o código não vai loopar infinitamente

        print ("Qual filtro gostaria de usar na sua pesquisa?\n")
        filtro = input("(Para retornar ao menu principal digite 0)\n\n 1. Gênero\n 2. Autor\n 3. Preço \n\n").lower()

        if filtro == "1":
            FiltroPorGenero()
        elif filtro == '2':
            FiltroPorAutor()
        elif filtro == '3':
            FiltroPorPreco()
        elif filtro == '0':
            break #Aqui onde será a volta ao menu principal, mas ele não existe nesse código ainda
        else:
            comando_invalido = True
            continue


def FiltroPorGenero():
    comando_invalido = False
    while True:
        os.system ("cls")

        print('Você está na sessão de filtro por gênero!')
        genero = input("Por qual gênero você deseja filtrar?\n\n").title() #Input do usuário
        if genero == "Hq":
            genero = genero.upper() #Pra que funcione com esse gênero porque ele apresenta duas letras maiúsculas

        livros_filtrados.clear() #Isso garante que quaiser livros de uma filtração anterior são excluídos para a próxima filtração

        os.system ("cls")
        for livro, valores in biblioteca.items(): 
            if genero in valores:
                #.items() Transforma o dicionário em várias tuplazinhas de fácil compreensão pro código, permitindo a comparação
                #("livro" são as keys e "valores" são os valores de cada key)
                livros_filtrados.append(livro) #Os valores que tem o input do usuário são colocados na lista
        
        if not livros_filtrados:
            print("Nenhum livro com esse gênero encontrado") #Se não tiver nada na lista, fale que não tem nada na lista
        else:
            for livros in livros_filtrados:
                print(livros) #Se a lista tiver items, imprima-os

        while True:
            if comando_invalido == True:
                os.system ("cls")
                print("ERRO: Comando inválido! Por favor digite R, M ou G")
                comando_invalido = False
            retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nG = Filtrar por um gênero diferente\n\n')
            if retorno.upper() == "R": 
                MenuDeFiltros() #Volta ao menu de filtros
                break
            elif retorno.upper() == "M": 
                break
            elif retorno.upper() == "G":
                FiltroPorGenero() #Volta para o começo
                break
            else:
                comando_invalido = True
                continue


def FiltroPorAutor(): #Esse é quase idêntico ao anterior
    comando_invalido = False
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

        while True:
            if comando_invalido == True:
                os.system ("cls")
                print("ERRO: Comando inválido! Por favor digite R, M ou A")
                comando_invalido = False

            retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nA = Filtrar por um autor diferente\n\n')
            if retorno.upper() == "R": 
                MenuDeFiltros()
                break
            elif retorno.upper() == "M": 
                break
            elif retorno.upper() == "A":
                FiltroPorAutor()
                break
            else:
                comando_invalido = True
                continue


def FiltroPorPreco():
    comando_invalido = False
    while True:
        os.system ("cls")

        print('Você está na sessão de filtro por preço!')
        input_min = input("Por favor coloque o preço mínimo desejado\n\n").replace(",",".") #A vírgula das casa decimais é trocada por um ponto para garantir que será convertido num float
        input_max = input("\nPor favor coloque o preço máximo desejado\n\n").replace(",",".")
        os.system ("cls")

        input_min = input_min.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()-_=+|\/}{~``[]:;?"<>ç'})
        input_max = input_max.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*()-_=+|\/}{~``[]:;?"<>ç'})
        #Se o usuário digitar letras com números, isso tira as letras + qualquer coisa que não for número ou ponto

        if (len(input_min) == 0) or (len(input_max) == 0): #Garante que o string vai ter alguma coisa nele
            while True:
                #Se o usuário digita o comando certo, ele é mandado pra onde quer ir
                #Se o usuário digita o comadno errado, ele volta pro começo com uma mensagem de erro
                if comando_invalido == False:
                    os.system ("cls")
                    print("ERRO: Valores inválidos!")

                    retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n\n')
                    if retorno.upper() == "R": 
                        MenuDeFiltros()
                        break
                    elif retorno.upper() == "P":
                        FiltroPorPreco()
                        continue
                    else:
                        comando_invalido = True
                        continue

                elif comando_invalido == True:
                    os.system ("cls")
                    print("ERRO: Comando inválido! Por favor digite R, M ou P")

                    retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n\n')
                    if retorno.upper() == "R": 
                        MenuDeFiltros()
                        break
                    elif retorno.upper() == "M": 
                        break
                    elif retorno.upper() == "P":
                        FiltroPorPreco()
                        break
                    else:
                        continue #já está True então não precisa afirmar


        precos_filtrados.clear() #Mesmo conceito da lista filtrada de livros de antes

        if(len(input_min) != 0) and (len(input_max) != 0):
            preco_min = float(input_min)
            preco_max = float(input_max)
            if preco_max < preco_min: #Não existe preço negativo
                while True:
                    if comando_invalido == False:
                        os.system ("cls")
                        print("ERRO: Valores inválidos!")

                        retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n\n')
                        if retorno.upper() == "R": 
                            MenuDeFiltros()
                            break
                        elif retorno.upper() == "P":
                            FiltroPorPreco()
                            continue
                        else:
                            comando_invalido = True
                            continue

                    elif comando_invalido == True:
                        os.system ("cls")
                        print("ERRO: Comando inválido! Por favor digite R, M ou P")

                        retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n\n')
                        if retorno.upper() == "R": 
                            MenuDeFiltros()
                            break
                        elif retorno.upper() == "M": 
                            break
                        elif retorno.upper() == "P":
                            FiltroPorPreco()
                            break
                        else:
                            continue #já está True então não precisa afirmar

            elif preco_max > preco_min: #O correto
                faixa_do_preco = preco_max - preco_min
                for livro, valores in biblioteca.items(): 
                    preco = valores[2] #A terceira key da biblioteca é o preço
                    if ((preco_max - preco) <= faixa_do_preco) and ((preco - preco_min) <= faixa_do_preco): #Pra que o preço fique dentro da faixa de preço
                        precos_filtrados[livro] = preco #O livro e o preço são armazenados
            
                if not precos_filtrados:
                    print("Nenhum livro com essa faixa de preço encontrado")
                else:
                    for livro, preco in precos_filtrados.items():
                        print(f"{livro} --- {preco}") #Imprime o livro e o seu preço

                while True:
                    if comando_invalido == True:
                        os.system ("cls")
                        print("ERRO: Comando inválido! Por favor digite R, M ou P")
                        comando_invalido = False

                    retorno = input('\nR = Retornar ao menu de filtros\nM = Retornar ao menu pincipal \nP = Filtrar por um preço diferente\n\n')
                    if retorno.upper() == "R": 
                        MenuDeFiltros()
                        break
                    elif retorno.upper() == "M": 
                        break
                    elif retorno.upper() == "P":
                        FiltroPorPreco()
                        break
                    else:
                        comando_invalido = True
                        continue


MenuDeFiltros() #Início do código 💀