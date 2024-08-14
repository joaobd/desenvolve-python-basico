N = int(input("Digite a quantidade de experimentos registrados: "))
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

for _ in range(N):
    quantia, tipo = input("Digite a quantidade e o tipo de cobaia (S/R/C): ").split()
    quantia = int(quantia)

    total_cobaias += quantia

    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia
    else:
        print(f"Tipo de cobaia inválido: {tipo}")

print(f"Total de cobaias utilizadas: {total_cobaias}")
print(f"Total de sapos: {total_sapos} - Percentual: ({(total_sapos / total_cobaias) * 100:.2f}%)")
print(f"Total de ratos: {total_ratos} - Percentual: ({(total_ratos / total_cobaias) * 100:.2f}%)")
print(f"Total de coelhos: {total_coelhos} - Percentual: ({(total_coelhos / total_cobaias) * 100:.2f}%)")
