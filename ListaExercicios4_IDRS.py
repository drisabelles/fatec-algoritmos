from random import sample

valor = sample(range(100), 10)
menor = maior = valor[0]
x = 1

while x < 10:
    if valor[x] < menor: menor = valor[x]
    if valor[x] > maior: maior = valor[x]
    x = x + 1

print('Valor: ', valor)
print(f'Menor: {menor}')
print(f'Maior: {maior}')
print()



from random import sample

par = []
impar = []

valor = sample(range(100), 20)
for x in valor:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)

print('Valores: ', valor)
print('Pares: ', par)
print('Ímpares: ', impar)
print()

    

from random import randint

vetorA = []
vetorB = []
vetorC = []

for x in range(10):
    x = randint(1, 100)
    vetorA.append(x) == vetorC.append(x)
    x = randint(1, 100)
    vetorB.append(x) == vetorC.append(x)

print('Vetor A: ', vetorA)
print('Vetor B: ', vetorB)
print('Vetor C: ', vetorC)
print()



texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community
is based on mutual respect, tolerance, and encouragement, and we are
working to help each other live up to these principles. We want our
community to be more diverse: whoever you are, and whatever your
background, we welcome you.'''.lower()

import string

for i in string.punctuation:
    texto = texto.replace(i, '')

resposta = []

for letras in texto.split():
    if letras[0] in 'python' or letras[-1] in 'phyton':
        resposta.append(letras)
print('As seguinte palavras contém letras da palavra PYTHON:', resposta)
print()



texto = '''The Python Software Foundation and the global Python community
welcome and encourage participation by everyone. Our community is based
on mutual respect, tolerance, and encouragement, and we are working to
help each other live up to these principles. We want our community to be
more diverse: whoever you are, and whatever your background, we welcome
you.'''.lower()

import string

for i in string.punctuation:
    texto = texto.replace(i, '')

resposta = []
resposta4 = []

for letras in texto.split():
    if letras[0] in 'python':
        resposta.append(letras)

for letras in texto.split():
    if letras[0:5] in 'python':
        resposta4.append(letras)

print(f'Temos {len(resposta)} palavras que contém 1 letra de PYTHON')
print(f'Temos {len(resposta4)} palavras que contém 4 letras de PYTHON')
print()
  
