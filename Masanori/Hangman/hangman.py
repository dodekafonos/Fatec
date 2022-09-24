# Jonas Alves Bueno
# Exercício complementar: Jogo da Forca.

# Modelo da Forca:
forca = ("""
    |=======
    ||     |
    ||     
    ||    
    ||    
    ||
    ==========""")
# 1º erro:
erro1 = ("""
    |=======
    ||     |
    ||     õ
    ||    
    ||    
    ||
    ==========""")
# 2º erro:
erro2 = ("""
    |=======
    ||     |
    ||     õ
    ||     |
    ||    
    ||
    ==========""")
# 3º erro:
erro3 = ("""
    |=======
    ||     |
    ||     õ
    ||    /|
    ||    
    ||
    ==========""")

# 4º erro:
erro4 = ("""
    |=======
    ||     |
    ||     õ
    ||    /|\\
    ||    
    ||
    ==========""")

# 5º erro:
erro5 = ("""
    |=======
    ||     |
    ||     õ
    ||    /|\\
    ||    / 
    ||
    ==========""")

# 6º erro:
erro6 = ("""
    |=======
    ||     |
    ||     õ
    ||    /|\\
    ||    / \\
    ||
    ==========""")

import requests
import random

certas = ""
erradas = ""


link = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"
txt = requests.get(link)
banco = txt.text.split("\n")
# nº palavras no banco: 245367
pos = random.randint(0, 245367)
palavra = banco[pos]



print("==============================================")
print("Bem vindes ao jogo da Forca!")
print("Já escolhi uma palavra...")
print("Você terá 5 chances para adivinhá-la. Valendo!")
print("==============================================")
print(forca)

print(palavra)

# função "desenha"
for letra in palavra:
    print("_ ", end="")
print("\n")

#função "chute"
chute = input("Chute uma letra: ")

if chute in palavra:
    print("nice")
else: print(erro3)





# certas; erradas;