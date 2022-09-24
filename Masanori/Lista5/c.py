start = 1067
end = 3627
pares_mult_sete = []

for num in range(start, end+1):
    if num % 2 == 0 and num % 7 == 0: pares_mult_sete.append(num)
    
print(f"Entre {start} e {end} existem {len(pares_mult_sete)} números divisíveis por 2 e 7:")
print(pares_mult_sete)