# Recebe a quantidade de elementos da lista 1 e os elementos
qtd_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
for i in range(qtd_lista1):
    elemento = int(input(f"Digite o elemento {i+1} da lista 1: "))
    lista1.append(elemento)

# Recebe a quantidade de elementos da lista 2 e os elementos
qtd_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
for i in range(qtd_lista2):
    elemento = int(input(f"Digite o elemento {i+1} da lista 2: "))
    lista2.append(elemento)

# Combina as duas listas de forma alternada
lista_intercalada = []
menor_tamanho = min(len(lista1), len(lista2))

for i in range(menor_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adiciona os elementos remanescentes da lista maior
if len(lista1) > len(lista2):
    lista_intercalada.extend(lista1[menor_tamanho:])
else:
    lista_intercalada.extend(lista2[menor_tamanho:])

# Imprime a lista intercalada
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))