'''
Projeto:                 Curso Desenvolvedor Python D.I.O
Desafio:                Aprimorar o sistema bancário, com novas funções de cadastro de clientes e contas
Desenvolvedor:    Edson Massao Matsuuchi
Versão:                 2.0
Data:                     16/11/2025 '''
import datetime
import textwrap
data_atual = datetime.datetime.now()
# tela Menu do cliente
menu = f"""\t==================================================

\t\t\t\t\t\t\t\t\t\t<<< M E N U >>>

\t\t\t\t\t\t\t\t\t[1] Depositar
\t\t\t\t\t\t\t\t\t[2] Sacar
\t\t\t\t\t\t\t\t\t[3] Extrato
\t\t\t\t\t\t\t\t\t[4] Abrir Nova Conta
\t\t\t\t\t\t\t\t\t[5] Exibir Contas Ativas
\t\t\t\t\t\t\t\t\t[6] Sair

\t\t\t\t\t\tSelecione a opção desejada... """

# tela para receber CPF
receber_cpf = f'''\n
\t==================================================
\tBemvindo ao Digital Bank\t\t\t\t\t\t\t\t{data_atual.strftime('%d/%m/%Y %H:%M')}

\t\t\t\t\t\t\t\t\t\t\tInforme o CPF
\t\t\t\t\t\t\t(somente números com 11 dígitos
\t\t\t\t\t\t\t\t\t\t\t\t=> '''

# tela para sugerir cadastro de cliente
vai_cadastrar = '''\n
\t\t\tDeseja realizar cadastro e tornar nosso cliente?
\t\t\t\t\t\t[S] Sim\t\t\t[N] Não\t\t=> '''

# Função de verificação da existência de CPF no cadastro
def filtro_cpf(cpf, clientes):
    str_cpf = str(cpf)
    cliente_filtrado = [cliente for cliente in clientes if cliente['cpf'] == str_cpf]
    return cliente_filtrado[0] if cliente_filtrado else None

# Função de cadastro de novos clientes
def cadastrar_cliente(cpf, clientes):
    data_cadastro = (datetime.datetime.now()).strftime('%d/%m/%Y %H:%M')
    print("\t==================================================")
    print(f"\tData: {data_cadastro}\n")
    c = str(cpf)
    mask_cpf = (c[:3]) + "." + (c[3:6]) + "." + (c[6:9]) + "-" + (c[9:])
    print(f"\t\t\t\t\t\t\t\t\t\t\t\tCPF...: {mask_cpf}")
    nome_cliente        = (input('\t\t\t\t\t\t\tNome Completo...: ')).upper()
    data_nascimento = input('Data de Nascimento (dd/mm/yyyy): ')
    logradouro            = input('\t\t\t\t\t\tLogradouro, número: ')
    complemento       = input('\t\t\t\t\t\t\t\tComplemento...: ')
    bairro                    = input('\t\t\t\t\t\t\t\t\t\t\t\tBairro.: ')
    cidade                  = input('\t\t\t\t\t\t\t\t\t\t\tCidade...: ')
    estado                  = input('\t\t\t\t\t\t\t\t\t\t\tEstado...: ')
    endereco_completo = f"{logradouro} - {complemento} - {bairro} - {cidade.upper()} / {estado.upper()}"
    clientes.append({'nome': nome_cliente, 'cpf': c, 'data_nascimento': data_nascimento, 'endereco': endereco_completo})
    return clientes

# Função para criar novas contas
def criar_conta(cpf, numero_conta, AGENCIA, /,  numero_opera):
    while True:
        senha   = int(input('\n\t\t\tDefina uma senha de 4 digitos: '))
        s_enha = str(senha)
        if len(s_enha) == 4:
            break
        else:
            print("\n\t\t\tSenha inválida. Tente novamente.")
    deposito = float(input('\n\t\t\tInforme valor do primeiro depósito de R$: '))
    print(f"\nAGÊNCIA: {AGENCIA} Nro. da Conta: {numero_conta:>4} Saldo: R${deposito:10.2f}")
    numero_opera += 1
    return {'agencia': AGENCIA, 'cpf': cpf, 'senha': s_enha, 'numero_conta': numero_conta, 'saldo': deposito}, numero_opera

