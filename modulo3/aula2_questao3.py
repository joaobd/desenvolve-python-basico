# Solicitando a idade do usuário
idade = int(input("Digite sua idade: "))

# Verificando se o usuário já jogou pelo menos 3 jogos de tabuleiro
jogou_tres_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False) ").strip().capitalize()
jogou_tres_jogos = jogou_tres_jogos == "True"

# Solicitando o número de vitórias em jogos de tabuleiro
vitorias = int(input("Quantos jogos já venceu? "))

# Verificando se o usuário está apto a ingressar no clube
apto = (16 <= idade <= 18) and jogou_tres_jogos and (vitorias > 0)

# Imprimindo o resultado
print("Apto para ingressar no clube de jogos de tabuleiro:", apto)
