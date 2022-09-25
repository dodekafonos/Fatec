
nomes = ["Thomas", "Renan", "Jonas", "Alexandre", "Alita", "Amanda"]

nomes.sort()

print("Ordem alfabética: ")
for i in range(len(nomes)):
    print(nomes[i])

i = 0

print("Ordem de tamanho: ")
while i < len(nomes):
    print(nomes[i])
    i += 1

nomes.sort(key = len)