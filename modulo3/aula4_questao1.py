# Solicitando os dois números do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calculando a soma dos dois números
soma = numero1 + numero2

# Verificando se a soma é par ou ímpar usando o operador %
if soma % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")
