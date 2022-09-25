#Exercício 11.
"""
Sabendo que str( ) converte valores numéricos para string,
calcule quantos dígitos há em 2 elevado a um milhão.
"""

biggie = 2 ** 1000000
big_str = str(biggie)
print(len(big_str))
