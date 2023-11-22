from ast import Num
import os
os.system("cls")

# (template bonitinho)
#print("\n="*9) 


biblioteca = {} #Dict principal
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
    while True:
        print("-----------------------------------------------------")
        saida = input("Deseja continuar na aplicação? \n[S] para Continuar\n[N] para Fechar\n").upper()
        os.system('cls')
        if saida == 'S':
            menu()
        elif saida =='N':
            break
        elif saida != "S" and saida != "N":
            print("Comando inválido, digite [S] ou [N]")
            
            continue
    
#==================================
#Função inical - insere os livros já existentes na dict da biblioteca 
def inicio():
    file = open('dados_' + str(usuario) + '.txt', 'r', encoding='utf8')

    lista = []

    for i in file.readlines(): #Colocando as lines em uma lista
        lista.append(i)
    
#Manipulação da lista para por na biblioteca
    for j in range(len(lista)):
        lista[j] = lista[j].replace("\n", '')
        lista[j] = lista[j].split('//')
 
        biblioteca[lista[j][0]] = [lista[j][1], lista[j][2], float(lista[j][3])]
        
    file.close()

#==================================
#Função menu agindo corretamente
def menu():
    
    while True:
        os.system('cls')
        print("Digite qual operação deseja fazer: ")
        print("\n[1] - Cadastrar Novo Livro \n[2] - Ler a biblioteca \n[3] - Atualizar informações \n[4] - Apagar um livro \n[5] - Menu de Filtros \n[6] - Ver Recomendações \n[0] - Sair do programa\n")
        i = (input("- "))
        print("--------------------------------------------------------\n")

        if i == "0":
            os.system ("cls")
            return()
        elif i == "1":
            cadastro_livros()
        
        elif i == "2":
            ler_livros()
        
        elif i == "3":
            atualizar_livros()

        elif i == "4":
            remover_livros()
        
        elif i == "5":
            MenuDeFiltros()

        elif i == "6":
            recomendations()
        
        else:
            os.system("cls")
            print("Função não encontrada por favor tente novamente")

#==================================
#Função de Create/Cadastro de Livros
def cadastro_livros():
    file = open('dados_' + str(usuario) + '.txt', 'a', encoding='utf8')

    
    while True:
        # os.system("cls")

        print("\tCadastro de Livros\n")
        print("Para continuar digite o nome do livro \nPara voltar ao menu principal digite [0]\n")
        nome = input("Nome do livro: ").title()

        if nome == "0":
            os.system("cls")
            break

        elif nome not in biblioteca:
            
            categoria = input("Gênero do livro: ").title() #Atualmente só suportamos 1 genero
            autor = input("Autor do livro: ").title()
            while True:
                try:
                    valor = float(input("Valor gasto no livro: "))

                except ValueError:
                    os.system("cls")
                    print("Valor inválido, digite um valor válido")

                    continue

                else:
                    biblioteca[nome] = [categoria, autor, valor] #adiciona o livro a biblioteca                    
                    file.write(f"{nome}//{categoria}//{autor}//{valor}\n") #adiciona o livro ao arquivo
                
                    file.close() #fecha o arquivo

                    break
            break
        else:
            os.system("cls")
            print(f"O livro {nome} já se encontra na sua biblioteca\n")

            continue
                
#==================================
#Função Leitura da biblioteca
def ler_livros():
    os.system("cls")
    print("\tlivros Na sua Biblioteca\n")
    Numero_de_livros = 0
    diminui = 0
    lista_de_leitura = [0]
    while True:
        try:
            for livros in biblioteca:
                Numero_de_livros += 1
                
                print(f"{Numero_de_livros}. {livros}")
                lista_de_leitura.append(livros)
                
                if len(lista_de_leitura) > len(biblioteca)+1:
                    lista_de_leitura.pop()
                    
                
            Numero_de_livros = 0
            
            print("\n\nDigite o numero correspondente para ver as informações de um livro. \nPara voltar ao menu principal digite [0]\n")
            ação = int(input("- "))
            if ação == 0:
                return()
            else:
                os.system("cls")
                print("="*9)
            #printa o livro e suas informações (tem que se referir assim mesmo, porque a forma de importar o arquivo deixa ele assim)
                print(f"Nome: {lista_de_leitura[ação]} \nGenero: {biblioteca[lista_de_leitura[ação]][0]} \nAutor: {biblioteca[lista_de_leitura[ação]][1]} \nValor: {biblioteca[lista_de_leitura[ação]][2]} \n")
                break
        except ValueError:
            os.system("cls")
            print("="*9)
            print("ERRO: O indice inserido não coresponde a nenhum livro.\n\n")
            continue
        except IndexError:
            os.system("cls")
            print("="*9)
            print("ERRO: O indice inserido não coresponde a nenhum livro. \n\n")
            continue
    while True:
        retorno = (input("\n\nDigite [0] para voltar ao menu \n\n")).upper()
        if retorno == "0":
            os.system("cls")
            return()
        else:
            os.system("cls")
            print("Comando invalido")
            continue
            
