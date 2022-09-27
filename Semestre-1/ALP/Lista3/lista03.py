# Exercício 01
nota = float(input("Entre com uma nota de 0.0 a 10: "))

while nota < 0 or nota > 10:
    print("Esta nota é inválida. Tente novamente.")
    nota = float(input("Entre com uma nota de 0.0 a 10: "))

print(f"Você digitou a nota {nota}")

# Exercício 02
while True:
    user = input("Usuário: ")
    passw = input("Senha: ")

    if user == passw:
        print("Sua senha precisa ser diferente do seu nome de usuário.\nTente novamente.")
    else: 
        print("Usuário criado com sucesso!")
        break

# Exercício 03
a = 80000
b = 200000
ano = 0
while a <= b:
    a += (a * 3 / 100)
    b += (b * 1.5 / 100)
    ano += 1
print(f"Em {ano} anos a população do país A será maior do que a população do país B.")
print(f"País A: {a:.0f}")
print(f"País B: {b:.0f}")

# Exercício 04
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


# Exercício 05
n1, n2 = input("digite dois números inteiros não nulos e eu te direi qual o máximo divisor comum entre eles: ").split(" ")

x = int(n1)
y = int(n2)
resto = 0

while y != 0:
    resto = x %y
    x = y
    y = resto
print(f"O MDC entre {n1} e {n2} é {x}")


