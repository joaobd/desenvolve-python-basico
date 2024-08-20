import os, csv

def processar_musicas():
    caminho_arquivo = os.path.join(os.getcwd(), "spotify-2023.csv")
    try:
        with open(caminho_arquivo, "r", encoding="latin-1") as arquivo:
            leitor_csv = csv.reader(arquivo)
            cabecalho = next(leitor_csv)  # Pula o cabeçalho

            # Dicionário para armazenar a música mais tocada de cada ano
            musicas_por_ano = {}

            for linha in leitor_csv:
                try:
                    track_name = linha[0]
                    artist_name = linha[1]
                    artist_count = int(linha[2])
                    released_year = int(linha[3])
                    streams = int(linha[8])

                    # Considera apenas músicas entre 2013 e 2023
                    if 2013 <= released_year <= 2023:
                        if released_year not in musicas_por_ano or streams > musicas_por_ano[released_year][3]:
                            musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]
                except ValueError:
                    # Ignora linhas com dados inválidos
                    continue

            # Gera a lista final com as músicas mais tocadas de cada ano
            lista_musicas = [musicas_por_ano[ano] for ano in sorted(musicas_por_ano)]

            return lista_musicas
    except FileNotFoundError:
        print(f"Arquivo não encontrado no diretório: {os.getcwd()}")
        return []

# Executa a função e imprime a lista
lista_musicas = processar_musicas()
print(lista_musicas)