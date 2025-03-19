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
    opcao = int(input('\nDigite a opção desejada: '))

    if opcao == 2:
        saque = float(input('\nValor do saque: R$ '))

        if saque > limite_saque:
            print('\nERRO! O valor do saque excede o limite de R$ 500,00.')
        
        elif saque > saldo_conta:
            print('\nNão é possível realizar o saque por falta de saldo.')

        elif contador_saque > limite_saque_diario:
            print('ERRO! Você excedeu o limite de saques de 3 vezes/dia.')

        elif contador_saque >= limite_saque_diario:
            print('\nERRO! Você excedeu o limite de saques de 3 vezes/dia.')

        else:
            if saque > 0:
                saldo_conta -= saque
                contador_saque += 1
                print(f'\nSaque de R$ {saque:.2f} realizado com sucesso!')
                extrato += f'Saque: R$ {saque:.2f}\n'
            else:
                print('\nERRO! Valor inválido.')
            
    elif opcao == 1:
        deposito = float(input('\nValor do depósito: R$ '))

        if deposito > 0:
            saldo_conta += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
            print(f'\nDepósito de R$ {deposito:.2f} realizado com sucesso!')

        else:
            print('\nERRO! Valor inválido.')
    
    elif opcao == 3:

        if not extrato:
            print('====================EXTRATO====================')
            print('Não foram realizadas movimentações nesta conta!')
            print('=' * 47)
        
        else:
            print('===========EXTRATO===========')
            print(f'{extrato}\nSaldo da conta: R$ {saldo_conta:.2f}')
            print('=' * 30)
        
            print('====================EXTRATO====================\n')
            print('Não foram realizadas movimentações nesta conta!\n'if not extrato else extrato)
            print(f'Saldo da conta: R$ {saldo_conta:.2f}\n')
            print('=' * 47)
        
    elif opcao == 4:
        break

    else:
        print('\nOpção inválida, por favor selecione novamente a operação desejada.')
