pos = int(input("Posição na sequência fibonacci: "))

# Solução recursiva:
# def fib(n):

#     if (n <= 2):
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(pos))

# Solução com while:
fib = 0
ultimo = 1
penultimo = 0
cont = pos
while cont >= 1:
    fib = ultimo + penultimo
    penultimo = ultimo
    ultimo = fib
    cont -= 1
print(f"O {pos}º número da sequência fibonacci é {fib}")
