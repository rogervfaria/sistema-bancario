from datetime import datetime


def menu():
    menu = '''
    ------------------
           MENU
    ------------------
    [1] -> Depositar
    [2] -> Sacar
    [3] -> Extrato
    [4] -> Novo usuário
    [5] -> Nova conta
    [6] -> Listar contas
    [7] -> Sair
    '''

    return input(f'{menu}\nDigite a opção desejada: ')


def depositar(valor, saldo, extrato, contador_transacoes, limite_transacoes, /):
    if contador_transacoes >= limite_transacoes:
        print('\nERRO! Você excedeu o limite de 10 transações por dia.')

    elif valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f} | {datetime.now()}\n'
        contador_transacoes += 1
        print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso!')

    else:
        print('\nERRO! Valor inválido.')

    return saldo, extrato, contador_transacoes
    

def sacar(*, valor, saldo, extrato, limite_saque, limite_transacoes, contador_transacoes):
    if valor > limite_saque:
        print('\nERRO! O valor do saque excede o limite de R$ 500,00.')

    elif contador_transacoes >= limite_transacoes:
        print('\nERRO! Você excedeu o limite de 10 transações por dia.')

    elif valor > saldo:
        print('\nNão é possível realizar o saque por falta de saldo.')

    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f} | {datetime.now()}\n'
        contador_transacoes += 1
        print(f'\nSaque de R$ {valor:.2f} realizado com sucesso!')

    return saldo, extrato, contador_transacoes


def exibir_extrato(saldo, /, *, extrato):
    print('\n=========================EXTRATO=========================\n')
    print('Não foram realizadas movimentações nesta conta!\n' if not extrato else extrato)
    print(f'Saldo da conta: R$ {saldo:.2f}\n')
    print('=' * 57)


def criar_usuario(usuarios):
    cpf = input('\nCPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário cadastrado com esse CPF!')
    
    else:
        nome = input('Nome completo: ')
        data_nascimento = input('Data de nascimento (dd-mm-aaaa): ')
        endereco = input('Endereço ((logradouro, nº - bairro - cidade/sigla estado)): ')
        print('\nUsuário cadastrado com sucesso!')
    
        usuarios.append(
                    {'Nome completo': nome, 
                    'Data de nascimento': data_nascimento,
                    'CPF': cpf,
                    'Endereço': endereco}
        )


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['CPF'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input('\nCPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        contas.append({'Agência': agencia, 'Conta': numero_conta, 'Usuário': usuario})

    else:
        print('\nUsuário não encontrado! Por favor, crie um usuário antes.')


def listar_contas(contas, agencia):
    print('\n====================CONTAS====================')
    for conta in contas:
        print(f'''
                Agência: {agencia}
                Conta: {conta['Conta']}
                Titular: {conta['Usuário']['Nome completo']}\n
            -------------------------------------------------------
        ''')


def main():
    limite_saque = 500
    limite_transacoes = 10
    contador_trasacoes = 0
    saldo = 0
    extrato = ''
    usuarios = []
    contas = []
    agencia = '0001'

    while True:
        opcao = int(menu())

        if opcao == 1:
            valor = float(input('Valor do depósito: R$ '))
            saldo, extrato, contador_trasacoes = depositar(
                valor, 
                saldo, 
                extrato, 
                contador_trasacoes, 
                limite_transacoes
            )

        elif opcao == 2:
            valor = float(input('Valor do saque: R$ '))
            saldo, extrato, contador_trasacoes = sacar(
                valor=valor, 
                saldo=saldo,
                extrato=extrato,
                limite_saque=limite_saque,
                limite_transacoes=limite_transacoes,
                contador_transacoes=contador_trasacoes
            )

        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(agencia, numero_conta, usuarios, contas)

        elif opcao == 6:
            listar_contas(contas, agencia)

        elif opcao == 7:
            break
  
        else:
            print('Opção inválida! Tente novamente.')


main()
