n = int(input("Digite um número: "))
div = []

for d in range (1, n+1):
    if n % d == 0: div.append(d)
if len(div) <= 2:
    print(f"{n} é um número primo, parabéns!")
    print(div)
else:
    print(f"{n} não é primo e tem os seguinte divisores:")
    print(div)

# testar com 8278737359