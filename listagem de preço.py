
print('-'*50)
print('LISTAGEM DE PREÇOS'.center(50))
print('-'*50)
# a = 'Lápis','Caderno','Mochila','Estojo','Compasso','Livro','Borracha'
# preco = 1.75,15.90,120.95,25.00,9.99,34.90,2.00
# n = 0
# digito = preco[0]
#
# for objetos in a:
#     digito = preco[n]
#     print(f'{objetos:.<40}{digito:.>5}')
#     n += 1
#     if n > len(preco)-1: #7
#         print('Lista completa')
#         break
itens = 'Lapis', 1.75,'Caderno', 15.9, 'Mochila', 120.95, 'Estojo', 25, 'Compasso',9.99, 'Livro', 34.9, 'Borracha', 2.00
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    elif pos % 2 != 0:
        print(f'R${itens[pos]:>5.2f}')


