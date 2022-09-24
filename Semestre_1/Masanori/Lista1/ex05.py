#Exercício 05.
"""
Solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""
# p = preço
# pd = percentual de desconto
# vd = valor do desconto
# pf = preço final

p = float(input("Informe o preço da mercadoria: "))
pd = int(input("Informe o percentual de desconto: "))

vd = (pd * p / 100)
pf = p - vd

print(f"O seu desconto foi de R${vd:.2f}. O preço com desconto é de R${pf:.2f}.")
