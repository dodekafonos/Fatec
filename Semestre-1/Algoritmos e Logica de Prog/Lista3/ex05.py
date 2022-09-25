n1, n2 = input("digite dois números inteiros não nulos e eu te direi qual o máximo divisor comum entre eles: ").split(" ")

x = int(n1)
y = int(n2)
resto = 0

while y != 0:
    resto = x %y
    x = y
    y = resto
print(f"O MDC entre {n1} e {n2} é {x}")

