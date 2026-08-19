# escreva um codigo que tenha a entrada de quatro numeros e exiba o maior e o menor 

# Entrada dos números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

# Encontrando o maior e o menor
maior = max(n1, n2, n3, n4)
menor = min(n1, n2, n3, n4)

# Exibindo os resultados
print("O maior número é:", maior)
print("O menor número é:", menor)