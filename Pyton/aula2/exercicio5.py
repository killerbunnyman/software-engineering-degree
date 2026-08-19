#Escreva um programa em Python que leia a cotação do
#dólar (taxa de conversão), leia um valor em dólares e converta
#e mostre o valor equivalente em Reais

#mais uma vez mais do que o solicitado 

print("Conversor de Moedas")

cotacao = float(input("Digite a cotação do dólar: "))

print("1 - Converter Dólar para Real")
print("2 - Converter Real para Dólar")

op = input("Escolha a opção: ")

if op == "1":
    dolar = float(input("Digite o valor em dólares: "))
    real = dolar * cotacao
    print(f"Valor em reais: R$ {real:.2f}")

elif op == "2":
    real = float(input("Digite o valor em reais: "))
    dolar = real / cotacao
    print(f"Valor em dólares: $ {dolar:.2f}")

else:
    print("Opção inválida")