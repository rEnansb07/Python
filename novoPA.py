a = 0
numero = int(input('Digite um valor para demonstrar a PA: '))
numero1 = numero
razao = int(input('Digite a razão da PA: '))
import time as s
print('Analisando...')
s.sleep(2)
while numero < numero1 + 9 * razao:
    a += 1
    print(numero, ' ->', end=' ')
    numero += razao
    s.sleep(0.5)
print(numero1 + 9 * razao,'-> FIM')
numero = numero1 + 9 * razao
numero1 = numero
t = int(input('Quantos termos deseja analisar a mais? '))
razao1 = razao
while t != 0 and numero < numero1 + t * razao:
    a += 1
    numero += razao
    if numero == numero1 + t * razao:
        print(numero,'-> FIM')
        numero1 = numero
        t = int(input('Quantos termos deseja analisar a mais? '))
    elif numero < numero1 + t * razao:
        print(numero, '->', end= ' ')
        s.sleep(0.5)
print(a+1)