#==================================
#Função Update/Atualizar informações de livros
def atualizar_livros():
    
    print("\tAtualização de livros\n")
    print("Digite o nome do livro que deseja alterar as informações. \nPara voltar ao menu principal digite [0]\n")
    while True:
        try:
            key = input("Livro: ").title()
            if key == "0":
                os.system("cls")
                return()
            elif key in biblioteca.keys():
                break
            else:
                print("Livro não encontrado, tente novamente")
                continue
        except ValueError:
            print("Valor inválido, digite um valor válido")
            continue
    
    print()
    print("="*9)
    print("\tSecção de alterar informações \nQual informação deseja alterar? (digite apenas números)")
    print("\n[0]- Alterar Nome \n[1]- Alterar Gênero \n[2]- Alterar Autor \n[3]- Alterar valor")

    while True:
        try:
            seccao = int(input("- "))

            if seccao > 3 or seccao < 0:
                print("Secção inválida, digite uma secção válida")
                continue

        except ValueError:
            print("Secção inválida, digite uma secção válida")
            continue

        else:
            break
    
    if seccao == 0: #Alterar Nome
        print()
        print("="*9)
        print(f"Escreva o novo nome do livro {key}: ")
        value = input("- ").title()

        biblioteca[value] = biblioteca[key]
        del biblioteca[key]

    elif seccao == 1: #Alterar Genero
        print()
        print("="*9)
        print(f"Escreva o novo gênero do livro {key}: ")
        value = input("- ").title()
        for i in range(len(biblioteca[key])):
            if i+1 == seccao:
            
                biblioteca[key][i] = value

    elif seccao == 2: #Alterar Autor
        print()
        print("="*9)
        print(f"Escreva o novo autor do livro {key}: ")
        value = input("- ").title()
        for i in range(len(biblioteca[key])):
            
            if i+1 == seccao:
                biblioteca[key][i] = value

    elif seccao == 3: #Alterar Valor
        print()
        print("="*9)
        while True:
            print(f"Escreva o valor novo do livro {key}")
            value = input("- ").title()
            try:
                value = float(value)
                break
            except ValueError:
                os.system("cls")
                print("Insira um valor valido!")
                continue
        
        for i in range(len(biblioteca[key])):
            
            if i+1 == seccao:
                biblioteca[key][i] = value
    
    file = open('dados_' + str(usuario) + '.txt', 'w+', encoding='utf8')

    for livros in biblioteca.keys():
        
        file.write(f'{livros}//{biblioteca[livros][0]}//{biblioteca[livros][1]}//{biblioteca[livros][2]}\n')
    
    file.close()

#==================================
#Função Delete/Remover livro do registro
def remover_livros():
    
    print("\tRemover livros\n")
    print("Qual livro deseja retirar da biblioteca? \nPara voltar ao menu principal digite [0]\n")
    while True:
        try:
            key = input("Livro: ").title()
            if key == "0":
                return()
            elif key in biblioteca.keys():
                break
            elif key not in biblioteca.keys():
                print("Livro não encontrado, tente novamente")
                continue
        except KeyError:
            print("Livro não encontrado, tente novamente")   
            continue
    
    del biblioteca[key]

    file = open('dados_' + str(usuario) + '.txt', 'w+', encoding='utf8')

    for livros in biblioteca.keys():
        
        file.write(f'{livros}//{biblioteca[livros][0]}//{biblioteca[livros][1]}//{biblioteca[livros][2]}\n')
    
    file.close()

