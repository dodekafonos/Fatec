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
