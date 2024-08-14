# Valores iniciais
v1 = 10
v2 = 20

# Usando uma variável auxiliar para trocar os valores
aux = v1  # Armazena o valor de v1 em aux
v1 = v2   # Atribui o valor de v2 a v1
v2 = aux  # Atribui o valor armazenado em aux a v2

# Imprimindo os valores após a troca
print("Após a troca:")
print("v1 =", v1)
print("v2 =", v2)