a = int(input('Insira o valor do primeiro lado: '))
b = int(input('Insira o valor do segundo lado: '))
c = int(input('Insira o valor do terceiro lado: '))

if a > b + c or b > a + c or c > a + b:
    print('Os valores não correspondem a um triângulo!')

elif a == b == c:
    print('O triângulo é um Equilátero!')

elif a == b or b == c or a == c:
    print('O triângulo é um Isóceles!')

else:
    print('O triângulo é um Escaleno!')
print()



ano = int(input('Digite o ano: '))

if ano % 4 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
print()



peso = int(input('Digite o peso do peixe pescado: '))

if peso > 50:
    excedente = peso - 50
    print(f'O excedente de peso é {excedente:.1f}kg')

    multa = excedente * 4
    print(f'O valor da multa é de R${multa:.2f}')

else:
    excedente = 0
    multa = 0
    print(f'O excedente de peso é {excedente:.1f}kg')
    print(f'O valor da multa é de R${multa:.2f}')
print()



a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

if a > b and a > c:
    print('O primeiro número é o maior deles!')

elif b > a and b > c:
    print('O segundo número é o maior deles!')

elif c > a and c > b:
    print('O terceiro número é o maior deles!')

elif a == b == c:
    print('Os três números são iguais...')
print()



a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))

if a > b and a > c:
    print('O primeiro número é o maior deles!')

elif b > a and b > c:
    print('O segundo número é o maior deles!')

elif c > a and c > b:
    print('O terceiro número é o maior deles!')  

if a < b and a < c:
    print('O primeiro número é o menor deles!')

elif b < a and b < c:
    print('O segundo número é o menor deles!')

elif c < a and c < b:
    print('O terceiro número é o menor deles!')

elif a == b == c:
    print('Os três números são iguais...')
print()



salariohora = float(input('Qual o valor que você recebe por hora? R: '))
horastrab = float(input('Quantas horas trabalha por mês? R: '))

salariobruto = salariohora * horastrab   
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - ir - inss - sindicato
print(f'+ Salário Bruto: R${salariobruto:.2f}')
print(f'- IR: R${ir:.2f}')
print(f'- INSS: R${inss:.2f}')
print(f'- Sindicato: R${sindicato:.2f}')
print(f'= Salário Líquido: R${salarioliquido:.2f}')
print()



area = int(input('Insira o tamanho da área a ser pintada: '))
mlata = 54

if area % 54 == 0:
    latas = area / 54

else:
    latas = int(area / 54) + 1

valor = latas * 80
print(f'Precisará de {latas} latas de tinta.')
print(f'O valor ficará em R${valor:.2f}')
print()
