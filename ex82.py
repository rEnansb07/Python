lista = []
lista_par = []
lista_impar =[]
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    m = str(input('Quer continuar? '))
    if m.upper() == 'N':
        break
for item in lista:
    if item % 2 == 0:
        lista_par.append(item)
    else:
        lista_impar.append(item)
print(lista)
print(lista_impar)
print(lista_par)