# Lendo a temperatura em graus Fahrenheit
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))  # Temperatura em Fahrenheit

# Convertendo a temperatura para graus Celsius
celsius = (fahrenheit - 32) * (5 / 9)  # Fórmula de conversão
celsius_inteiro = int(celsius)  # Convertendo o valor em Celsius para inteiro

# Imprimindo o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius_inteiro} graus Celsius")  # Exibindo a conversão