n = int(input('Digite um valor : ' )),int(input('Digite um valor: ' )),int(input('Digite um valor ')), int(input('Digite um valor: '))
print('A quatidade de vezes em que o número 9 apareceu foi: ',n.count(9))
lista = []
listai = []
if 3 in n:
    print('A posição do primeiro número 3 é: ',n.index(3)+1)
print('Os números pares são: ',end='')
for i, v in enumerate(n):
    if v % 2 == 0 and i is not len(n)-1:
        print(f'{v} ', end='')
    elif v % 2 == 0 and i is len(n)-1:
        print(f'{v} ', end=' Fim ')

# O que eu queria tentar fazer era com que se o último número ja tivesse aparecido na tupla, o computador omitisse ele e escreveria fim








