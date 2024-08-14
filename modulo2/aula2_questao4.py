# Inicializando as variáveis
juros = 1.01
saldo = 500.0

# Calculando o saldo após três meses
saldo *= juros  # Após 1º mês
saldo *= juros  # Após 2º mês
saldo *= juros  # Após 3º mês

# Imprimindo o resultado final
print("Após 3 meses meu novo saldo é")
print(saldo)