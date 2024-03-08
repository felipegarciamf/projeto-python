def logar_usuario(): 
    try:
        usuario = input("Digita seu usuario: ")   
        senha = input("Digite sua senha: ")
        usuario = int(usuario)
        senha = int(senha)
        if usuario == 123 and senha == 123:
            print("Bem vindo")
        else:
            print("Usuário ou senha inválidos")
    except:
        print("Digite um usuário e senha válidos")







