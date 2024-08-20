import random

# Gerando uma lista com 20 elementos aleatórios entre -10 e 10
minha_lista = [random.randint(-10, 10) for _ in range(20)]

# Encontrando o intervalo com a maior quantidade de números negativos em sequência
maior_contagem = 0
inicio_maior_intervalo = 0
contagem_atual = 0

for i, num in enumerate(minha_lista):
    if num < 0:
        contagem_atual += 1
        if contagem_atual > maior_contagem:
            maior_contagem = contagem_atual
            inicio_maior_intervalo = i - maior_contagem + 1
    else:
        contagem_atual = 0

# Intervalo com a maior quantidade de números negativos em sequência
maior_intervalo = minha_lista[inicio_maior_intervalo:inicio_maior_intervalo + maior_contagem]

# Imprimindo a lista original
print("Lista original:", minha_lista)
print("Intervalo com mais números negativos em sequência:", maior_intervalo)
print("Início do intervalor com mais números negativos em sequência:", inicio_maior_intervalo)
print("Tamanho do maior intervalo:", len(maior_intervalo))

# Removendo o intervalo com a maior quantidade de números negativos em sequência
del minha_lista[inicio_maior_intervalo:inicio_maior_intervalo + maior_contagem]

# Imprimindo a lista editada
print("Lista editada:", minha_lista)
