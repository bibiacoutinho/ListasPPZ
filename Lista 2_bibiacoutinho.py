##Exercício 1
a = int(input('Lado 1: '))
b = int(input('Lado 2: '))
c = int(input('Lado 3: '))

if a<b+c or b<a+c or c<b+c:
    print (f' Os lados informados formam um triângulo')
    if a==b==c: ##essa condição so será executada caso os lados formem um triângulo
        print (f' O triângulo é equilátero')##por isso há indentação (paragrafo) antes
    elif a==b or b==c or a==c: ##elif é escrito para uma segunda condição
        print(f' O triângulo é isósceles')
    else:
        print(f' O triângulo é escaleno')    
else:
    print(f' Os lados informados não formam um triângulo')


##Exercício 2
ano = int(input(f'Insira o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print (f' Esse ano é bissexto')
else:
    print (f' Esse ano não é bissexto')


##Exercício 3
peso = int(input(f'Insira, em kg, a quantidade de peixe: '))
excesso = peso-50
if excesso >= 0:
    multa = excesso * 4
    print(f'Peso em excesso é de {excesso}kg. Multa é de R${multa:.2f}')
else:
    print(f'Peso em excesso é de 0kg. Multa é de R$0.00')


##Exercício 4
a = int(input(f'Número 1: '))
b = int(input(f'Número 2: '))
c = int (input(f' Número 3: '))
maior = max(a,b,c)
print (f'O maior número é {maior}')


##Exercício 5
a = int(input(f'Número 1: '))
b = int(input(f'Número 2: '))
c = int (input(f' Número 3: '))
maior = max(a,b,c)
menor = min(a,b,c)
print (f'O maior número é {maior} e o menor é {menor}')


##Exercício 6
v = float(input(f'Valor por hora: '))
h = float(input(f'Horas trabalhadas no mês:'))
sb = v*h
ir = sb *0.11
inss = sb*0.08
sind = sb*0.05
d = ir + inss + sind
sl = sb - d
print(f'Salário bruto: R${sb:.2f}')
print (f'IR: R$ {ir:.2f}')
print(f'INSS: R${inss:.2f}')
print (f'Sindicato: R${sind:.2f}')
print (f'Salário Líquido: R${sl:.2f}')


##Exercício 7
a = int(input(f'Área a ser pintada, em m²:'))
#uma lata pinta 54 metros quadrados (3*18)
if a % 54 ==0:
    latas = int(a/54) #se resto = 0, latas = quociente inteiro
else:
    latas = int(a/54 +1) #se resto != 0, latas = quociente inteiro + 1
valor = latas*80         #parte quebrada do quociente é desprezado
print(f'Você precisa de {latas} latas de tinta, preço total R${valor:.2f}')
