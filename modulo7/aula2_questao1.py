def obter_mes_extenso(mes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[mes - 1]

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = map(int, data_nascimento.split('/'))
mes_extenso = obter_mes_extenso(mes)
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")
