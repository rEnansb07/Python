n = int(input('Insira um valor para calcular a PA: '))
r = int(input('Insira a razão da PA: '))
R = 9 * r
b = n
a = n + R
print(f'Ordem dos termos: {n} ->',end=' ')
import time as s
s.sleep(0.5)
while n != (b + R):
    s.sleep(0.1)
    n += r
    if n < (b + R):
        print(n,end=' -> ')
print(n,end=' -> PAUSA')
print('\n','-='*20)
t = int(input('Quantos termos você deseja mostrar a mais? '))
T = r * t
print(a + T)
if t == 0:
    print('FIM')
else:
    while t != 0: # n = 26

        s.sleep(1)
        n += r
        if n > (a + T):       #ele vai ver n é igual a 26 e não mais o limite de 24, então agoro a = 26 + r * t -2 (quero ver 26 e 28 escrito)
            z = n
            a = z - r
            print(f'///o valor de a é {a}/// e o valor de n é {n}///')
            if n < (a + T):
                print(f'{n} =>',end= ' ')
            if n == (a + T):
                print(f'{n} =>',end= 'PAUSA')
                t = int(input('1Quantos termos deseja mostrar a mais? '))



        elif n < (a + T):                                      #o problema é que o a continua sendo o decimo termo da sequencia
            print(f'{n} -> ',end=' ')
        elif n == (a + T):
            print(f'{n} -> PAUSA',    f'{a + T}')
            t = int(input('2Quantos termos deseja mostrar a mais? '))
        #if n == (a + T):  # n = 24
            #t = int(input('Quantos termos deseja mostrar a mais? ')) #escreva 26 e 28 e pare
