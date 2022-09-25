a = 80000
b = 200000
ano = 0
while a <= b:
    a += (a * 3 / 100)
    b += (b * 1.5 / 100)
    ano += 1
print(f"Em {ano} anos a população do país A será maior do que a população do país B.")
print(f"País A: {a:.0f}")
print(f"País B: {b:.0f}")