pessoas = 0
dados = list()
peso = list()
bancopeso = list()
nomes = list()
nomes2 = list()
while True:
    dados.append(str(input('Qual o nome: ' )))
    dados.append(int(input('Qual o peso: ')))
    bancopeso.append(dados[:])
    dados.clear()
    pessoas += 1
    sn = str(input('Quer continuar? [S/N] '))
    if sn in 'Nn':
        break
for p in bancopeso:
    peso.append(p[1])
maximo = max(peso)
minimo = min(peso)
for p in bancopeso:
    if maximo in p:
        nomes.append(p[0])
    elif minimo in p:
        nomes2.append(p[0])
print(f'Foram cadastradas {pessoas} pessoas.')
print(f'O maior peso foi de {max(peso)} Kg e seu(s) nome(s) são {nomes}')
print(f'O menor peso foi de {min(peso)} Kg e seu(s) nome(s) são {nomes2}')













