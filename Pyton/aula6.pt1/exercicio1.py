# 1- Faça um programa em Python que imprima os números pares entre 0 e 100

# Usamos um laço for para percorrer os números de 0 até 100
# A função range(0, 101) gera números de 0 até 100 (o 101 não é incluído)

for numero in range(0, 101):
    
    # Verificamos se o número é par
    # Um número é par quando o resto da divisão por 2 é igual a 0
    if numero % 2 == 0:
        
        # Se for par, imprimimos o número
        print(numero)