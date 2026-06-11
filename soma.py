n = int(input('Digite qualquer valor ( 999 para sair): '))
a = 0
tentativas = 0
while True:
    tentativas += 1
    a += n
    n = int(input('Digite qualquer valor ( 999 para sair): '))
    if n == 999:
        break
print(f'Você digitou {tentativas} e a soma entre eles é {a}.')
