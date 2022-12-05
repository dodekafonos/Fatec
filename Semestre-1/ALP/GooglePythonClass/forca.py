# EP Opcional: Jogo da Forca
# dupla: Jonas e Amanda. 1º ADS Matutino
from urllib.request import urlopen
from random import randint

forca = [
    '''
    |====+
         |
         |
         |
=========+
    ''',
    '''
    |====+
    0    |
         |
         |
=========+
    ''',
    '''
    |====+
    0    |
    |    |
         |
=========+
    ''',
    '''
    |====+
    0    |
    |\   |
         |
=========+
    ''',
    '''
    |====+
    0    |
   /|\   |
         |
=========+
    ''',
    '''
    |====+
    0    |
   /|\   |
     \   |
=========+
    ''',
    '''
    |====+
    0    |
   /|\   |
   / \   |
=========+
    '''
]

def escolhe():
    print("\nBem vindo ao jogo da forca!")
    print("Escolhi uma palavra aleatória. Você tem 6 tentativas para acertá-la.")
    url = "https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt"
    site = urlopen(url)
    lista = site.read().decode('utf-8').split()
    segredo = lista[randint(0, len(lista))]
    return segredo

def desenha():
    print(forca[len(erradas)])

def chute(letra):
    global certas
    global erradas

    alfabeto = "abcdefghijklmnopqrstuvxyz"
    if len(letra) > 1:
        print("Adivinhe apenas uma letra de cada vez.")
        return
    if letra.lower() not in alfabeto:
        print("Caractere inválido, tente novamente.")
        return
    if letra.lower() in certas:
        print("Você já chutou esta letra. Tente novamente.")
        return
    if letra in segredo:
        ocorrencias = segredo.count(letra)
        certas += letra * ocorrencias
    else:
        erradas += letra
    return desenha()

def jogar_novamente():
    continuar = ""
    while True:
        continuar = input("Deseja jogar novamente? [s/n]: ").lower()
        if continuar == "s" or continuar == "n": break
    if continuar == "s": return True
    else: return False

def ganhou():
    print("\n==================================\n")
    print("Parabéns, você ganhou!")
    print("\n==================================\n")
    return

certas, erradas = "", ""
segredo = escolhe()

while True:
    print("\nacertos: ", certas.upper(), "\n")
    print("erros: ", erradas.upper(), "\n")

    for i in range(len(segredo)):
        if segredo[i] in certas:
            print(segredo[i].upper(), end=" ")
        else:
            print("_", end=" ")

    letra = input("Advinhe uma letra: ")
    chute(letra)

    if len(certas) == len(segredo):
        ganhou()
        opc = jogar_novamente()
        if opc:
            certas = ""
            erradas = ""
            segredo = escolhe()
        else:
            print("Obrigado por jogar! Até a próxima.")
            break

    if len(erradas) >= 6:
        print("Você perdeu.")
        jogar_novamente()
        opc = jogar_novamente()
        if opc:
            certas = ""
            erradas = ""
            segredo = escolhe()
        else:
            print("Obrigado por jogar! Até a próxima.")
            break
