pares = [num for num in range(20, 51) if num % 2 == 0]
print("Números pares:", pares)

quadrados = [num ** 2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print("Quadrados:", quadrados)

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Divisíveis por 7:", divisiveis_por_7)

par_ou_impar = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print("Par ou ímpar:", par_ou_impar)
