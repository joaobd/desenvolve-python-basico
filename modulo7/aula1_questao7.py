import random

def encrypt(lista_strings, chave):
    n = chave
    lista_criptografada = []

    for string in lista_strings:
        string_criptografada = ""
        for char in string:
            novo_char = chr(((ord(char) - 33 + n) % 94) + 33)
            string_criptografada += novo_char
        lista_criptografada.append(string_criptografada)

    return lista_criptografada, n

# Exemplo de uso
chave_aleatoria = 5

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
print(f"Nomes: {nomes}")

nomes_criptografados = encrypt(nomes, chave_aleatoria)
print(f"Nomes criptografados: {nomes_criptografados}")