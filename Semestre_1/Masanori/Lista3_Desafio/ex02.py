# Exercício 02.
conta = int(input("Valor da conta: R$"))
troco = conta
cinquenta, vinte, dez, cinco, dois, um = 0, 0, 0, 0, 0, 0

cinquenta = int(troco / 50)
troco -= cinquenta * 50

vinte = int(troco / 20)
troco -= vinte * 20

dez = int(troco / 10)
troco -= dez * 10

cinco = int(troco / 5)
troco -= cinco * 5

dois = int(troco / 2)
troco -= dois * 2

um = int(troco / 1)
troco -= um * 1

print("="*38)
print(f'''
Você vai precisar de:
{cinquenta} notas de R$50;
{vinte} notas de R$20;
{dez} notas de R$10;
{cinco} notas de R$5;
{dois} notas de R$2;
{um} notas de R$1.''')
print("="*38)
m = cinquenta + vinte + dez + cinco + dois + um
print(f"O mínimo de notas para este valor é {m}")
