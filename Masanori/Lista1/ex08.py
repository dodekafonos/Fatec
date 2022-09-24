#Exercício 08.
"""
Converta uma temperatura digitada em Fahrenheit para Celsius.
F = 9*C/5 + 32
C = 9 / C * 5 - 32
"""

f = float(input("Digite uma temperatura em graus Fahrenheit: "))
c = (f - 32) / 9 * 5

print(f"Isso equivale a {c:.2f} ºC.")
