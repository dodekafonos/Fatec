"""
Lista de Exercício II
Jonas Alves Bueno 
ADS - manhã - 1º Semestre
"""
# ============
# Exercício 01.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a <= b + c and b <= a + c and c <= a + b:
    print("triângulo")
    if a == b == c:
        print("Equilátero")
    elif a == b or b == c or c == a:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não triângulo")

