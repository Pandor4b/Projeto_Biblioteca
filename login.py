import os
os.system("cls")


def login(usuario):

    usuario = input("Informe o nome do usuário: ")

    usuario = open('dados_' + str(usuario) + '.txt', 'a', encoding='utf-8')

    return

login('usuario')

def logout():
    saida = input("Deseja fechar o aplicativo? \n[S] para Sim\n[N] para Não \n")
    saida.capitalize()
    os.system('')
    if saida == 'N':
        menu()
    if saida =='S':
        return quit
    
logout()



    




