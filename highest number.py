import math as m
n = float(input('peso da 1ª pessoa: '))
a = 1
maior = n
menor = n
for c in range(1,5):
    a += 1
    n = float(input(f'Peso da {a}ª pessoa: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    m.ceil(n)
print(f'O maior peso da lista é {maior:.2f}kg e o menor é {menor:.2f}kg)')
