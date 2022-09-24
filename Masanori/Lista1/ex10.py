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
print(f"Isso equivale a {int(dias)} dias, {int(horas)} horas e {int(minutos)} minutos.")
