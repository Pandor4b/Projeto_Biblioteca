import os
os.system("cls")
from pickle import TRUE


biblioteca = {}
recomendacoes= {}
lista_de_Recomendacoes = []
livros_filtrados = [] #Lista onde os livros dentro do filtro são colocados
precos_filtrados = {} #Dicionário onde os livros e preços dentro da faixa monetária são colocados


#==================================
#Função Login
def login(usuario):


    usuario = open('dados_' + str(usuario) + '.txt', 'a', encoding='utf-8')
    usuario.close()
    return

#==================================
#Função Logout
def logout():
    saida = input("Deseja fechar o aplicativo? \n[S] para Sim\n[N] para Não \n")
    saida.capitalize()
    os.system('cls')
    if saida == 'N':
        menu()
    if saida =='S':
        quit
    
#==================================
def inicio(): #Por os livros no arquivo na biblioteca
    file = open('dados_' + str(usuario) + '.txt', 'r', encoding='utf8')

    lista = []

    for i in file.readlines(): #Colocando as lines em uma lista

        lista.append(i)
    

#Manipulação da lista para por na biblioteca
    for j in range(len(lista)):
        lista[j] = lista[j].replace("\n", '')

        lista[j] = lista[j].split(',')
 

        biblioteca[lista[j][0]] = [lista[j][1], lista[j][2], float(lista[j][3])]
        

    file.close()


#==================================

#Função menu agindo corretamente
def menu():
    
    while True:
        print("Digite qual operação deseja fazer: ")
        print("\n1 - Cadastrar Novo Livro \n2 - Ler a biblioteca \n3 - Atualizar informações \n4 - Apagar um livro \n5 - Menu de Filtros \n6 - Ver Recomendações \n0 - Sair do programa")
        i = int(input(""))
        print("-----------")

        if i == 0:
            logout()
            break
        elif i == 1:
            cadastro_livros()
        
        elif i == 2:
            ler_livros()
        
        elif i == 3:
            atualizar_livros()

        elif i == 4:
            remover_livros()
        
        elif i == 5:
            MenuDeFiltros()

        elif i == 6:
            recomendations()
        
        else:
            print("Função não encontrada por favor tente novamente")

#==================================

#Função de Create/Cadastro de Livros
def cadastro_livros():
    file = open('dados_' + str(usuario) + '.txt', 'a', encoding='utf8')

    nome = input("Nome do livro: ")
    categoria = input("Categoria do livro: ") #Atualmente só suportamos 1 categoria
    autor = input("Autor do livro: ")
    valor = float(input("Valor gasto no livro: "))
    biblioteca[nome] = [categoria, autor, valor]
 
    # lista = list(biblioteca[nome])
    file.write(f"{nome},{categoria},{autor},{valor}\n")

    # file.writelines(f"{biblioteca}")

    file.close()

#==================================

def ler_livros():
    print(biblioteca)

    
#==================================

#Função Update/Atualizar informações de livros
def atualizar_livros():
    
    print("Qual livro deseja alterar as informações: ")
    key = input("livro: ")
    print("Secção de alterar informações, qual informação deseja alterar? \n1- Alterar Nome \n2- Alterar Categoria \n3- Alterar Autor \n4- Alterar valor")
    seccao = int(input())
    print("escreva a informação nova: ")
    value = input()

    if seccao == 4:
        value = float(value)

    if seccao == 1:
        
        biblioteca[value] = biblioteca[key]
        del biblioteca[key]

    else: 
        for i in range(len(biblioteca[key])):
            
            if i+1 == seccao:
                biblioteca[key][i] = value
    
    file = open('dados_' + str(usuario) + '.txt', 'w+', encoding='utf8')

    for livros in biblioteca.keys():
        
        file.write(f'{livros},{biblioteca[livros][0]},{biblioteca[livros][1]},{biblioteca[livros][2]}\n')
    
    file.close()

#==================================

#Função Delete/Remover livro do registro
def remover_livros():
    
    print("Qual livro deseja retirar a biblioteca?: ")
    key = input("livro: ")
    
    del biblioteca[key]

    file = open('dados_' + str(usuario) + '.txt', 'w+', encoding='utf8')

    for livros in biblioteca.keys():
        
        file.write(f'{livros},{biblioteca[livros][0]},{biblioteca[livros][1]},{biblioteca[livros][2]}\n')
    
    file.close()

#===================
def recomendations():
    file = open('recomend.txt', 'r', encoding='utf8')

    lista1 = []

    for i in file.readlines(): #Colocando as lines em uma lista1

        lista1.append(i)
    file.close()

#Manipulação da lista1 para por na biblioteca
    for j in range(len(lista1)):
        lista1[j] = lista1[j].replace("\n", '')

        lista1[j] = lista1[j].split(',')

        recomendacoes[lista1[j][0]] = [lista1[j][1:]]
    while TRUE: #
        gender = input("Digite o genero que deseja recomendações: ").capitalize() #escolhendo o genero para achar recomendações
        
        if gender in recomendacoes:

            print(f"Recomendações do genero {gender}: \n")

            num=0
            for item in recomendacoes.get(gender)[0]: #printando as recomendações
                num+=1
                print(f"{num}. {item}")

            continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper() #perguntando se a função será reiniciada
            if continuar == "N":
                break
            elif continuar == "S":
                os.system('cls')
                continue
        else:
            os.system('cls')
            print("Gênero não encontrado / ou não existem recomendações para este gênero")
            continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper() #perguntando se a função será reiniciada
            if continuar == "N":
                break
            elif continuar == "S":
                os.system('cls')
                continue

#=================
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
        while True:
            try:
                preco_min = float(input("Por favor coloque o preço mínimo desejado\n\n"))
                preco_max = float(input("\nPor favor coloque o preço máximo desejado\n\n")) #Tente converter os inputs do usuario em float
                os.system("cls")
            except:
                os.system("cls")
                print("ERRO: Digite um número válido! Se precisar usar casas decimais, use ponto em vez de vírgula!\n")
            else:

                while True:
                    precos_filtrados.clear() #Mesmo conceito da lista filtrada de livros de antes

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
                                print(f"{livro} --- R${preco}") #Imprime o livro e o seu preço

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



#--------------------------------------------------------

usuario = input("Informe o nome do usuário: ")

login(usuario)

inicio()

logout()