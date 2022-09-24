# Exercício 04.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

maior = a

if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"O maior número digitado foi {maior}")
