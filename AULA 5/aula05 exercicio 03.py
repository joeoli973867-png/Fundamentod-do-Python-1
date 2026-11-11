# Exercício 3: Verifique se o usuário é maior de idade e pode entrar no show, escreva
# um programa que peça a usuário a idade e decida se ele pode entrar no show.
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você pode entrar no Show! ')
else:
    print('Você não pode entrar no Show! ')