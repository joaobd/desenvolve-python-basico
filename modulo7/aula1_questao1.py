def imprimir_escada(nome):
    for i in range(1, len(nome) + 1):
        print(nome[:i])

nome = input("Digite seu nome: ")
imprimir_escada(nome)