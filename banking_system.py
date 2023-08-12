menu = """

    [d] Depositar Valor
    [s] Sacar Valor
    [e] Consultar Extrato
    [x] Encerrar Operação

    => """

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
        
        else:
            print("Operação falhou! Valor informado inválido")
    
    elif opcao == "s":
        print("Saque")

    elif  opcao == "e":
        print("Extrato")

    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")