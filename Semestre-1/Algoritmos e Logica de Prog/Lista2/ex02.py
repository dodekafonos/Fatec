# Exercício 02.

ano = int(input("Digite um ano qualquer... "))
if ano % 400 == 0:
    print("Este é um ano bissexto, ou seja, de 366 dias.")
if ano % 4 == 0 and ano % 100 != 0:
    print("Este é um ano bissexto, ou seja, de 366 dias.")
else: 
    print("Este não é um ano bissexto.")

