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
