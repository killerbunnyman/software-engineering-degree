# 2- Faça um programa em Python que imprima os números de 1 a 50 de 1 em 1
# e de 52 a 100 de 2 em 2.

# Primeiro: imprimir de 1 até 50, de 1 em 1
# range(1, 51) -> começa no 1 e vai até 50 (51 não entra)
for numero in range(1, 51):
    print(numero)

# Segundo: imprimir de 52 até 100, de 2 em 2
# range(52, 101, 2) -> começa no 52, vai até 100, pulando de 2 em 2
for numero in range(52, 101, 2):
    print(numero)