# Solicitando as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))  # Idade de Juliana
idade_cris = int(input("Digite a idade de Cris: "))        # Idade de Cris

# Verificando se ambas as idades são maiores que 17
pode_entrar = idade_juliana > 17 and idade_cris > 17  # Ambas precisam ser maiores de 17

# Imprimindo o resultado
print(pode_entrar)  # Exibe True se ambas forem maiores de 17, caso contrário False
