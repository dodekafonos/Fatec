f = open('surf.txt')
notas = {}
notas[9.12] = 'Juan'
notas[7.21] = 'Zack'
for n in sorted(notas, reverse = True):
    print(f'{notas[n]} {n}')
f.close()
