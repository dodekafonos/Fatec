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

print(f"O tempo gasto na viagem será de {h} horas e {m:.0f} minutos.")
