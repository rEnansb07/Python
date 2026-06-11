lista = []
lista1 = []
n = int(input('Digite um valor: '))
while n != 0:
    lista.append(n)
    n = int(input('Digite um valor, caso deseja parar digite 0 '))
for i, v in enumerate(lista):
    if v in lista1:
        del v
    else:
        lista1.append(v)
lista1.sort()
print(lista1)

