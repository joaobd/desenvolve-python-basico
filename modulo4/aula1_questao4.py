n = float(input("Leia n: "))  # Lê o valor de n (assumindo que o input é um número)
maior = 0  # Inicializa a variável 'maior' como 0

while n > 0:
    x = float(input("Leia x: "))  # Lê o valor de x (assumindo que o input é um número)
    if x > maior:
        maior = x  # Atualiza 'maior' se x for maior que o valor atual
    n = n - 1  # Decrementa n em 1

print("Maior valor encontrado:", maior)  # Imprime o maior valor encontrado
print("Fim")  # Sempre imprime "Fim" no final
