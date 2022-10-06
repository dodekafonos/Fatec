inp = input("Digite uma sequência de numeros:")


def soma(nums):
    # lista = []
    s = 0
    nums = nums.strip()
    lista = nums.split()
    for n in lista:
        s += int(n)
    return s

print(f"A soma dos números é: {soma(inp)}")