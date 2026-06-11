lista = []
n = int(input('Digite um valor: '))
lista.append(n)
while True:
    validacao = str(input('Quer continuar? [S/N] '))
    if validacao.upper() == 'S':
        n = int(input('Digite um valor: ' ))
        lista.append(n)
    else:
        break
print('-'*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 faz parte da lista.')