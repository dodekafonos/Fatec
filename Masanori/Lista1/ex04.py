#Exercício 04.
"""
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""

sal = float(input("Por favor, nos informe seu salário atual: R$"))
aum = float(input("Informe por gentileza a porcentagem do aumento recebido: "))

valor_aum = (aum * sal / 100)
novo = sal + valor_aum

print(f"O seu aumento foi de R${valor_aum:.2f}.")
print(f"Seu novo salário será de R${novo:.2f}.")
