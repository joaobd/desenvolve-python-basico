# Solicitando a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega em km: "))

# Solicitando o peso do pacote em quilogramas
peso = float(input("Digite o peso do pacote em kg: "))

# Inicializando a variável do custo do frete
custo_frete = 0

# Calculando o custo do frete com base na distância
if distancia <= 100:
    custo_frete = peso * 1.0  # R$1 por kg
elif 101 <= distancia <= 300:
    custo_frete = peso * 1.5  # R$1.50 por kg
else:
    custo_frete = peso * 2.0   # R$2 por kg

# Adicionando a taxa de R$10 para pacotes acima de 10 kg
if peso > 10:
    custo_frete += 10

# Imprimindo o valor total do frete
print(f"O valor do frete é R${custo_frete:.2f}")
