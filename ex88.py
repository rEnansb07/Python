import random, time
num = list()
print('--' * 20)
print('\033[31mMEGA SENA\033[m'.center(40))
print('--' * 20)
jogos = int(input('Quantos jogos deseja jogar? '))
for tabelas in range(1, jogos + 1):
    for numeros in range(0,6):
        n = random.randint(1,60)
        if n in num:
            m = n
            del n
            while m in num:
                m = random.randint(1,60)
                if m not in num:
                    num.append(m)
                    break
        else:
            num.append(n)
    coleta = sorted(num[:])
    num.clear()
    print(f'Jogo {tabelas}: {coleta}')
    time.sleep(1)

