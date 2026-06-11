frase = str(input('Insira uma expressão: ')).strip()
direita = frase.count('(')
esquerda = frase.count(')')
if direita == esquerda:
    print('Sua expressão está correta')
else:
    print('Sua expressaõ é inválida')
