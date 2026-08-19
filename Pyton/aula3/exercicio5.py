# 5- Faça uma programa em Python que peça do usuário um valor em graus para um
# ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,
# cosseno e tangente deste ângulo. 

import math

# Entrada de dados
graus = float(input("Digite o valor do ângulo em graus: "))

# Conversão para radianos
radianos = math.radians(graus)

# Cálculo das funções trigonométricas
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Saída
print("Ângulo em radianos:", radianos)
print("Seno:", seno)
print("Cosseno:", cosseno)
print("Tangente:", tangente)
