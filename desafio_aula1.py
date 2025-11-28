"""
1) Pergunta nome, idade e cidade e exibe mensagem completa.
2) Pergunta um número e informa se é positivo, negativo ou zero.
3) Pergunta peso e altura, calcula o IMC e classifica: Abaixo do peso, Normal, Sobrepeso, Obesidade.
"""

def atividade_1():
    nome = input('Digite seu nome: ').strip()
    while not nome:
        nome = input('Nome inválido. Digite seu nome: ').strip()

    idade_input = input('Digite sua idade (apenas números): ').strip()
    while not idade_input.isdigit():
        idade_input = input('Idade inválida. Digite sua idade (apenas números): ').strip()
    idade = int(idade_input)

    cidade = input('Digite sua cidade: ').strip()
    while not cidade:
        cidade = input('Cidade inválida. Digite sua cidade: ').strip()

    print(f"\nOlá, {nome}! Você tem {idade} anos e mora em {cidade}.\n")


def atividade_2():
    while True:
        num_str = input('Digite um número (positivo, negativo ou zero): ').strip()
        try:
            numero = float(num_str.replace(',', '.'))  # aceita vírgula ou ponto
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')

    if numero > 0:
        print(f'O número {numero} é positivo.')
    elif numero < 0:
        print(f'O número {numero} é negativo.')
    else:
        print('O número é zero.')


def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Normal'
    elif imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'


def atividade_3():
    print('\nCálculo do IMC (Índice de Massa Corporal)')
    while True:
        peso_str = input('Digite seu peso em kg: ').strip()
        try:
            peso = float(peso_str.replace(',', '.'))
            if peso <= 0:
                print('Peso deve ser maior que zero. Tente novamente.')
                continue
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')

    while True:
        alt_str = input('Digite sua altura em metros (ex: 1.75): ').strip()
        try:
            altura = float(alt_str.replace(',', '.'))
            if altura <= 0:
                print('Altura deve ser maior que zero. Tente novamente.')
                continue
            break
        except ValueError:
            print('Entrada inválida. Tente novamente.')

    imc = peso / (altura ** 2)
    classificacao = classificar_imc(imc)
    print(f'\nSeu IMC é {imc:.2f} — {classificacao}.\n')


def main():
    print('--- Atividades: Nome/Idade/Cidade, Número, IMC ---\n')
    atividade_1()
    atividade_2()
    atividade_3()
hasattr


if __name__ == '__main__':
    main()
