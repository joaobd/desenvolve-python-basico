# Solicitando o gênero do usuário
genero = input("Digite seu gênero (M para masculino, F para feminino): ").strip().upper()

# Solicitando a idade e o tempo de serviço do usuário
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (em anos): "))

# Verificando se a pessoa já pode se aposentar
if genero == "F":
    pode_aposentar = idade > 60 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)
elif genero == "M":
    pode_aposentar = idade > 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25)
else:
    pode_aposentar = False  # Caso o gênero seja inválido, retorna False

# Imprimindo o resultado
print(pode_aposentar)
