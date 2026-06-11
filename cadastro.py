homens = contador = mulheres = velha = 0
nomefinal = ''
while True:
    print('-'*30)
    print('CADASTRO'.center(15))
    print('-'*30)
    nome = str(input('Nome: '))
    i = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    continuar = str(input('Continuar [S/N]? ')).upper()
    if i > 18:
        contador += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if i > velha:
            velha = i
            nomefinal = nome
        if i >= 20:
            mulheres += 1
    if continuar == 'N':
        break
print(f'Obrigado por finalizar o cadastro! De acordo com os dados existem {contador} pessoas maiores de 18 anos, {homens} homens, {mulheres} mulheres com mais de 20 anos e o nome da mais velha é {nomefinal} com {velha} anos de idade')