# Função para exibir contas ativas
def exibir_contas(contas_ativas, /, numero_opera):
    print('=' * 50)
    for contas in contas_ativas:
        linha = f"""\tAgência: {contas['agencia']}\tConta: {contas['numero_conta']:>4}\tSaldo: R${contas['saldo']:>10.2f}"""
        print(textwrap.dedent(linha))
    print('=' * 50)
    numero_opera += 1
    return contas_ativas, numero_opera

# Função para operação de depósito de valores em conta
def depositar(saldo, valor, extrato, numero_opera, /):
    if valor <= 0:
        print('\n\t\t\tValor informado inválido!')
    else:
        data_deposito = (datetime.datetime.now()).strftime('%d/%m/%Y %H:%M')
        saldo += valor
        registro = f'{data_deposito}\t\tDeposito\t\tR$ {valor :>10.2f}\n'
        extrato += registro
        numero_opera += 1
        print("\n\t\t\tOperação Realizada com sucesso!!!")
    return saldo, extrato, numero_opera

# Função para operação de saques de valores da conta
def sacar(*, saldo, valor, extrato, saque_limite, numero_saques, numero_opera, LIMITE_SAQUE):
    if valor <= 0:
        print("\n\t\t\tFalha na operação! Valor inválido para saque!")
        return saldo, extrato, numero_saques, numero_opera
    if valor > saldo:
        print("\n\t\t\tFalha na operação! Saldo insuficiente!")
        return saldo, extrato, numero_saques, numero_opera
    if valor > saque_limite:
        print(f"\nFalha na operação! Valor excedeu limite de R$ {saque_limite:6.2f}!")
        return saldo, extrato, numero_saques, numero_opera
    if numero_saques >= LIMITE_SAQUE:
        print("\n\tFalha na operação! Excedeu limite de saques no dia.")
        return saldo, extrato, numero_saques, numero_opera
    data_deposito = (datetime.datetime.now()).strftime('%d/%m/%Y %H:%M')
    saldo -= valor
    registro = f'{data_deposito}\t\tSaque\t\t\tR$ {valor :>10.2f}\n'
    extrato += registro
    numero_saques += 1
    numero_opera += 1
    print("\n\t\t\tOperação Realizada com sucesso!!!")
    return saldo, extrato, numero_saques, numero_opera

# Função para exibir extrato da conta
def exibir_extrato(saldo, /, *, extrato, numero_opera):
    print("\n=================== EXTRATO ======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\t\t\t\t\t\t\t\t\tSaldo Atual...: R${saldo:10.2f}")
    print("===================================================")
    numero_opera += 1
    return saldo, extrato, numero_opera

# definindo as variáveis
saldo = valor = numero_saques = numero_opera = cpf = senha = numero_conta = 0
saque_limite = 500.00
AGENCIA = "0001"
LIMITE_SAQUE = 3
LIMITE_OPERA = 10
clientes = [{"nome": "EDSON",
                    "cpf": "12345678901",
                    "data_nascimento": "17/08/1970",
                    "endereco": "Rua Olinda, 1045 - Sobreloja - Parque Industrial - SÃO JOSE DOS CAMPOS / SP"}]
extrato = ""
contas_ativas = [{
    'agencia': '0001',
    'cpf': '12345678901',
    'senha': '1234',
    'numero_conta': '1',
    'saldo': 0}]

