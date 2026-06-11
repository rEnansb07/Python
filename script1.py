import time as s
n = int(input('Digite quantos termos da sequencia de Fibonacci deseja verificar: '))
constante = n
a = 1
b = 0
lista = []
c = 0
while constante > 0:
    print(b, '->',end= ' ')#0 #2 #8
    constante = constante - 1
    lista.append(b)
    if constante == 0:
        print('FIM')
        break
    print(a, '->',end=' ')#1 #3 #11
    constante = constante - 1
    lista.append(a)
    if constante == 0:
        print('FIM')
        break
    print(a+b, '->',end=' ')#1 #5
    constante = constante - 1
    lista.append(a+b)
    if constante == 0:
        print('FIM')
        break
    c = a + b
    b = a + b + a
    a = b + c
    s.sleep(1)
print(lista[n-1])

