num = int(input("Digite um número: "))
fatores, primos = [], []
def primo(n):
    div = 0
    for d in range (1, n+1):
        if n % d == 0: div += 1
    return div < 3

for n in range(1, num+1):
    if num % n == 0: fatores.append(n)
for fator in fatores:
    if primo(fator) and fator != 1: primos.append(fator)
if primo(num):
    print(f"{num} é um número primo!")
else:
    print(f"Fatores: {fatores}")
    print(f"{num} tem os seguintes fatores primos: {primos}")