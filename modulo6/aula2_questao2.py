import random
from collections import Counter

# Preencher as listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar a intersecção sem duplicatas
interseccao = list(set(lista1) & set(lista2))
interseccao.sort()

# Contagem de ocorrências nas listas
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Impressão das listas e interseção
print(f"lista1 - {lista1}")
print(f"lista2 - {lista2}")
print(f"Interseccao - {interseccao}")

# Impressão da contagem de ocorrências
print("Contagem")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
