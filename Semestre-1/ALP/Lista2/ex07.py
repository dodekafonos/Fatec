# Exercício 07.

area = int(input("Qual é a área a ser pintada, em metros quadrados? "))
litros = area / 3

latas = (litros / 18)

if latas - int(latas) != 0:
    latas = int(latas) + 1

preco = latas * 80
print(f"Para pintar esta área você precisará de {litros:.2f}L de tinta, ou seja, {latas} latas.")
print(f"O preço final é de R${preco}.")
