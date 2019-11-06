#Exercício 1
n = int (input('Digite uma nota: '))
while n <0 or n > 10:
    print(f'Valor inválido')
    n= int(input('Digite outra nota: '))

#Exercício 2

u = input(f'Digite o usuário: ')
s = input (f'Digite a senha: ')
while u==s:
    print(f'Usuário e senha inválidos.')
    u = input ('Digite o usuário: ')
    s = input ('Digite a senha: ')
if u != s:
    print (f'Usuário cadastrado com sucesso.')

#Exercício 3

a = 80000
b = 200000
ac = 0 #anos
while a < b:
    a = a*1.03
    b = b*1.015
    ac = ac + 1
print (f'Anos necessários para que país A ultrapasse ou iguale a população de B: {ac} anos')

#Exercício 4

n = int(input(f'Digite um número: '))
a,b = 1,1
ac = 1
while ac <= n-2:
a,b=b,a+b
ac = ac + 1

#Exercício 5
n1 = int(input(f'Digite o primeiro número: '))
n2 = int(input(f'Digite o segundo número: '))
if n1>n2:
    while n1 % n2 != 0:
        n1,n2=n2,n1%n2
    print(f'O MDC é {n2}')
elif n2>n1:
    while n2% n1 != 0:
        n2,n1 = n1, n2%n1
    print (f' O MDC é {n1}')
else:
    print(f'O MDC é {n1}')
