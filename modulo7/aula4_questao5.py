import os, csv

# Lista de livros com as informações: título, autor, ano de publicação, número de páginas
livros = [
    ["1984", "George Orwell", 1949, 328],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["O Apanhador no Campo de Centeio", "J.D. Salinger", 1951, 277],
    ["Dom Quixote", "Miguel de Cervantes", 1605, 1072],
    ["Moby Dick", "Herman Melville", 1851, 635],
    ["Guerra e Paz", "Liev Tolstói", 1869, 1225],
    ["Orgulho e Preconceito", "Jane Austen", 1813, 279],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 417],
    ["Crime e Castigo", "Fiódor Dostoiévski", 1866, 671],
    ["O Grande Gatsby", "F. Scott Fitzgerald", 1925, 180]
]

# Nome do arquivo CSV
nome_arquivo = "meus_livros.csv"

# Criação e escrita no arquivo CSV
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    # Escreve os títulos das colunas
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    # Escreve as informações dos livros
    escritor_csv.writerows(livros)

print(f"Frase salva em {os.path.abspath(nome_arquivo)}")