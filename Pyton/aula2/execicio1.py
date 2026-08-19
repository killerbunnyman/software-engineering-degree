#Desenvolva um programa em Python que solicite ao
#usuário os valores dos lados de um retângulo e calcule e
#mostre seu perímetro e sua área.

print("------CALCULADORA DE ÁREA E PERIMETRO------")
val1  = float(input ("qual o valor do primeiro lado? "))
val2 = float (input ("qual o valor do segundo lado? "))

area = (val1 * val2)
perimetro = (2 * val1 + 2 * val2)

print ("o valor da área é :" , area)
print ("e o valor do perimetro é : " , perimetro )