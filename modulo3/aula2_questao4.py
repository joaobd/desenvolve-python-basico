# Solicitando a classe do personagem
classe = input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()

# Solicitando os pontos de força e magia
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

# Verificando se os atributos são consistentes com a classe escolhida
if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = 5 < forca <= 15 and 5 < magia <= 15
else:
    valido = False  # Caso a classe seja inválida, retorna False

# Imprimindo o resultado
print(valido)
