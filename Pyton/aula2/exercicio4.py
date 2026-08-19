#Escreva um programa em Python que calcule as duas
#raízes de uma equação de 2º grau ax²+bx+c, conhecendo os
#valores dos coeficientes da mesma (a, b, c). Suponha que as
#raízes são reais. Lembre-se que para calcular as duas raízes:
import math
print ("calculadora de equação do segundo grau ")

a = float (input (" qual o valor de a?" ))

b = float (input (" qual o valor de b?" ))

c = float (input (" qual o valor de c? "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais")

else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("As raízes da equação são:")
    print("x1 =", x1)
    print("x2 =", x2)