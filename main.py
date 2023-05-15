print(" /*/ " * 30)
print("Banco do Negro".center(150))
print(" /*/ " * 30)

print(" Selecione uma opção")
menu = """

[d] Depositar

[s] Sacar

[e] extrato

[q] sair 

=> """

saldo = 500

limite = 500

extrato = ''

numero_saques = 3

LIMITE_SAQUES = 500

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:

            saldo += valor

            extrato += f"Depósito: R$ + {valor:.2f}\n"

            input("Deposito.s realizado com sucesso!")

        else:

            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "s":

        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")
        elif excedeu_saques:
            print("Operação falhou! O valor excedeu o limite de saques.")
        elif excedeu_limite:
            print("Operação Falhou! numero maximo de saques excedido.")

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ + {valor:.2f}\n"
            numero_saques += 1

            input(f"Saque, Autorizado. Aguarde o dinheiro na boca do caixa!\n"
                  f"Aperte qualquer tecla para sair")

        else:
            print("Operação Falhou! Numero informado é invalido!")

    elif opcao == "e":

        print("\n----------------- EXTRATO ---------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("=======================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")