import random, time
verificacao = []
maioridade = []
tabela = list()
jogadores = dict()
for c in range(0,4):
    n = str(input('Nome: '))
    jogadores[n] = random.randint(1, 6)
tabela.append(jogadores)
# não precisei colocar o método de copy no dicionario porque eu ja coloquei o que deveria ser o input do indice jogador sendo o nome do jogador ja como indice
   # if c == 3:
     #del tabela[:3]
for k,v in jogadores.items():
        print(f'O jogador {k} tirou o valor {v}')
        maioridade.append(v)
        maioridade.sort(reverse=True)

print('-=' * 30)
print('A classificação ficou: ')
for indice, ref in enumerate(maioridade): #renan: 4 e felipe: 4 e renata: 6
        encontrou = False
        for k, v in jogadores.items():
            time.sleep(1)
            if encontrou:
                break
            elif ref == v and k not in verificacao: #evitar repeticao
                print(f'{indice+1}º jogador: {k} tirou {v} no dado.')
                verificacao.append(k)

                break
            else:
                        for k2, v2 in jogadores.items():
                            time.sleep(1)
                            if ref == v2 and k2 not in verificacao:
                                print(f'{indice+1}º jogador: {k2} tirou {v2} no dado.')
                                verificacao.append(k2)
                                encontrou = True
                                break
print(tabela)