from datetime import datetime

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
limite_trasacoes_diario = 10
contador_transacoes = 0

saldo_conta = 0
extrato = ''

while True:
    print(menu)
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 2:
        saque = float(input('\nValor do saque: R$ '))

        if saque > limite_saque:
            print('\nERRO! O valor do saque excede o limite de R$ 500,00.')
        
        elif saque > saldo_conta:
            print('\nNão é possível realizar o saque por falta de saldo.')

        elif contador_transacoes >= limite_trasacoes_diario:
            print('\nERRO! Você excedeu o limite de 10 transações por dia.')

        else:
            if saque > 0:
                saldo_conta -= saque
                contador_transacoes += 1
                print(f'\nSaque de R$ {saque:.2f} realizado com sucesso!')
                extrato += f'Saque: R$ {saque:.2f} | {datetime.now()}\n'
            else:
                print('\nERRO! Valor inválido.')
            
    elif opcao == 1:
        deposito = float(input('\nValor do depósito: R$ '))

        if contador_transacoes >= limite_trasacoes_diario:
            print('\nERRO! Você excedeu o limite de 10 transações por dia.')

        elif deposito < 0:
            print('\nERRO! Valor inválido.')

        else: 
            saldo_conta += deposito
            contador_transacoes += 1
            extrato += f'Depósito: R$ {deposito:.2f} | {datetime.now()}\n'
            print(f'\nDepósito de R$ {deposito:.2f} realizado com sucesso!')

    elif opcao == 3:
            print('=========================EXTRATO=========================\n')
            print('Não foram realizadas movimentações nesta conta!\n' if not extrato else extrato)
            print(f'Saldo da conta: R$ {saldo_conta:.2f}\n')
            print('=' * 57)
        
    elif opcao == 4:
        break

    else:
        print('\nOpção inválida, por favor selecione novamente a operação desejada.')
