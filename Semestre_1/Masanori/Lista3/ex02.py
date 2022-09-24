while True:
    user = input("Usuário: ")
    passw = input("Senha: ")

    if user == passw:
        print("Sua senha precisa ser diferente do seu nome de usuário.\nTente novamente.")
    else: 
        print("Usuário criado com sucesso!")
        break