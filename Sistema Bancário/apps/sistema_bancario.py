'''
    Projeto:        Curso Desenvolvedor Python D.I.O
    Desafio:        Criar sistema simples de movimentação de conta corrente de um banco
    Desenvolvedor:  Edson Massao Matsuuchi
    Versão:         1.0
    Data:           10/11/2025
'''
import datetime

# declarando as variáveis
data_sistema = datetime.datetime.now()
saldo_atual  = 0
saque_limite = 500
limite_saque = 3
regi_extrato = ''
conta_saques = 0
menu = f'''
******************** M E N U ********************
                           Data: {data_sistema.strftime('%d/%m/%Y %H:%M')}

                [1] Depositar
                [2] Sacar
                [3] Exibir Extrato
                [4] Sair do sistema

        Digite a opção desejada: '''

def depositar():
    global saldo_atual, data_sistema, regi_extrato
    validade = False
    while validade == False:
        valor_deposito = float(input('\n    Informe o valor do deposito: R$'))
        if valor_deposito <= 0:
            print('\n   Falha na operação! Valor inválido! Tente novamente.')
        else:
            saldo_atual += valor_deposito
            regi_extrato += f"Data: {data_sistema.strftime('%d/%m/%Y %H:%M')}...Depósito....: R${valor_deposito:8.2f}\n"
            print(f'\n  Deposito de R${valor_deposito:8.2f} realizado com sucesso!!!')
            validade = True

def sacar():
    global saldo_atual, data_sistema, regi_extrato, saque_limite, conta_saques, limite_saque
    validade = False
    while validade == False:
        valor_saque = float(input('\n   Informe o valor do saque: R$'))
        if valor_saque <= 0:
            print('\n   Falha na Operação! Valor informado é inválido! Tente novamente.')
        elif conta_saques >= limite_saque:
            print(f'\n  Falha na Operação! Excedeu limite de {limite_saque} saques diário!')
            validade = True
        elif valor_saque > saldo_atual:
            print('\n   Falha na Operação! Saldo Insuficiente!')
            validade = True
        elif valor_saque > saque_limite:
            print('\n   Falha na Operação! Valor excede o limite de saque! Tente novamente.')
        else:
            saldo_atual -= valor_saque
            conta_saques += 1
            regi_extrato += f"Data: {data_sistema.strftime('%d/%m/%Y %H:%M')}...Saque.......: R${valor_saque:8.2f}\n"
            print(f'\n  Saque de R${valor_saque:8.2f} realizado com sucesso!!!')
            validade = True

def exibir():
    global saldo_atual, data_sistema, regi_extrato
    print('\n***************** E X T R A T O *****************')
    print('\n              +++++  Não ha movimentações.  +++++' if not regi_extrato else regi_extrato)
    print(f'\n                         Saldo atual: R$ {saldo_atual:8.2f}')
    print('*************************************************')

while True:
    opcao = input(menu)
    print('*************************************************')
    if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
        print('\n       Opção inválida! Tente novamente.')

    if opcao == '1':
        depositar()

    if opcao == '2':
        sacar()

    if opcao == '3':
        exibir()

    if opcao == '4':
        print('Saindo do sistema...')
        break