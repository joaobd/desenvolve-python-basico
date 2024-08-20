import os
import re

def analisar_arquivo():
    caminho_arquivo = os.path.join(os.getcwd(), "estomago.txt")
    
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    
    # Imprime as primeiras 25 linhas
    print("Texto das primeiras 25 linhas:")
    for i in range(min(25, len(linhas))):
        print(linhas[i].strip())
    
    # Número de linhas do arquivo
    num_linhas = len(linhas)
    print(f"\nNúmero de linhas do arquivo: {num_linhas}")
    
    # Linha com maior número de caracteres
    linha_maior = max(linhas, key=len).strip()
    print(f"\nLinha com maior número de caracteres: {linha_maior}")
    
    # Número de menções aos personagens "Nonato" e "Íria"
    conteudo = ''.join(linhas)
    num_nonato = len(re.findall(r'\b[Nn]onato\b', conteudo))
    num_iria = len(re.findall(r'\b[Ii]ría\b', conteudo))
    print(f"\nNúmero de menções a 'Nonato': {num_nonato}")
    print(f"Número de menções a 'Íria': {num_iria}")

# Executa a função
analisar_arquivo()