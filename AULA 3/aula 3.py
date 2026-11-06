numero = float(input('Digite um número real:'))
cubo = numero ** 3
print(f'O cubo de {numero} é {cubo}')

print()

fruta1 = 'Maça'
fruta2 = 'Banana'
fruta3 = 'Abacate'
print(fruta1, fruta2, fruta3)

print()
             
num1 = int(input('Didite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))
print(num1, num2)

print()

palavra = 'Python é show'
print(palavra, True)


#formas de concatenação em Python
print(fruta1, fruta2, fruta3)
print(fruta1  + ' '  +  fruta2 +  ' '  + fruta3 )
print(f'{fruta1} {fruta2} {fruta3}')
print('%s %s %s '%(fruta1, fruta2, fruta3))
print('{} {} {} '.format(fruta1,fruta2,fruta3))
