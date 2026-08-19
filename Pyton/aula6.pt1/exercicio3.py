# 3- Faça um programa em Python que leia um valor n, inteiro e positivo,
# calcule e mostre a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

# Solicitamos ao usuário um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Inicializamos a variável que vai armazenar a soma
soma = 0

# Verificamos se o número é positivo
if n > 0:
    
    # Percorremos de 1 até n
    for i in range(1, n + 1):
        
        # Somamos o valor de 1/i a cada repetição
        soma += 1 / i
    
    # Exibimos o resultado final
    print("O valor da soma S é:", soma)

else:
    # Caso o número não seja positivo
    print("Por favor, digite um número inteiro positivo.")
    