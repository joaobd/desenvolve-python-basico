def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    frase_modificada = ''.join(['*' if char in vogais else char for char in frase])
    return frase_modificada

frase = input("Digite uma frase: ")
frase_modificada = substituir_vogais(frase)
print(f"Frase modificada: {frase_modificada}")