import emoji

# Lista de alguns emojis com seus textos correspondentes
emojis_disponiveis = {
    ":smile:": "😄",
    ":heart:": "❤️",
    ":rocket:": "🚀",
    ":star:": "⭐",
    ":thumbs_up:": "👍",
    ":fire:": "🔥",
    ":coffee:": "☕",
}

# Mostra a lista de emojis disponíveis
print("Emojis disponíveis:")
for texto, emoji_unicode in emojis_disponiveis.items():
    print(f"{texto} -> {emoji_unicode}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("Digite uma frase codificada (use os textos dos emojis acima): ")

# Decodifica a frase e exibe a visualização de emojis
frase_emojizada = emoji.emojize(frase_codificada)
print(f"Frase decodificada (emojizada): {frase_emojizada}")