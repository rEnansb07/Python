n = int(input('Digite qualquer valor: '))
a = str(input('Deseja sair? [S/N] ')).upper()
b = c = 0
maior = menor = n
while a == 'N':
    c += 1
    b += n
    n = int(input('Digite qualquer valor: '))
    a = str(input('Deseja sair? [S/N] ')).upper()
    if maior < n :
        maior = n
        if menor > n:
            menor = n
print(f'A média entre os valores é igual a {b / c:.2f} e o maior valor = {maior} e o menor valor = {menor}.')
