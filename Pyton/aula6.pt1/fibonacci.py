# Exercício extra:
# Fazer um código em Python que peça um número ao usuário
# e mostre a quantidade de números da sequência de Fibonacci solicitada.
# Exemplo: se o usuário pedir 6 → saída: 0, 1, 1, 2, 3, 5

# Pedimos ao usuário quantos números ele quer ver
n = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

# Verificamos se o número é positivo
if n > 0:
    
    # Inicializamos os dois primeiros números da sequência
    a = 0
    b = 1
    
    print("Sequência de Fibonacci:")
    
    # Laço para gerar os n primeiros números
    for i in range(n):
        
        # Imprime o número atual
        print(a)
        
        # Atualiza os valores:
        # o próximo número é a soma dos dois anteriores
        proximo = a + b
        
        # Atualizamos as variáveis para continuar a sequência
        a = b
        b = proximo

else:
    print("Por favor, digite um número inteiro positivo.")