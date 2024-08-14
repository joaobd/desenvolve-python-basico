# Lendo as dimensões do terreno em inteiros
comprimento = int(input("Digite o comprimento do terreno (em metros): "))  # Comprimento do terreno
largura = int(input("Digite a largura do terreno (em metros): "))          # Largura do terreno

# Lendo o preço do metro quadrado em ponto flutuante
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))       # Preço por metro quadrado

# Calculando a área do terreno em metros quadrados
area_m2 = comprimento * largura  # Área total do terreno

# Calculando o preço total do terreno
preco_total = preco_m2 * area_m2  # Valor total do terreno

# Imprimindo o resultado com a formatação solicitada
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")  # Exibindo a área e o preço total formatado
