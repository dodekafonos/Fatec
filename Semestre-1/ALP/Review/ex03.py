f = open("./hi.txt")
vazias = 0
for line in f:
    if line.strip() == "":
        vazias += 1
    else: print(line)
print(vazias)