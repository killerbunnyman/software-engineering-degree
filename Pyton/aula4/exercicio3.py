# 3- Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar
# o valor da compra considerando o desconto, conforme descrito abaixo:
# para compras acima de R$ 200 a loja dá um desconto de 20%
# para as abaixo disso não tem desconto, mostre o valor da compra.

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 200:
    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
else:
    valor_final = valor_compra

print(f"O valor final da compra é: R$ {valor_final:.2f}")
