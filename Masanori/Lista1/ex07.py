#Exercício 07.
"""
Converta uma temperatura digitada em Celsius para Fahrenheit.
F = 9*C/5 + 32
"""

c = float(input("Digite uma temperatura em graus Celsius: "))
f = (9 * c / 5) + 32

print(f"Isso equivale a {f:.2f} ºF.")
