resultado = 1
n = int(input('Insira um valor: '))
m = n
import time as t
print('-'*30)
print('Calculando o fatorial...'.center(30))
print('-'*30)
t.sleep(2)
print(m,'!',end= ' = ')
while m > 0:
    if m != 1:
        print(m,end=' x ')
    resultado *= m
    m -= 1
    if m == 1:
        print(m,end= ' = ')
print(resultado)


