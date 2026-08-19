#Escreva um programa em Python que solicite ao usuário a
#distância entre duas cidades e o tempo de viagem. O
#programa deverá calcular e exibir a velocidade média de um
#carro que vai de uma cidade para outra.

#como sou vida louca vou fazer ao contrario tbm

print ("bem vindo a sua calculadora de viagens !! ")

print ("se você deseja ver sua velocidade media em uma viagem digite vm ")
print ("se você deseja ver a distancia entre duas cidades digite dist ")

op = input (" digite uma opção : ")

if op == ("vm"):

    print ("calculadora de velocidade media da viagem ")

    dist = float ( input ( " qual a distancia entre as duas cidades ? "))

    temp = float (input (" quanto tempo demora sua viagem ? "))

    vm = dist / temp 

    print ("a velocidade media da sua viagem é de : " , vm , "km/h")

else :
    print (" calculadora de distancia media entre duas cidades ")

    velm =  float (input (" qual foi sua velocidade media durante a viagem ? "))
    
    dur = float ( input ( " quanto tempo sua viagem durou ? "))

    esp = velm * dur 

    print (" a distancia media entre as duas cidades é de : ", esp ,"km")