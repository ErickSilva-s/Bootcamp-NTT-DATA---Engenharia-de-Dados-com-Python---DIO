menu = f"""

    ESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR:

                    [d] Depositar
                    [s] Sacar
                    [e] Extrato
                    [q] Sair

"""
saldo = 0
limite = 250
extrato =  ""
numero_saques = 0
LIMITE_SAQUES = 3

def tirar_extrato(): # fiz em função apenas para praticar mais 
    TITULO =  "EXTRATO"
    print(TITULO.center(40,'='))
    print(extrato if extrato else "Ainda não houve nenhuma movimentação")
    print(f"Seu saldo atual: R$ {saldo:.2f}")
    print("".center(40,'='))

while True:

    opcao = input(menu)

    if opcao == "d": #deposito

        valor = float(input("Digite o valor que deseja Depositar:  \n R$: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso.")
        else:
            print("ERRO! Digite um valor válido" )

    elif opcao == "s": #saque

        valor = float(input("Digite o valor que deseja sacar:  \n R$: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("ERRO!  Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("ERRO!  O valor do saque excede o limite.")

        elif excedeu_saques:
            print("ERRO!  Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")

        else:
            print("ERRO!  Digite um valor válido.")

    elif opcao == "e": #extrato
        tirar_extrato()
            
    elif opcao == "q": #sair
        break

    else:
        print("Operação invalida. por favor selecione novamente a operação desejada")
    