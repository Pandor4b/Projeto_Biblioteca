import os
os.system('cls')

def dados():
    info = open('dados.txt', 'a')
    info.write(input())
    return ('')
print(dados())


#armazenar informações do usuário no dicionario e as trata no for
#criar lista apara cada pessoa
#cada pessoa vira um dict com seus dados