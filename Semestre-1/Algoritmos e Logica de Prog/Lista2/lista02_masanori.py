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
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or b == c or c == a:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não pode ser um triângulo")
    
# Exercício 02.

ano = int(input("Digite um ano qualquer... "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é um ano bissexto, ou seja, de 366 dias.")
else:
    print(f"{ano} não é um ano bissexto.")
    
# Exercício 03.

multa = 0
excesso = 0

peso = float(input("Peso de peixes de hoje: "))
dif = int(peso - 50)

if dif > 0:
    multa += dif * 4
    excesso += dif

print(f"Excesso: {excesso}kg; multa: R$ {multa}.")

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

# Exercício 06.

hora = float(input("Quanto você recebe por hora? "))
mes = float(input("Quantas horas você trabalha no mês? "))

bruto = hora * mes
ir = 11 * bruto / 100
inss = 8 * bruto / 100
sind = 5 * bruto / 100
liquido = bruto - ir - inss - sind

print(f"Seu salário bruto é de {bruto}.")
print(f"Seus descontos são:")
print(f"Imposto de Renda: R${ir}. \nINSS: R${inss}\nSindicato: R${sind}")

print(f"Seu salário líquido é de: R${liquido}")

# Exercício 07.

area = int(input("Qual é a área a ser pintada, em metros quadrados? "))
litros = area / 3

latas = (litros / 18)

if latas - int(latas) != 0:
    latas = int(latas) + 1

preco = latas * 80
print(f"Para pintar esta área você precisará de {litros:.2f}L de tinta, ou seja, {latas} latas.")
print(f"O preço final é de R${preco}.")
