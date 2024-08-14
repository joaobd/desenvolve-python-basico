N = int(input("Digite a quantidade de respondentes: "))
total_idade = 0

for _ in range(N):
    idade = int(input("Digite a idade do respondente: "))
    total_idade += idade

media = total_idade / N
print(f"A média das idades é: {media:.2f}")
