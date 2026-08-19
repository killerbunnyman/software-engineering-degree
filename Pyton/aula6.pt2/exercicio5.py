# 5- Temos um grupo de pessoas. Escreva um programa em Python que leia
# o sexo e a altura de cada pessoa, calcule e mostre a altura média
# das mulheres e dos homens separadamente.
# Utilize o comando de repetição que desejar.

# Perguntamos quantas pessoas serão informadas
quantidade = int(input("Quantas pessoas serão cadastradas? "))

# Inicializamos acumuladores e contadores
soma_altura_homens = 0
soma_altura_mulheres = 0

qtd_homens = 0
qtd_mulheres = 0

# Laço para ler os dados
for i in range(quantidade):
    
    print(f"\nPessoa {i+1}")
    
    # Lê o sexo (convertendo para minúsculo para evitar erro)
    sexo = input("Digite o sexo (M/F): ").lower()
    
    # Lê a altura
    altura = float(input("Digite a altura (em metros): "))
    
    # Verifica o sexo e acumula corretamente
    if sexo == 'm':
        soma_altura_homens += altura
        qtd_homens += 1
    elif sexo == 'f':
        soma_altura_mulheres += altura
        qtd_mulheres += 1
    else:
        print("Sexo inválido! Essa pessoa não será considerada.")
    
# Calcula as médias (evitando divisão por zero)
if qtd_homens > 0:
    media_homens = soma_altura_homens / qtd_homens
else:
    media_homens = 0

if qtd_mulheres > 0:
    media_mulheres = soma_altura_mulheres / qtd_mulheres
else:
    media_mulheres = 0

# Exibe os resultados
print("\nRESULTADOS:")
print("Média de altura dos homens:", media_homens)
print("Média de altura das mulheres:", media_mulheres)