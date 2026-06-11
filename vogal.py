a = 'Mercado','Planos','Misterio','Piru','Buceta','Frio'
b = ('a','e','i','o','u')
for pos in range(len(a)):
    print(f'Na palavra {a[pos]} aparece ',end=' ')
    for vogal in b:
       if vogal in a[pos]:
           print(f'{vogal}',end=' ')
    print('')
