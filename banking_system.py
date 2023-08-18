menu = """
    ESCOLHA UMA OPERAÇÃO:
    Insira a letra correspondente.

    [d] Depositar Valor
    [s] Sacar Valor
    [e] Consultar Extrato
    [x] Encerrar Operação

    >>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!\n")
        
        else:
            print("Operação falhou! Valor informado inválido")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo suficiente.\n")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite de saque único.\n")

        elif excedeu_saques:
            print("Falha na operação! Número máximo de saque diário excedido.\n")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado! Recolha seu dinheiro.\n")

        else:
            print("Falha na operação! O valor informado é inválido.\n")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============\n")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================\n")

    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
