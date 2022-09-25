
import random

lista = []
for i in range (0, 10):

    lista.append(random.randrange(1, 101))

maior = 0
menor = 101

for elemento in lista:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento

print(f"Lista: {lista}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")



