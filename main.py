menu = '''

------------------
       MENU
------------------
[1] -> Depositar
[2] -> Sacar
[3] -> Extrato
[4] -> Sair

'''

limite_saque = 500
limite_saque_diario = 3
contador_saque = 0
saldo_conta = 0
extrato = ''

while True:
    print(menu)
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 2:
        saque = float(input('Valor do saque: R$ '))

        if saque > limite_saque:
            print('ERRO! O valor do saque excede o limite de R$ 500,00.')
        
        elif saque > saldo_conta:
            print('Não é possível realizar o saque por falta de saldo.')

        elif contador_saque > limite_saque_diario:
            print('ERRO! Você excedeu o limite de saques de 3 vezes/dia.')

        else:
            saldo_conta -= saque
            contador_saque += 1
            print(f'Saque de R$ {saque:.2f} realizado com sucesso!')
            extrato += f'Saque: R$ {saque:.2f}\n'
            
    elif opcao == 1:
        deposito = float(input('Valor do depósito: R$ '))
        saldo_conta += deposito
        extrato += f'Depósito: R$ {deposito:.2f}\n'
        print(f'Depósito de R$ {deposito:.2f} realizado com sucesso!')
    
    elif opcao == 3:

        if not extrato:
            print('====================EXTRATO====================')
            print('Não foram realizadas movimentações nesta conta!')
            print('=' * 47)
        
        else:
            print('===========EXTRATO===========')
            print(f'{extrato}\nSaldo da conta: R$ {saldo_conta:.2f}')
            print('=' * 30)
        
    elif opcao == 4:
        break

    else:
        print('Opção inválida, por favor selecione novamente a operação desejada.')
