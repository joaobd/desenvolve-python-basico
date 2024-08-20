import os

def salvar_frase():
    frase = input("Digite uma frase: ")
    caminho_arquivo = os.path.join(os.getcwd(), "frase.txt")
    
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(frase)
    
    print(f"Frase salva em {caminho_arquivo}")

# Executa a função
salvar_frase()
