# 1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
# • não-eleitor (abaixo de 16 anos)
# • eleitor obrigatório (entre 18 e 65 anos)
# • eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não-eleitor")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
else:
    print("Eleitor facultativo")