#===================
#Funcionalidade extra - Recomendaçõs
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

    while True: 
        gender = input("Digite o genero que deseja recomendações: ").title() #escolhendo o genero para achar recomendações
        
        if gender in recomendacoes:


            print()
            print("="*9)            
            print(f"Recomendações do genero {gender}: \n")

            num = 0
            for item in recomendacoes.get(gender)[0]: #printando as recomendações
                if item not in biblioteca.keys():
                    num+=1
                    print(f"{num}. {item}")


            print()
            print("="*9)            
            continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper() #perguntando se a função será reiniciada
            if continuar == "N":
                break
            elif continuar == "S":
                os.system('cls')
                continue
            else:
                os.system("cls")
                print("Comando invalido, digite S ou N")
                continue
        else:
            os.system('cls')
            print("Genero não encontrado")
            while True:
                
                print()
                print("="*9) 
                continuar = input("Deseja continuar procurando recomendações? [S/N] ").upper() #perguntando se a função será reiniciada
                if continuar == "N":
                    os.system("cls")
                    return()
                elif continuar == "S":
                    os.system('cls')
                    break
                else:
                    os.system("cls")
                    print("Comando invalido, digite S ou N")

#=================
#Função de filtros - menu de filtros
def MenuDeFiltros():
    #Esse boleano checa se o usuário mandou um comando inválido. Se sim, loopa o código e manda uma mensagem de erro
    comando_invalido = False 
    while True:
        os.system ("cls")

        print("Você está no menu de filtros da sua biblioteca particular!")
        if comando_invalido == True:
            os.system ("cls")
            print("ERRO: Comando inválido! Por favor coloque um número de [0 a 3]")

            #Isso garante que o código não vai loopar infinitamente
            comando_invalido = False 

        print ("Qual filtro gostaria de usar na sua pesquisa?\n")
        filtro = input("(Para retornar ao menu principal digite 0)\n\n 1. Gênero\n 2. Autor\n 3. Preço \n\n").lower()

        if filtro == "1":
            FiltroPorGenero()
        elif filtro == '2':
            FiltroPorAutor()
        elif filtro == '3':
            FiltroPorPreco()
        elif filtro == '0':
            os.system("cls")
            #Aqui onde será a volta ao menu principal, mas ele não existe nesse código ainda
            break 
        else:
            comando_invalido = True
            continue


def FiltroPorGenero():
    comando_invalido = False
    while True:
        os.system ("cls")

        print('Você está na sessão de filtro por gênero!')
        genero = input("Por qual gênero você deseja filtrar?\n\n").title() #Input do usuário
        
        #Isso garante que quaiser livros de uma filtração anterior são excluídos para a próxima filtração
        livros_filtrados.clear() 

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
                print("ERRO: Comando inválido! Por favor digite [R] ou [G]")
                comando_invalido = False
            retorno = input('\n[R] = Retornar ao menu de filtros \n[G] = Filtrar por um gênero diferente\n\n').upper()
            if retorno == "R": 
                return()
            elif retorno == "G":
                break
            else:
                comando_invalido = True
                print("Comando invalido")
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
                print("ERRO: Comando inválido! Por favor digite [R] ou [G]")
                comando_invalido = False
            retorno = input('\n[R] = Retornar ao menu de filtros \n[G] = Filtrar por um autor diferente\n\n').upper()
            if retorno == "R": 
                return()
            elif retorno == "G":
                break
            else:
                comando_invalido = True
                print("comando invalido")
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
                            
                            os.system ("cls")
                            print("ERRO: Comando inválido! Por favor digite [R] ou [G]")
                            retorno = input('\n[R] = Retornar ao menu de filtros \n[G] = Filtrar por uma faixa de preço diferente\n\n').upper()
                            if retorno == "R": 
                                return()
                            elif retorno == "G":
                                os.system ("cls")
                                break
                            else:
                                comando_invalido = True
                                print("Comando invalido")
                                continue
                        break
                        

                        
                    elif preco_max >= preco_min: #O correto
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
                                print("ERRO: Comando inválido! Por favor digite [R] ou [G]")
                                comando_invalido = False
                            retorno = input('\n[R] = Retornar ao menu de filtros \n[G] = Filtrar por uma faixa de preço diferente\n\n').upper()
                            if retorno == "R": 
                                return()
                            elif retorno == "G":
                                break
                            else:
                                comando_invalido = True
                                print("Comando invalido")
                                continue
                        break



#--------------------------------------------------------

usuario = input("Informe o nome do usuário: ").title()

login(usuario)

inicio()

logout()