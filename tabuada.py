n = int(input('Você quer ver a tabuada de qual valor? '))
cont = 0
while cont <= 10:
    if n < 0:
        break
    cont += 1
    if cont <= 10:
        print(f'{n} x {cont} = {n * cont}')
    if cont > 10:
        n = int(input('Você quer ver a tabuada de qual valor? '))
        cont = 0
    print('~'*20)
print('~'*20)
print('O programa foi terminado com sucesso!')
