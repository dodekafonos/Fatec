#====================================================================
# Exercício 01.
'''
Faça um programa que peça dois números inteiros;
imprima a soma desses dois números.
'''

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
r = a + b

print(f"O resultado da soma entre {a} e {b} é {r}.\n")

#====================================================================
#Exercício 02.
"""
Escreva um programa que leia um valor em metros;
o exiba convertido em milímetros.
"""

m = float(input("Forneça um valor em metros: "))
mm = m*100

print(f"{m:.2f}m convertido para milímetros é igual a {mm:.2f}mm.\n")

#====================================================================
#Exercício 03.
'''
Escreva um programa que leia a quantidade de
dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
'''

dias = int(input("Quantos dias vc tem? "))
horas = int(input("E quantas horas? "))
minutos = int(input("Mas diga lá... e quantos minutos hein?? "))
segundos = int(input("Quero ver se sabe quantos segundos então... "))

total_segundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"Então você já possui {total_segundos} segundos vividos. Parabéns!!!\n")

#====================================================================
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
print(f"Seu novo salário será de R${novo:.2f}.\n")

#====================================================================
#Exercício 05.
"""
Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""
# p = preço
# pd = percentual de desconto
# vd = valor do desconto
# pf = preço final

p = float(input("Informe o preço da mercadoria: "))
pd = int(input("Informe o percentual de desconto: "))

vd = (pd * p / 100)
pf = p - vd

print(f"O seu desconto foi de R${vd:.2f}. O preço com desconto é de R${pf:.2f}.\n")

#====================================================================
#Exercício 06.
"""
Calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada
para a viagem.
"""

dis = float(input("Qual distância você irá percorrer, em kms? "))
vel = float(input("Quantos km/h você pretender manter, em média? "))

tempo = (dis / vel) 
h = int(tempo)
m = (tempo - h) * 60

print(f"O tempo gasto na viagem será de {h} horas e {m:.0f} minutos.\n")

#====================================================================
#Exercício 07.
"""
Converta uma temperatura digitada em Celsius para Fahrenheit.
F = 9*C/5 + 32
"""

c = float(input("Digite uma temperatura em graus Celsius: "))
f = (9 * c / 5) + 32

print(f"Isso equivale a {f:.2f} ºF.\n")

#====================================================================
#Exercício 08.
"""
Converta uma temperatura digitada em Fahrenheit para Celsius.
F = 9*C/5 + 32
C = 9 / C * 5 - 32
"""

f = float(input("Digite uma temperatura em graus Fahrenheit: "))
c = (f - 32) / 9 * 5

print(f"Isso equivale a {c:.2f} ºC.\n")

#====================================================================
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

print(f"O valor total a pagar é de R${p:.2f}. Volte sempre!\n")

#====================================================================
#Exercício 10.
"""
Escreva um programa para calcular
a redução do tempo de vida de um fumante.
Pergunte a quantidade de cigarros fumados por dia
e quantos anos ele já fumou.
Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá.
Exiba o total de dias.
"""

# cpd = cigarros por dia
cpd = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("E a quantos anos você fuma? "))

tempo = cpd * 10 * anos * 365

dias = tempo / 60 / 24
horas = (dias - int(dias)) * 24
minutos = (horas - int(horas)) * 60

print(f"Lamentamos informar que você já perdeu {tempo} minutos de vida.")
print(f"Isso equivale a {int(dias)} dias, {int(horas)} horas e {int(minutos)} minutos.\n")

#====================================================================
#Exercício 11.
"""
Sabendo que str( ) converte valores numéricos para string,
calcule quantos dígitos há em 2 elevado a um milhão.
"""

biggie = 2 ** 1000000
big_str = str(biggie)
print(f"Dois elevado à um milhão resulta em um número que contém {len(big_str)} dígitos.")

