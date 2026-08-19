# Escreva um programa em Python que obtenha uma
# temperatura em graus Celsius, calcule e mostre a respectiva
# temperatura nas escalas Fahrenheit e Kelvin.

#gostei desse

print("Conversor de Temperatura")

print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")

op = input("Escolha uma opção: ")

temp = float(input("Digite a temperatura: "))

if op == "1":
    resultado = (temp * 9/5) + 32
    print(f"Resultado: {resultado:.2f} °F")

elif op == "2":
    resultado = temp + 273.15
    print(f"Resultado: {resultado:.2f} K")

elif op == "3":
    resultado = (temp - 32) * 5/9
    print(f"Resultado: {resultado:.2f} °C")

elif op == "4":
    resultado = (temp - 32) * 5/9 + 273.15
    print(f"Resultado: {resultado:.2f} K")

elif op == "5":
    resultado = temp - 273.15
    print(f"Resultado: {resultado:.2f} °C")

elif op == "6":
    resultado = (temp - 273.15) * 9/5 + 32
    print(f"Resultado: {resultado:.2f} °F")

else:
    print("Opção inválida")