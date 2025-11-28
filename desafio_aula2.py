# DESAFIOS AULA 2

# Desafio 1 – Controle de estoque com while
# Desafio 2 – Média de temperaturas semanais
# Desafio 3 – Simulador de caixa eletrônico


# DESAFIO 1 #
def desafio_1():
    print("\n=== DESAFIO 1: CONTROLE DE ESTOQUE ===")

    estoque = int(input("Digite a quantidade inicial de produtos em estoque: "))

    while True:
        acao = input("\nDigite 'vender', 'repor' ou 'sair': ").lower()

        if acao == "sair":
            break

        elif acao == "vender":
            qtd = int(input("Quantidade vendida: "))
            estoque -= qtd
            print(f"Venda registrada! Estoque atual: {estoque}")

        elif acao == "repor":
            qtd = int(input("Quantidade adicionada: "))
            estoque += qtd
            print(f"Reposição concluída! Estoque atual: {estoque}")

        else:
            print("Opção inválida. Tente novamente.")

    print(f"\nSaldo final de produtos: {estoque}")


# DESAFIO 2 #
def desafio_2():
    print("\n=== DESAFIO 2: TEMPERATURAS SEMANAIS ===")

    temperaturas = []

    for dia in range(1, 8):
        temp = float(input(f"Digite a temperatura do dia {dia}: "))
        temperaturas.append(temp)

    media = sum(temperaturas) / 7
    maior = max(temperaturas)
    menor = min(temperaturas)

    print(f"\n📌 Média semanal: {media:.2f}°C")
    print(f"🔥 Maior temperatura: {maior}°C")
    print(f"❄ Menor temperatura: {menor}°C")


# DESAFIO 3 #
def desafio_3():
    print("\n=== DESAFIO 3: CAIXA ELETRÔNICO ===")

    saque = int(input("Digite o valor do saque: R$ "))

    notas100 = saque // 100
    saque %= 100

    notas50 = saque // 50
    saque %= 50

    notas20 = saque // 20
    saque %= 20

    notas10 = saque // 10
    saque %= 10

    print("\nNotas entregues:")

    if notas100 > 0: print(f"{notas100} nota(s) de R$100")
    if notas50 > 0:  print(f"{notas50} nota(s) de R$50")
    if notas20 > 0:  print(f"{notas20} nota(s) de R$20")
    if notas10 > 0:  print(f"{notas10} nota(s) de R$10")

    if saque > 0:
        print(f"Valor restante não pode ser sacado com notas disponíveis: R${saque}")

print("\n=== MENU DE DESAFIOS ===")
print("1 - Controle de Estoque")
print("2 - Média de Temperaturas")
print("3 - Caixa Eletrônico")

opcao = input("\nEscolha o desafio (1/2/3): ")

if opcao == "1":
    desafio_1()
elif opcao == "2":
    desafio_2()
elif opcao == "3":
    desafio_3()
else:
    print("Opção inválida.")
