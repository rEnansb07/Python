velhas = 0
mulher = 20
f = 1
idade = 0
m = 0
lista = []
lista1 = []
maior = idade
for c in range(1,5):
    et = lista1
    print('-=-'*20,f'{f}ª pessoa','-=-'*20)
    f += 1
    n = str(input('Qual é o seu nome? '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    print('-=-'*20)
    m += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
    elif sexo == 'F':
        if idade < 20:
            velhas += 1





    lista.append(n)
    lista1.append(idade)
k = lista1.index(maior)
#print(lista[k])
print(f'O homem mais velho é {lista[k]} e possui {maior} anos.')
print(f'A quantidade de mulheres menores que 20 anos é {velhas}')





print(m/4)

