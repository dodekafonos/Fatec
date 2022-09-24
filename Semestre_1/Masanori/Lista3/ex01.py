
while (True):

    nota = input("Entre com uma nota de 0.0 a 10: ")
    
    nota = float(nota)

    if nota < 0 or nota > 10:
        print("Esta nota é inválida. Tente novamente.")
    else:
        print("Você digitou a nota ", nota)
        break
        
