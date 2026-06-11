from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados ['Carteira de Trabalho'] == 0:
    print('-='*30)
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
        print('-=' * 30)
        dados['Ano de Contratação'] = int(input('Ano de contratação: '))
        dados['Salário '] = int(input('Salário: '))
        dados['Aposentadoria'] = 65 - dados['Idade']
        for k, v in dados.items():
                print(f'{k} tem o valor {v}')


