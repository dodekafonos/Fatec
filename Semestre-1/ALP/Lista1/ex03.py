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

print(f"Então você já possui {total_segundos} vividos. Parabéns!!!")
