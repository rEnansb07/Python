n = ''

while n != 'M' and n != 'F':
     n = str(input('Qual o seu sexo[M/F]: ')).upper().strip()
     if n != 'M' and n != 'F':
       print('Você está escrevendo sem se adequar às especificações')
     else:
       print('Obrigado!')

#else:
    #print('Escreva novamente')



