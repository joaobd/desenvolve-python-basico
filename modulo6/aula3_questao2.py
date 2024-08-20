# URLs fornecidas
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com", "www.uol.com"]

# Criando a lista de domínios
dominios = [url[4:-4] for url in urls]

# Imprimindo os domínios
print("Domínios:", dominios)
