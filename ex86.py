matriz = []
coluna = linha = cont = soma = thirdcolumn = maior = 0
for c in range(0,9):
        n = [int(input(f'Insira um valor no {linha, coluna}: '))]
        matriz.append(n)
        if matriz[c][0] % 2 == 0:
            soma += matriz[c][0]
        coluna += 1
        if coluna % 3 == 0:
            linha += 1
            coluna = 0
print('-=' * 40)
for c in range(0,9):
    if c != 0 and cont == 2:
        print(f'[ {matriz[c][0]:^3} ]\n')
        cont = 0
        thirdcolumn += matriz[c][0]

    else:
        print(f'[ {matriz[c][0]:^3} ]', end=' ')
        cont += 1

for c in range(0,9):
    if 2 < c < 6:
            if maior < matriz[c][0]:
                maior = matriz[c][0]
print('-=' * 40)
print(f'A soma dos valores pares é igual a {soma}.')
print(f'A soma de todos os valores da terceira coluna é {thirdcolumn}.')
print(f'O maior valor da segunda linha é {maior}.')