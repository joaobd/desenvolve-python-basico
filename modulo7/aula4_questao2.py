import os
import re

def processar_frase():
    caminho_arquivo_frase = os.path.join(os.getcwd(), "frase.txt")
    caminho_arquivo_palavras = os.path.join(os.getcwd(), "palavras.txt")
    
    with open(caminho_arquivo_frase, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    
    # Remove caracteres não alfabéticos e separa as palavras
    palavras = re.findall(r'\b\w+\b', conteudo)
    
    with open(caminho_arquivo_palavras, "w", encoding="utf-8") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")
    
    print(f"Conteúdo do arquivo '{caminho_arquivo_palavras}':")
    with open(caminho_arquivo_palavras, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

# Executa a função
processar_frase()
