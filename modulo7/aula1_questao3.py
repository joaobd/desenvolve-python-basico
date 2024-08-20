def contar_espacos(frase):
    return frase.count(' ')

frase = input("Digite a frase: ")
espacos_em_branco = contar_espacos(frase)
print(f"Espaços em branco: {espacos_em_branco}")