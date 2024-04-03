menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Inicialização das variáveis
saldo = 0  # Saldo inicial
limite = 500  # Limite de saque
extrato = ""  # Histórico de transações
numero_saques = 0  # Contador de saques
LIMITE_SAQUES = 3  # Número máximo de saques permitidos

# Loop principal para interação com o usuário
while True:

    # Exibição do menu e obtenção da escolha do usuário
    opcao = input(menu)

    # Verifica a opção escolhida pelo usuário
    if opcao == "d":  # Opção para depósito
        valor = float(input("Informe o valor do depósito: "))  # Solicita o valor a ser depositado

        # Verifica se o valor informado é válido
        if valor > 0:
            saldo += valor  # Adiciona o valor ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"  # Registra a transação no extrato

        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro se o valor for inválido

    elif opcao == "s":  # Opção para saque
        valor = float(input("Informe o valor do saque: "))  # Solicita o valor a ser sacado

        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo
        excedeu_limite = valor > limite  # Verifica se o valor do saque excede o limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número máximo de saques foi excedido

        # Verifica se a operação de saque pode ser realizada
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")  # Mensagem de erro se o saldo for insuficiente

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")  # Mensagem de erro se o valor exceder o limite

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")  # Mensagem de erro se o número de saques exceder o limite

        elif valor > 0:
            saldo -= valor  # Subtrai o valor sacado do saldo
            extrato += f"Saque: R$ {valor:.2f}\n"  # Registra a transação no extrato
            numero_saques += 1  # Incrementa o contador de saques

        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro se o valor for inválido

    elif opcao == "e":  # Opção para extrato
        # Exibe o extrato, caso haja movimentações, e o saldo atual
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":  # Opção para sair do programa
        break  # Sai do loop

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro se a opção for inválida
        