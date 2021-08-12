nota = float(input('Insira uma nota: '))
while nota < 0 or nota > 10:
    print('Valor inválido, apenas números ente 0 e 10!')
    nota = float(input('Insira uma nota: '))

if nota >= 0 or nota <= 10:
    print('Valor aceito, obrigada!')
print()



usuario = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

while usuario == senha:
    print('Dados inválidos! O nome de usuário e senha não pode ser iguais!')
    usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
print()



a = 80000
b = 200000
anos = 0

while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1
print(anos)
print()



n = int(input('Digite um número: '))

a = b = 1
f = 1

while f <= n - 2:
    a, b = b, a + b
    f = f + 1
print(b)
print()



a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

while a % b != 0:
    a, b = b, a % b
    
print('O MDC dos números citados é', b)
print()





