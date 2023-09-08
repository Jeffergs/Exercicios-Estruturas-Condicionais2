'''
Crie um menu com as 4 operações matemáticas (soma, subtração, multiplicação e divisão) que devem ser executadas com 2 números reais (float) de acordo com a escolha (opção) do usuário:

Opcao = 1: soma dos 2 números.

Opcao = 2: subtração dos 2 números.

Opcao = 3: multiplicação dos 2 números.

Opcao = 4: divisão dos 2 números.
'''

num1 = float(input("Digite o primeiro número real: "))
num2 = float(input("Digite o segundo número real: "))

opcao = int(input("Digite uma opção (1 a 4): "))

match opcao:
    case 1:
        soma = num1 + num2
        print(f"Soma: {soma:.2f}")
    case 2:
        sub = num1 - num2
        print(f"Subtração: {sub:.2f}")
    case 3:
        mult = num1 * num2
        print(f"Multiplicação: {mult:.2f}")
    case 4:
        div = num1 / num2
        print(f"Divisão: {div:.2f}")
    case _:
        print("Opção inválida")
