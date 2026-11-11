saldo = float(5000.20)
senha = 1234
print('Banco do Joe')
print('Seja bem vindo(a)')
senha = int(input('Digite sua senha: '))
op = input('''Escolha a operação:
      Escolha a operação:
      1-Saque
      2-Deposito
      3-Extrato
      ''')
if op == '1':
    saque = float(input('Digite o valor do saque R$: '))
    saldo = saldo - saque
    print('Saque realizado com sucesso!')
    print('Saldo atual:', saldo)
elif op == '2':
    Deposito = float(input('Digite o valor do Depósito R$: '))
    saldo = Deposito + saldo
    print('Depósito realizado com sucesso!')
    print('Saldo atual:', saldo)
elif op == '3':
    print('Extrato da conta')
    print('Saldo atual:', saldo)


    
    
   
            
