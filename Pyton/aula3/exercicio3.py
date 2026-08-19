# 3- Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,
# meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.
# Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

# Entrada de dados
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite os meses: "))
dias = int(input("Digite os dias: "))

# Cálculo
idade_dias = (anos * 365) + (meses * 30) + dias

# Saída
print("Sua idade em dias é:", idade_dias)