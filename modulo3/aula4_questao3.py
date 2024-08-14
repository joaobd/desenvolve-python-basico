# Solicitando ao usuário para inserir um ano
ano = int(input("Digite um ano: "))

# Verificando se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")
