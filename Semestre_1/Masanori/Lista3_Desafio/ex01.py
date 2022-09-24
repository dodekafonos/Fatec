# Lista 3 - Desafio
# Jonas Alves Bueno
# 1º ADS Matutino - 2022/2

# Exercício 01.
# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
# Exemplo: 120 é triangular, pois 4.5.6 = 120.
# Dado um inteiro não-negativo n, verificar se n é triangular.

n = int(input("Entre com um inteiro não-negativo: "))
test = 0
a, b, c = 1, 2, 3
circulares = []

while test < n:
    test = a * b * c
    circulares.append(test)
    a += 1
    b += 1
    c += 1

if n in circulares:
    print(f"{n} é um número circular, produto de {a-1} * {b-1} * {c-1}!")
else:
    print(f"{n} não é um número circular.")
    print(f"Circular anterior: {circulares[-2]}.")
    print(f"Próximo circular: {circulares[-1]}")
