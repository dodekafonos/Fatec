#Exercício 09.
"""
Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado pelo usuário, 
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar,sabendo que o carro custa
R$ 60,00 por dia e R$ 0,15 por km rodado.
"""
print("Bem vindo à Localiza. Vamos calcular quanto ficou essa brincadeira.")

kms = float(input("Quantos kilometros você rodou com o nosso carro? "))
dias = int(input("E por quantos dias você ficou com o carro? "))

p = kms * 0.15 + dias * 60

print(f"O valor total a pagar é de R${p:.2f}. Volte sempre!")
