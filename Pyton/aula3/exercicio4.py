# 4- Escreva um programa em Python para calcular o valor de uma prestação em atraso
# (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de
# multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o
# valor da prestação atualizado, sabendo que:
# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

# Entrada de dados
valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem de multa por dia (%): "))
qtdeDias = int(input("Digite a quantidade de dias de atraso: "))

# Cálculo
prestacao = valorPrestacao + (valorPrestacao * (multa / 100) * qtdeDias)

# Saída
print("O valor da prestação atualizada é:", prestacao)