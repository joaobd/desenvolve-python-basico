# Solicita ao usuário uma quantidade indefinida de números inteiros
numeros = []
while len(numeros) < 4:
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Imprime a lista original
print("Lista original:", numeros)

# Fatiamento de listas
tres_primeiros = numeros[:3]
dois_ultimos = numeros[-2:]
invertida = numeros[::-1]
pares = numeros[::2]
impares = numeros[1::2]

# Imprime os resultados
print("Os 3 primeiros elementos:", tres_primeiros)
print("Os 2 últimos elementos:", dois_ultimos)
print("Lista invertida:", invertida)
print("Elementos de índice par:", pares)
print("Elementos de índice ímpar:", impares)