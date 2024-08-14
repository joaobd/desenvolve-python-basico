n1 = float(input("Leia n1: "))  # Lê o valor de n1 (assumindo que o input é um número)
n2 = float(input("Leia n2: "))  # Lê o valor de n2 (assumindo que o input é um número)
n3 = float(input("Leia n3: "))  # Lê o valor de n3 (assumindo que o input é um número)

m = (n1 + n2 + n3) / 3  # Calcula a média

if m >= 60:
    print("Aprovado")  # Imprime "Aprovado" se a média for maior ou igual a 60
elif m >= 40:
    print("Recuperação")  # Imprime "Recuperação" se a média for maior ou igual a 40
else:
    print("Reprovado")  # Imprime "Reprovado" se a média for menor que 40

print("Fim")  # Sempre imprime "Fim" no final
