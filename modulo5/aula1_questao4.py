import datetime

# Obtém a data e hora atuais
data_hora_atual = datetime.datetime.now()

# Formatação da data e hora
data_formatada = data_hora_atual.strftime("%d/%m/%Y")
hora_formatada = data_hora_atual.strftime("%H:%M")

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
