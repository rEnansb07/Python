

lista = []
lista1 = []
menor = 0
n = int(input('Digite um valor: '))
while n != 999:
    lista.append(n)
    n = int(input('Digite um valor: ')) #lista já está com os valores adiconados
for item in lista:
    if item in lista1:
        del item
    else:
        lista1.append(item)
c = min(lista1)

lista1.pop(lista1.index(c))
lista1.insert(0,c) #o menor valor já está no inicio
print(lista1)
lista = []
for i, v in enumerate(lista1):
    if i == 0 or v > lista[-1]:
        lista.append(v)
    else:
        for i, x in enumerate(lista):
            if v < x:
                lista.insert(i, v)
                break
#10,8,9,11


print(lista)
