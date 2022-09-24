
meses = """
Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro
""".split()

dia, mes, ano = input("dd/mm/aaaa: ").split("/")

print(f"Seu aniversário é dia {dia} de {meses[int(mes) -1]} de {ano}.")