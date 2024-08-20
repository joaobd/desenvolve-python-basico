# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Obtém as vogais (ignorando maiúsculas)
vogais = [letra.lower() for letra in frase if letra.lower() in "aeiou"]

# Obtém as consoantes (ignorando maiúsculas)
consoantes = [letra for letra in frase if letra.isalpha() and letra.lower() not in "aeiou"]

# Imprime as listas
print("Vogais:", vogais)
print("Consoantes:", consoantes)
