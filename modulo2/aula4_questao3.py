# Solicitando os dados do primeiro produto
nome_produto1 = input("Informe o nome do primeiro produto: ")  # Nome do produto 1
preco_unitario1 = float(input("Informe o preço unitário do primeiro produto (R$): "))  # Preço unitário do produto 1
quantidade1 = int(input("Informe a quantidade do primeiro produto: "))  # Quantidade do produto 1

# Solicitando os dados do segundo produto
nome_produto2 = input("Informe o nome do segundo produto: ")  # Nome do produto 2
preco_unitario2 = float(input("Informe o preço unitário do segundo produto (R$): "))  # Preço unitário do produto 2
quantidade2 = int(input("Informe a quantidade do segundo produto: "))  # Quantidade do produto 2

# Solicitando os dados do terceiro produto
nome_produto3 = input("Informe o nome do terceiro produto: ")  # Nome do produto 3
preco_unitario3 = float(input("Informe o preço unitário do terceiro produto (R$): "))  # Preço unitário do produto 3
quantidade3 = int(input("Informe a quantidade do terceiro produto: "))  # Quantidade do produto 3

# Calculando o preço total da compra
total = (preco_unitario1 * quantidade1) + (preco_unitario2 * quantidade2) + (preco_unitario3 * quantidade3)

# Imprimindo o preço total formatado
print(f"Total: R${total:,.2f}")  # Formatação com separador de milhar e duas casas decimais
