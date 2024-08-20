import random

# Gera 20 valores inteiros aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

# Imprime a lista original
print("Lista original:")
print(valores)

# Ordena a lista (sem modificar a original)
lista_ordenada = sorted(valores)
print("\nLista ordenada:")
print(lista_ordenada)

# Índice do maior valor
indice_maior = valores.index(max(valores))
print(f"\nÍndice do maior valor: {indice_maior}")

# Índice do menor valor
indice_menor = valores.index(min(valores))
print(f"Índice do menor valor: {indice_menor}")
