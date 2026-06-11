print('-'*40)
print('BANCO CSV'.center(40))
print('-'*40)
valor = int(input('Qual o valor deseja sacar: R$ '))
print('-'*40)
while True:
     cedula_50 = valor // 50
     if cedula_50 > 0:
         print(f'Total de {cedula_50} cédulas de 50 reais')
     cedula_20 = (valor - cedula_50 * 50) // 20
     if cedula_20 > 0:
         print(f'Total de {cedula_20} cédulas de 20 reais')
     cedula_10 = (valor - cedula_50 * 50 - cedula_20 * 20) // 10
     if cedula_10 > 0:
         print(f'Total de {cedula_10} cédulas de 10 reais')
     cedula_5 = (valor - cedula_50 * 50 - cedula_20 * 20 - cedula_10 * 10) // 5
     if cedula_5 > 0:
         print(f'Total de {cedula_5} cédulas de 5 reais')
     moeda = (valor - cedula_50 * 50 - cedula_20 * 20 - cedula_10 * 10- cedula_5 * 5)
     if moeda > 0:
         print(f'Total de {moeda} moedas de 1 real')
     break
print('-'*40)
print('Obrigado por utilizar o caixa!'.center(40))
#120
#1: 2
#2: 120 - 2*50 = 20 // 20 = 1
#3: