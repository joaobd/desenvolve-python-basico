from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    palavra_objetivo_contador = Counter(palavra_objetivo.lower())
    palavras = frase.split()
    anagramas = []

    for palavra in palavras:
        if Counter(palavra.lower()) == palavra_objetivo_contador:
            anagramas.append(palavra)

    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = encontrar_anagramas(frase, palavra_objetivo)
print(f"Anagramas: {anagramas}")