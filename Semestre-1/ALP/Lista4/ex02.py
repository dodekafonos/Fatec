
import random

lista = []
for i in range (0, 20):
    lista.append(random.randrange(1, 101))

pares = []
impares = []

for j in lista:
    if j % 2 == 0:
        pares.append(j)
    else:
        impares.append(j)

print(lista)
print(f"Pares: {pares}")
print(f"Ímpares {impares}")



















