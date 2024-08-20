alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Usando compreensão de listas para criar a lista de aprovados
aprovados = [alunos[i] for i in range(len(alunos)) if notas[i] >= 60]

print(aprovados)
