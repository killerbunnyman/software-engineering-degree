# 3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
# Crie uma programa que permita digitar o nome do produto e valor da compra, e
# imprimindo o nome do produto e o valor da venda.
# Valor de compra Valor de venda
# valor < R$10,00 lucro de 70%
# R$ 10,00 <= valor < R$ 30,00 lucro de 50%
# R$ 30,00 <= valor < R$ 50,00 lucro de 40%
# valor >= R$50,00 lucro de 30%

produto = input("Digite o nome do produto: ")
valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra < 10:
    valor_venda = valor_compra * 1.70

elif valor_compra >= 10 and valor_compra < 30:
    valor_venda = valor_compra * 1.50

elif valor_compra >= 30 and valor_compra < 50:
    valor_venda = valor_compra * 1.40

else:
    valor_venda = valor_compra * 1.30

print("Produto:", produto)
print("Valor de venda: R$", valor_venda)