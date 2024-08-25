import os
import matplotlib.pyplot as plt
import numpy as np

qtd = int(input("Digite a quantidade de alunos no total (max. 5): "))
while qtd > 5:
    print('Inválido! No máximo 5.')
    qtd = int(input("Digite a quantidade de alunos no total (max. 5): "))

nomes = []
notas = []

for i in range(1, qtd + 1):
    os.system('cls')
    nome = input(f"Digite o nome do {i}º aluno: ")
    nomes.append(nome)
    notas_aluno = []
    for x in range(1, 5):
        while True:
            nota = int(input(f"Digite a nota do aluno {nome} para o {x}º bimestre (0-10): "))
            if nota > 10 or nota < 0:
                print("A nota deve ser entre 0 e 10! Tente novamente.")
            else:
                notas_aluno.append(nota)
                break
    notas.append(notas_aluno)

bimestres = [1, 2, 3, 4]
width = 0.15 

x = np.arange(len(bimestres))

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(qtd):
    ax.bar(x + i * width, notas[i], width, label=nomes[i])

ax.set_xlabel('Bimestres')
ax.set_ylabel('Notas')
ax.set_title('Comparação de Notas dos Alunos por Bimestre')
ax.set_xticks(x + width * (qtd - 1) / 2)
ax.set_xticklabels(bimestres)
ax.set_ylim(0, 10)
ax.legend(title="Alunos")

plt.show()