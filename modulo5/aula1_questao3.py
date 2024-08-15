import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

print("Tente adivinhar o número secreto entre 1 e 10.")

while True:
    palpite = input("Digite seu palpite: ")

    if not palpite.isdigit():
        print("Entrada inválida. Digite um número inteiro válido.")
        continue

    palpite = int(palpite)

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Seu palpite é muito baixo. Tente novamente.")
    else:
        print("Seu palpite é muito alto. Tente novamente.")

print(f"O número secreto era {numero_secreto}. Obrigado por jogar!")
