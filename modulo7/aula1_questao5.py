def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    indices = [i for i, letra in enumerate(frase) if letra in vogais]
    return len(indices), indices

frase = input("Digite uma frase: ")
quantidade_vogais, indices_vogais = contar_vogais(frase)
print(f"{quantidade_vogais} vogais")
print(f"Índices {indices_vogais}")