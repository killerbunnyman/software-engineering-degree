# agora com entrada de 5 numeros

#Detalhe que ele pediu apenas para mostrar o maior mas eu quis mostrar o menor tambem

# Entrada dos números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

# Encontrando o maior e o menor
maior = max(n1, n2, n3, n4, n5)
menor = min(n1, n2, n3, n4, n5)

# Mostrando o resultado
print("O maior número é:", maior)
print("O menor número é:", menor)

