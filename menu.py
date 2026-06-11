n, m = map(int, input('Digite dois números separando-os por espaço: ').split())
b = ''
while b != 5:
    b = int(input(' [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Novos números \n [5] Sair \n'))
    if b == 1:
        soma = n + m
        print(f'A soma desses números resulta em {soma}')
    if b == 2:
        multiplicar = n * m
        print(f'A multiplicação é igual a {multiplicar}')
    if b == 3:
        if n > m:
            maior = n
            print(f'O maior número é {maior}')
        elif n < m:
            maior = m
            print(f'O maior número selecionado foi {maior}')
        else:
            print('Os numeros são iguais')
    if b == 4:
        print('Ok, escolha outros dois números que deseja!')
        n, m = map(int,input('Números separados por espaço: ' ).split())
    if b == 5:
        print('Saindo do programa')
