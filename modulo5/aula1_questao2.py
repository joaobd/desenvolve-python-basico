import random
import math

# Solicita ao usuário o valor de n
n = input("Digite o valor de n (quantidade de números aleatórios): ")

if not n.isdigit():
    print("Valor inválido. Digite um número inteiro válido.")
else:
    n = int(n)
    numeros_aleatorios = [random.randint(0, 100) for _ in range(n)]
    soma = sum(numeros_aleatorios)
    raiz_quadrada_soma = math.sqrt(soma)
    print(f"Números gerados: {numeros_aleatorios}")
    print(f"Soma dos valores: {soma}")
    print(f"Raiz quadrada da soma: {raiz_quadrada_soma:.2f}")
