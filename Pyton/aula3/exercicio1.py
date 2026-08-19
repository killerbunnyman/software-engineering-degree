# 1- Faça um programa em Python que calcule e mostre o valor do volume do tronco de
# uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do
# tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e
# calcular a seguinte expressão:

# volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
import math

# Entrada de dados
h = float(input("Digite a altura do tronco da pirâmide (h): "))
Bmenor = float(input("Digite o valor da base menor: "))
Bmaior = float(input("Digite o valor da base maior: "))

# Cálculo do volume
volume = (h/3) * (Bmaior**2 + Bmenor**2 + math.sqrt(Bmaior**2 * Bmenor**2))

# Saída
print("O volume do tronco da pirâmide é:", volume)