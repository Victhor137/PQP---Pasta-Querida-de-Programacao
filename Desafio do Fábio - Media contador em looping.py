# Listas
nomes = []
medias = []
status = []

# Contador
contador = 0
while contador < 3:
    nome = input(f"Digite o nome do {contador + 1}º aluno: ")
    nota1 = float(input("Digite a nota da 1ª avaliação: "))
    nota2 = float(input("Digite a nota da 2ª avaliação: "))
    nota3 = float(input("Digite a nota da 3ª avaliação: "))

    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 6:
        aluno_status = "Aprovado"
    else:
        aluno_status = "Reprovado"
    
    nomes.append(nome)
    medias.append(media)
    status.append(aluno_status)

    contador += 1

# Printada
print("\nRelatório Final:")
for i in range(3):
    print(f"Nome: {nomes[i]}")
    print(f"Média: {medias[i]:.2f}")
    print(f"Status: {status[i]}")
    print("-" * 20)
