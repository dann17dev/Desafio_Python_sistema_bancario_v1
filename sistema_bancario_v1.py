#desafio 

#Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja 
#modernizar suas operações e para isso escolheu a linguagem "Python"
#Devemos implementar 03 operações (Depósito, Saque e Extrato).

#Operação de deposito 

#Operação Saque

#Operação Extrato 

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Limite de Saque por Transação
[5] Limite de Saques Diários Restantes
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Mensagem de boas-vindas
nome = "Fulano"
print(f"Bem-vindo ao banco XPTO, {nome}!")

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe qual será o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado do depósito é inválido.")

    elif opcao == "2":
        if numero_saques >= LIMITE_SAQUES:
            print("Você não possui saques disponíveis para hoje. Tente novamente amanhã.")
        else:
            valor = float(input("Informe qual será o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            if excedeu_saldo:
                print("Operação falhou! Você não possui saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite permitido por transação.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print(f"O limite de saque por transação é R$ {limite:.2f}.")

    elif opcao == "5":
        saques_restantes = LIMITE_SAQUES - numero_saques
        print(f"Limite de saques diários restantes: {saques_restantes}.")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

mensagem = f"""
############## Agradecimento ##############
Olá {nome}, Espero que volte logo!
É um prazer saber que faz parte 
do banco XPTO, agradecemos a confiança!
=========================================
"""

print(mensagem)
