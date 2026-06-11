dados = [[],[],[]]
notas = []
boletim = list()
soma = 0
alunos = 0
while True:
    nome = str(input('Nome do aluno: '))
    dados[1].append(nome)
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    soma = nota1 + nota2
    notas.append(nota1)
    notas.append(nota2)
    boletim.append(notas[:])
    notas.clear()
    somaf = soma
    dados[2].append(somaf / 2)
    soma = 0
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
    alunos += 1
print('-=' *20)
print('No.',end='       ')
print('NOME'.center(20), end='')
print('MÉDIA'.rjust(10))
for c in range(0,alunos+1):
    print(f'{c} ',end='')
    print(f'{dados[1][c]:>20}',end='')
    print(f'{dados[2][c]:>17}')
while True:
        indice = int(input('A nota de qual aluno deseja verificar? [999 para parar]: '))
        if indice == 999:
            print('Finalizando...')
            break
        else:
            print(f'As notas desse aluno foram: {boletim[indice]}')


