QUANTIDADE_LIMITE_DE_SAQUE = 3
VALOR_LIMITE_DE_SAQUE = 500.00

extrato = []
saldo = 0.00
saques_realizados = 0

def depositar():

    global extrato
    global saldo

    print('\nOperação de Depósito\n')
    valor = float(input('Digite o valor que deseja depositar: R$ '))

    if valor > 0:
        saldo += valor
        extrato.append(['depósito', valor])
        print('Depósito realiado com sucesso.')

    else:
        print('Valor inválido para depósito.')

def sacar():

    global extrato
    global saldo
    global saques_realizados

    print('\nOperação de Saque\n')

    if saldo > 0 and saques_realizados < QUANTIDADE_LIMITE_DE_SAQUE:

        valor = float(input('Digite o valor que deseja sacar: R$ '))

        if valor <= saldo and valor <= VALOR_LIMITE_DE_SAQUE and valor > 0:
            saldo -= valor
            saques_realizados += 1
            extrato.append(['saque', valor])
            print('Saque realizado com sucesso.')

        elif valor > VALOR_LIMITE_DE_SAQUE:
            print('Valor acima do limite de segurança permitido.')

        elif valor > saldo:
            print('Operação de saque cancelada por insuficiência de saldo.')

        else:
            print('Operação cancelada.')

    elif saldo == 0:
        print('Operação de saque indisponível por falta de saldo.')

    else: 
        print('Limite diário de saque atingido.')

def emitir_extrato():

    global extrato
    global saldo
    global saques_realizados

    print('\n******* EXTRATO *******\n')

    for item in extrato:
        print(f'{item[0].upper() + (" " * (10 - len(item[0])))} R$ {item[1]:.2f} {"(+)" if item[0].lower() == "depósito" else "(-)"}')
    
    print(f'\nSALDO:{" " * 4} R$ {saldo:.2f} (+)')
        
    print('\n***********************\n')

def menu():

    while True:

        print('******* MENU BANCÁRIO *******\n')
        print('1: DEPÓSITO')
        print('2: SAQUE')
        print('3: EXTRATO')
        print('9: SAIR')
        print('\n*****************************\n')
        opcao = input('Digite o número da operação desejada: ').strip()

        if opcao == '1':
            depositar()
        
        elif opcao == '2':
            sacar()

        elif opcao == '3':
            emitir_extrato()

        elif opcao == '9':
            break

        else: 
            print('Opção inválida.')
    
        print()

    print('Aplicação encerrada com sucesso.')

if __name__ == '__main__':
    menu()