n = int(input('Um valor: '))
m = n
resultado = 1
#for c in range(m,0,-1):
    #print(c)
    ##resultado *= c
#print(resultado)
while m > 0:
    print(m,end='x')
    resultado *= m
    m -= 1
print('\n')
print(end='=')
print(resultado)



#4x3x2x1 = 24