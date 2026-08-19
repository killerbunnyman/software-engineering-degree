#Escreva um programa em Python que leia um valor
#representando o gasto realizado por um cliente do restaurante
#ComaBem e visualize o valor total a ser pago, considerando
#os 10% do garçom

print("Restaurante ComaBem")

gasto = float(input("Digite o valor do gasto: R$ "))

garcom = gasto * 0.10
total = gasto + garcom

print(f"Valor da conta: R$ {gasto:.2f}")
print(f"Taxa do garçom (10%): R$ {garcom:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
