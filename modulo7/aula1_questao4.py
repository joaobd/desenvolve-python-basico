def formatar_numero(numero):
    if len(numero) == 8:
        numero = '9' + numero
    if len(numero) == 9 and numero[0] != '9':
        numero = '9' + numero
    return numero[:5] + '-' + numero[5:]

numero = input("Digite o número: ")
numero_formatado = formatar_numero(numero)
print(f"Número completo: {numero_formatado}")