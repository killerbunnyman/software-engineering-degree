# 6 - Ler uma quantidade indeterminada de alunos com as seguintes informações:
# RGM, NOME, Sexo e Média.
# Calcular a média da sala, exibir a média da sala, maior nota,
# menor nota e a média por sexo.

# Dicionário para armazenar dados por sexo (evita vários if)
dados = {
    'm': {'soma': 0, 'qtd': 0},
    'f': {'soma': 0, 'qtd': 0}
}

# Lista para armazenar todas as médias (facilita cálculos)
medias = []

while True:
    
    print("\nCadastro de aluno")
    
    # Entrada com condição de parada
    rgm = input("Digite o RGM (ou 'sair' para encerrar): ")
    if rgm.lower() == 'sair':
        break
    
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo (M/F): ").lower()
    media = float(input("Digite a média do aluno: "))
    
    # Armazena a média na lista
    medias.append(media)
    
    # Atualiza dados por sexo (sem precisar de vários if/elif)
    if sexo in dados:
        dados[sexo]['soma'] += media
        dados[sexo]['qtd'] += 1

# Cálculos gerais usando funções prontas do Python
media_sala = sum(medias) / len(medias) if medias else 0
maior_nota = max(medias) if medias else 0
menor_nota = min(medias) if medias else 0

# Médias por sexo usando operador ternário
media_masculino = dados['m']['soma'] / dados['m']['qtd'] if dados['m']['qtd'] else 0
media_feminino = dados['f']['soma'] / dados['f']['qtd'] if dados['f']['qtd'] else 0

# Resultados
print("\nRESULTADOS:")
print("Média da sala:", media_sala)
print("Maior nota:", maior_nota)
print("Menor nota:", menor_nota)
print("Média dos homens:", media_masculino)
print("Média das mulheres:", media_feminino)
