# 2- Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de
# horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a
# seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um
# caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$
# 37,50

turno = input("Digite seu turno de trabalho (N para noturno ou outro para diurno): ")
horas = float(input("Digite a quantidade de horas trabalhadas: "))

if turno == 'N' or turno == 'n':
    valor_hora = 45.00
else:
    valor_hora = 37.50

salario = horas * valor_hora

print("O valor do salário é: R$", salario)