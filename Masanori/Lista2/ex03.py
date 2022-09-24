# Exercício 03.

multa = 0
excesso = 0

peso = float(input("Peso de peixes de hoje: "))
dif = int(peso - 50)

if dif > 0:
    multa += dif * 4
    excesso += dif

print(f"Excesso: {excesso}kg; multa: R$ {multa}.")
