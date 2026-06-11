lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print(f'o maior valor digitado foi {max(lista)} na posição {lista.index(max(lista))+1} e o menor {min(lista)} na posição {lista.index(min(lista))+1}')