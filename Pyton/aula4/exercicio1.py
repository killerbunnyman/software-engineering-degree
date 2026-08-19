# 1- Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valor
# entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”.

num = float (input("digite um número: "))

if num >= 0 and num <= 9 : 
    print ("valor correto ")

else: 
    print ("valor incorreto")