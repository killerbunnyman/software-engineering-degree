# 4- Escreva um algoritmo que leia um grupo de valores reais e determine
# quantos valores são positivos e quantos são negativos.
# Determine, também, qual é o menor desses valores.
# Utilize o comando de repetição que desejar.

# Vamos pedir primeiro quantos números o usuário quer digitar
quantidade = int(input("Quantos valores você deseja informar? "))

# Inicializamos os contadores
positivos = 0
negativos = 0

# Inicializamos o menor valor como None (ainda não definido)
menor = None

# Laço de repetição para ler os valores
for i in range(quantidade):
    
    # Lê um valor real (float)
    valor = float(input(f"Digite o {i+1}º valor: "))
    
    # Verifica se é positivo ou negativo
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    
    # Verifica o menor valor
    # Se for o primeiro número ou se o valor atual for menor que o menor registrado
    if menor is None or valor < menor:
        menor = valor

# Exibe os resultados
print("Quantidade de valores positivos:", positivos)
print("Quantidade de valores negativos:", negativos)
print("Menor valor digitado:", menor)