#Exercício 1
numero1 = int(input ('Primeiro número:'))
numero2 = int(input ('Segundo numero:'))
print(numero1 + numero2)

#Exercício 2
metros = float(input ('Insira valor em metros: '))
milimetros = metros*1000
print (f' O valor corresponde a {milimetros}mm')

#Exercício 3
d = int (input(f'Insira o valor de dias:'))
h = int (input(f'Insira o valor de horas:'))
m = int (input(f'Insira o valor de minutos:'))
s = int (input(f'Insira o valor de segundos:'))

total = (d*86400)+(h*3600)+(m*60)+s
print (f'Esse valor corresponde a {total} segundos')

#Exercício 4
salário = float (input('Salário: '))
porcentagem = float (input('Aumento em porcentagem:'))
n = porcentagem
aumento = salário * n/100
novo = salário + aumento
print (f' Seu novo salário é de {novo}')

#Exercício 5
valor = float (input ('Insira preço da mercadoria:'))
porcentagem = float (input('Insira desconto em porcentagem:'))
desconto = valor * porcentagem/100
novo = valor - desconto
print (f'Preço atual da mercadoria é de {novo} reais, Você obteve o desconto de {desconto} reais')

#Exercício 6
distância = float (input('Insira a distância a ser percorrida em km:'))
velocidade = float (input('Insira velocidade média da viagem em km/h:'))
tempo = distância/velocidade
print (f'O tempo estimado de sua viagem é de {tempo:.2f} hora(s)')

#Exercício 7
celsius = float (input('Insira temperatura em ºC:'))
f = 9*celsius/5 + 32
print (f' A temperatura corresponde a {f}ºF')

#Exercício 8
f = float (input (' Insira a temperatura em ºF: '))
c =  (f-32) * 5/9
print ( f' A temperatura em ºC é: {c}')

#Exercício 9
d =  int(input (' Por quantos dias  o carro foi alugado: '))
km = int( input (' Quantos Km foram percorridos: '))
calculo1 = d * 60
calculo2 = km * 0.15
valor = calculo1 + calculo2
print ( f' O valor á ser pago é : {valor}')

#Exercício 10
c = int(input(f'Quantos cigarros são fumados por dia?:'))
a = int(input(f'Em anos, quantos anos você já fumou?:'))
ca = c*a*365 #calcular quantidade de cigarro total já foram fumados até agora
m = ca*10 #calcular perda de vida total em minutos
d = m/1440 #calcular quantos dias de vida foram perdidos
print (f'Você já perdeu {d:.1f} dias de vida para o cigarro. Pare de fumar. Ligue 136.')

#Exercício 11
valor = len(str(2**1000000))
print (valor)
