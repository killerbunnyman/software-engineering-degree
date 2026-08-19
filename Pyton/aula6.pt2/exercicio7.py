# 7 - Ler vários produtos (código, descrição, quantidade e valor) para uma venda,
# exibir a lista de produtos e o total da venda.

# Criamos uma lista vazia para armazenar os produtos
produtos = []

# Variável para guardar o total da venda (começa em 0)
total_venda = 0

# Loop infinito (vai rodar até o usuário decidir parar)
while True:
    
    print("\nCadastro de produto")  # \n serve para pular uma linha
    
    # Pedimos o código do produto
    # Se o usuário digitar "sair", o programa será encerrado
    codigo = input("Digite o código do produto (ou 'sair' para encerrar): ")
    
    # .lower() transforma o texto em minúsculo (evita erro com SAIR, Sair, etc.)
    if codigo.lower() == 'sair':
        break  # encerra o loop
    
    # Entrada dos outros dados do produto
    descricao = input("Digite a descrição do produto: ")
    
    # int() converte para número inteiro
    quantidade = int(input("Digite a quantidade: "))
    
    # float() converte para número decimal
    valor = float(input("Digite o valor unitário: "))
    
    # Calcula o subtotal (quantidade × valor)
    subtotal = quantidade * valor
    
    # Soma o subtotal ao total da venda
    # += é um jeito reduzido de somar
    total_venda += subtotal
    
    # Criamos um dicionário para organizar os dados do produto
    produto = {
        'codigo': codigo,
        'descricao': descricao,
        'quantidade': quantidade,
        'valor': valor,
        'subtotal': subtotal
    }
    
    # Adicionamos o produto na lista
    produtos.append(produto)

# Exibimos todos os produtos cadastrados
print("\nLISTA DE PRODUTOS:")

# Percorremos a lista de produtos
for p in produtos:
    
    # f-string permite colocar variáveis dentro do texto usando {}
    print(f"Código: {p['codigo']} | Descrição: {p['descricao']} | "
          f"Qtd: {p['quantidade']} | Valor: {p['valor']} | Subtotal: {p['subtotal']}")

# Mostramos o total final da venda
print("\nTotal da venda:", total_venda)