'''
Pela tabela a seguir, mostre a descrição e o preço do produto após a digitação do código pelo usuário. Se o produto não estiver cadastrado, emitir mensagem avisando. OBS: utilizar o Desvio Condicional de Múltipla Escolha.
Tabela vide enunciado (.docx)
'''

codigo = int(input("Digite o código do produto (1 a 5): "))

match codigo:
    case 1:
        print("Caneta - R$1.20")
    case 2:
        print("Lápis - R$0.80")
    case 3:
        print("Caderno - R$4.50")
    case 4:
        print("Borracha - R$1.00")
    case 5:
        print("Régua - R$1.50")
    case _:
        print("Código inválido")
