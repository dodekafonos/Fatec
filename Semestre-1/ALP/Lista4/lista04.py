# Exercício 01:
print("\n","="*80,"\n")
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

# Exercício 02:
print("\n","="*80,"\n")
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

# Exercício 03:
print("\n","="*80,"\n")
from random import randint

l1 = []
l2 = []
l3 = []

for i in range(0, 10):
    l1.append(randint(1, 101))
    l2.append(randint(1, 101))

for el in range(0, len(l1)):
    l3.append(l1[el])
    l3.append(l2[el])

print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")
print(f"União intercalada: {l3}")

# Exercício 04:
print("\n","="*80,"\n")
st = "The Python Software Foundation and the global Python community welcomes and encourages participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
st = st.lower()
st = st.replace(",", "")
st = st.replace(".", "")
st = st.replace(":", "")

frase = st.split(" ")
pythonwords = []

for word in frase:
    if word[0] in "python" or word[-1] in "python":
        pythonwords.append(word)
print(pythonwords)

# Exercício 05:
print("\n","="*80,"\n")
original = "The Python Software Foundation and the global Python community welcomes and encourages participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

original = original.lower().replace(",", "").replace(".", "").replace(":", "")

frase = original.split(" ")

def select(frase):
    words = []
    for word in frase:
        if len(word) > 4:
            for letter in word:
                if letter in "python":
                    words.append(word)
                    break
    return words

print(select(frase))
print(f"A frase original tem {len(select(frase))} palavras que contém uma das letras de 'python'.")
