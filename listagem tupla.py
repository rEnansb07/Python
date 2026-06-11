import random as r
maior = 0
a = r.randint(0,50)
b = r.randint(0,50)
c = r.randint(0,50)
menor = a
lista = [a,b,c]
tupla = tuple(lista)
for n in tupla:
        if maior < n:
            maior = n
        if menor > n:
            menor = n



print(tupla,end=' ')
print(f'O maior número da tupla é {maior} e o menor é {menor}.')
