'''
Baseado em um número real X (float) digitado pelo usuário, utilize o desvio condicional de múltipla escolha e faça as seguintes operações:



Opcao = 1: adicione 5 ao valor de X e exiba na tela.

Opcao = 2: subtraia 4 ao valor de X e exiba na tela.

Opcao = 3: dobre o valor de X e exiba na tela.
'''

numero_X = float(input("Digite um número real: "))
opcao = int(input("Digite uma opção (1 a 3): "))

match opcao:
    case 1:
        numero_X = numero_X + 5
    case 2:
        numero_X = numero_X - 4
    case 3:
        numero_X = numero_X * 2
    case _:
        print("Opção inválida")

print(f"O número X é {numero_X:.2f}")

