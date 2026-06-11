boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['Media'] = float(input(f'Média do {boletim["nome"]}: '))
if boletim['Media'] > 6.0:
    boletim['Situaçao'] = 'Aprovado'
else:
    boletim['Situaçao'] = 'Reprovado'
for k, v in boletim.items():
    print(f'{k} é igual a {v}')
