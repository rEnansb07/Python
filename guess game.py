import random as r
t = 10
j = r.randint(1,100)
print('-='*50)
print('Jogo das adivinhações'.center(100))
print('Tente adivinhar antes que suas tentativas acabem! VOCÊ tem 5 tentativas:')
n = ''
while t >= 0  and n != j:
    t = t - 1
    n = int(input('Tente adivinhar...'))
    if n == j:
        print('Você é sigma boy!')
    else:
        print('Muito burro kkkkk')
    if t >= 0:
        print(t)
print('Fim do jogo')