# algoritmo principal
while True: ### Laço Principal ###
    # Solicita CPF e verifica se é válido
    cpf = int(input(textwrap.dedent(receber_cpf)))
    if len(str(cpf)) != 11:
        print("\n\t\t\t\tCPF inválido. Tente novamente.")
    else:
        # Verifica se já é CPF cadastrado ou não
        usuario = filtro_cpf(cpf, clientes)
        if usuario:
            while True: ### Laço do Menu ###
                # Continua operação para cliente confirmado
                while True: ### Laço de erro de seleção das opções ###
                    data_atual = (datetime.datetime.now()).strftime('%d/%m/%Y %H:%M')
                    print(f"\n\tCliente logado: {usuario.get('nome')}\t\t\t\t\t\t\t\t{data_atual}")
                    opcao = int(input(textwrap.dedent(menu)))
                    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
                        print("\n\t\t\tOpção Inválida. Tente novamente.")
                    else:
                        break ### Quebra do laço de erro de seleção das opções ###
                # seletor de opções
                if opcao == 6:
                    print("\n\t\tFim das movimentações. Cliente Deslogado.")
                    break
                while True: ### Laço das opções ###
                    if opcao == 1:
                        if numero_opera >= LIMITE_OPERA:
                            print("Operação bloqueada! Excedeu limite de movimentações")
                            break ### Quebra para retornar ao Menu ###
                        while True: ### Laço para pedido de valor de depósito ###
                            print("\n\t==================================================")
                            valor = float(input("\n\t\t\tInforme o valor do depósito: "))
                            if valor <= 0:
                                print("\n\t\t\tValor informado inválido! Tente novamente.")
                            else:
                                break ### Quebra para sair do pedido de valor de depósito ###
                        saldo, extrato, numero_opera = depositar(saldo, valor, extrato, numero_opera)
                        print(f"\nMovimentações no dia: {numero_opera}\t\t\t\tSaldo: R${saldo:10.2f}")
                        break ### Quebra para retornar ao Menu ###
                    elif opcao == 2:
                        if numero_opera >= LIMITE_OPERA:
                            print("Operação bloqueada! Excedeu limite de movimentações")
                            break ### Quebra para retornar ao Menu ###
                        print("\n\t==================================================")
                        valor = float(input("\n\t\t\tInforme o valor do saque: "))
                        saldo, extrato, numero_saques, numero_opera = sacar(
                            saldo = saldo,
                            valor = valor,
                            extrato = extrato,
                            saque_limite = saque_limite,
                            numero_saques = numero_saques,
                            numero_opera = numero_opera,
                            LIMITE_SAQUE = LIMITE_SAQUE,
                        )
                        print(f"\nMovimentações no dia: {numero_opera}\t\t\t\tSaldo: R${saldo:10.2f}")
                        break ### Quebra para retornar ao Menu ###
                    elif opcao == 3:
                        if numero_opera >= LIMITE_OPERA:
                            print("Operação bloqueada! Excedeu limite de movimentações")
                            break ### Quebra para retornar ao Menu ###
                        saldo, extrato, numero_opera = exibir_extrato(saldo, extrato = extrato, numero_opera = numero_opera)
                        break
                    elif opcao == 4:
                        if numero_opera >= LIMITE_OPERA:
                            print("Operação bloqueada! Excedeu limite de movimentações")
                            break ### Quebra para retornar ao Menu ###
                        numero_conta = len(contas_ativas) + 1
                        conta, numero_opera = criar_conta(cpf, numero_conta, AGENCIA, numero_opera = numero_opera)
                        if conta:
                            contas_ativas.append(conta)
                        print("\n\t\t\tCadastrado com sucesso!!! Vamos reiniciar...")
                        break
                    elif opcao == 5:
                        if numero_opera >= LIMITE_OPERA:
                            print("Operação bloqueada! Excedeu limite de movimentações")
                            break ### Quebra para retornar ao Menu ###
                        contas_ativas, numero_opera = exibir_contas(contas_ativas, numero_opera = numero_opera)
                        break
        if not usuario:
            # Não estando cadastrado, solicita cadastro ou volta para o início do processo
            print("\n\t\t\t\tCPF informado não foi encontrado.")
            novo_cadastro = input(textwrap.dedent(vai_cadastrar))
            if novo_cadastro.upper() == 'S':
                cadastrar = cadastrar_cliente(cpf, clientes)
                numero_conta = len(contas_ativas) + 1
                conta = criar_conta(cpf, numero_conta, AGENCIA)
                if conta:
                    contas_ativas.append(conta)
                print("\n\t\t\tCadastrado com sucesso!!! Vamos reiniciar...")
            else:
                print("\n\t\tTudo bem, finalizando operação e voltando ao início.")