import random

def escolher_palavra():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip().lower()

def carregar_estagios():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        estagios = arquivo.read().split("\n\n")
    return estagios

def imprime_enforcado(erros, estagios):
    if erros < len(estagios):
        print(estagios[erros])
    else:
        print(estagios[-1])

def jogar_forca():
    palavra = escolher_palavra()
    estagios = carregar_estagios()
    palavra_oculta = ["_" for _ in palavra]
    tentativas = 6
    letras_erradas = []
    letras_certas = []

    while tentativas > 0 and "_" in palavra_oculta:
        print("\nPalavra:", " ".join(palavra_oculta))
        print(f"Erros restantes: {tentativas}")
        print("Letras erradas:", " ".join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_certas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_certas.append(letra)
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            imprime_enforcado(6 - tentativas, estagios)

    if "_" not in palavra_oculta:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
    else:
        imprime_enforcado(6, estagios)  # Imprime o estágio final do enforcado
        print("\nVocê perdeu! A palavra era:", palavra)

# Executa o jogo
jogar_forca()