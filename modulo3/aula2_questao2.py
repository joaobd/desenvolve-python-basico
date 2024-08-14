# Solicitando as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))  # Idade de Juliana
idade_cris = int(input("Digite a idade de Cris: "))        # Idade de Cris

# Verificando se pelo menos uma das idades é maior que 17
pode_entrar = idade_juliana > 17 or idade_cris > 17  # Pelo menos uma precisa ser maior de 17

# Imprimindo o resultado
print(pode_entrar)  # Exibe True se uma delas for maior de 17, caso contrário False
