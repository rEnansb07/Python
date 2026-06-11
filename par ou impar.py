import random as r
print('-=-'*40)
print('Jogo do Par Ou Ímpar só pro KK bb'.center(120))

cont = 0
while True:
    print('-=-' * 40)
    n = int(input('Digite um valor: '))
    setor = str(input('O que deseja [P/I]? ')).upper()
    comp = r.randint(0,11)
    print('-'*40)
    print(f'O computador escolheu {comp} e o Kaique escolheu {n}!')
    print('-'*40)
    soma = n + comp
    print(f'O resultado ficou {soma}.')
    if soma % 2 == 0 and setor == 'P':
        print('O Kaique é sigma e ganhou do computador com o poder do 67 master!')
        cont += 1
    elif soma % 2 == 0 and setor == 'I':
        print('O Kaique foi beta e perdeu para o computador!')
        break
    elif soma % 2 != 0 and setor == 'P':
        print('O Kaique foi beta e perdeu para o computador!')
        break
    elif soma % 2 != 0 and setor == 'I':
        print('O Kaique é sigma e gnahou do computador com o poder do 67 master!')
print('~~'*20)
print(f'Obrigado por jogar! O Kaique ganhou {cont} vez(es).'.center(40))

