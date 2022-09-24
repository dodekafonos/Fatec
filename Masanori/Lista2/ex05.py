# Exercício 05.

a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

menor = a
maior = a

if b < menor:
    menor = b
if c < menor:
    menor = c

if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"O menor número digitado foi {menor}.")
print(f"O maior número digitado foi {maior}.")

