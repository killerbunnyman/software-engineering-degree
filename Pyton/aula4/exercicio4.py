# 4- Escreva um programa em Python que solicite ao usuário os valores de três contas de
# consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é
# suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
# insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.

agua = float(input("Digite o valor da conta de água: "))
luz = float(input("Digite o valor da conta de luz: "))
internet = float(input("Digite o valor da conta de internet: "))
salario = float(input("Digite o valor do seu salário: "))

# Soma das contas
total_contas = agua + luz + internet

# Verificação das condições
if salario < total_contas:
    print("Salário insuficiente!")
elif salario == total_contas:
    print("Você pagou suas contas, mas não sobrou nada.")
else:
    resto = salario - total_contas
    print(f"Após pagar as contas, restará: R$ {resto:.2f}")