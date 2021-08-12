a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
total = a + b
print ('O total da soma é: ', total)
print()

metros = int(input('Digite o número de metros que deseja converter: '))
milimetros = metros * 1000
print('O valor de metros convertido em milimetros é ', milimetros)
print()

d = int(input('Digite o número de dias: '))
h = int(input('Digite o número de horas: '))
m = int(input('Digite o número de minutos: '))
s = int(input('Digite o número de segundos: '))
total = (d*24*60*60) + (h*60*60) + (m*60) + s
print('O total de segundos é: ', total)
print()

sAtual = float(input('Digite o valor do salário: '))
p = float(input('Digite o valor da porcentagem do aumento: '))
aumento = sAtual*(p/100)
sAcresc = sAtual + aumento
print(f'O valor do aumento será de R${aumento:.2f}')
print(f'O salário com aumento será de R${sAcresc:.2f}')
print()

pAtual = float(input('Digite o valor do produto: '))
d = float(input('Digite o valor da porcentagem do desconto: '))
desconto = pAtual*(d/100)
pDesc = pAtual - desconto
print(f'O valor do desconto será de R${desconto:.2f}')
print(f'O valor do produto com desconto será de R${pDesc:.2f}')
print()

d = float(input('Qual é a distância a ser percorrida em km? R: '))
vm = int(input('Qual é a velocidade na qual pretende percorrer a viagem? R: '))
t = d / vm
print(f'O tempo que levará para chegar ao destino será de {t:.1f}h')
print()

C = float(input('Digite a temperatura em graus Celsius: '))
F = (9*C/5) + 32
print(f'A temperatura convertida em Fahreinheit é {F:.1f}')
print()

F = float(input('Digite a temperatura em graus Fahrenheit: '))
C = (F - 32) * 5/9
print(f'A temperatura convertida em Celsius é {C:.1f}')
print()

kmper = float(input('Digite a quantidade de km peercorridos: '))
dias = int(input('Digite o número de dias pelos quais o carro foi alugado: '))
total = (kmper*(3/20)) + (dias*60)
print(f'O valor total do aluguel do carro ficará em R${total:.2f}')
print()

qcig = int(input('Qual a quantidade de cigarros fumados por dia? R: '))
anos = int(input('Há quantos anos fuma? R: '))
tcig = (anos * 365)* qcig
diasp = tcig / 144
print(f'A quantidade de dias perdidos é igual a {diasp:.1f}')
print()

print(len(str(2**1000000)))
print ()






