# Solicita ao usuário para inserir dois números decimais
numero1 = float(input("Digite o primeiro número decimal: "))
numero2 = float(input("Digite o segundo número decimal: "))

# Calcula a diferença absoluta entre os números
diferenca_absoluta = abs(numero1 - numero2)

# Arredonda o resultado para duas casas decimais
diferenca_arredondada = round(diferenca_absoluta, 2)

print(f"A diferença absoluta entre {numero1} e {numero2} é {diferenca_arredondada}.")
