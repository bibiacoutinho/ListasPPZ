##Exercício 1
from random import randint
lista = []
for número in range (10):
    lista.append(randint(1,100)) ##escolhe 10 numeros entre 1-99 aleatoriamente e adiciona na lista
menor = lista[0]#insere primeiro elemento da 'lista' no 'menor'
maior = lista[0]#insere primeiro elemento da 'lista' no 'maior'
for c in range(10): #o contador 'c' começa com 0. o 'c' é a posição do elemento na 'lista[c]' (equivale ao conjunto 'lista'), ele vai variar de 0 a 9
    if menor >= lista[c]: #comparando elemento zero da 'lista' com elemento zero da 'lista[c]' (lista[c] é cópia da 'lista')
        menor = lista[c]
    if maior <= lista[c]: #comparando elemento zero da 'lista' com elemento zero da 'lista[c]'
        maior = lista[c] #vai retornar agora 'c' somando +1, assim a lista[c] vira o próximo elemento aleatório
                         #na ordem para comparar com os elementos atuais em 'maior' e 'menor'
        ##em resumo vamos comparar cada elemento da 'lista' criada com numeros aleatorios com cada elemento da 'lista[c]' (equivalente ao conjunto 'lista')
print (f'''Lista: {lista}
Maior elemento: {maior}
Menor elemento: {menor}''')


##Exercício 2
from random import randint
listatodos = []#criei uma lista vazia
for numeros in range(20):#sorteia 20 numero aleatorios
    listatodos.append(randint(1,100))#entre 1-99 e adiciona na 'listatodos'
pares = [] #cria uma lista 'pares' vazia
impares = [] #cria uma lista ' impares' vazia
for c in range (20): #'c' começa com zero
    if listatodos[c]%2==0:#verificando se posição 'c' da 'listatodos' é divisivel por 2
        pares.append(listatodos[c]) #se sim, é incluído na lista pares
    if listatodos[c]%2!=0:#verificando se posição 'c' da 'listatodos' não é divisivel por 2
        impares.append(listatodos[c])#se sim, é incluído na lista impares
        ##programa entra em looping para 'c' variar de 0-19 (posição 0-19)
print (f'''Todos: {listatodos}
Pares: {pares}
Ímpares: {impares}''')


##Exercício3
from random import randint
vetor1 = []#criei lista vazia
for n in range(10):#sortiei 10 numeros
    vetor1.append(randint(1,100))#entre 1-99
vetor2 = []#criei lista vazia
for n in range(10):#sortiei 10 numeros
    vetor2.append(randint(1,100))#entre 1-99
vetor3 = []#criei lista vazia
for c in range(10):#contador 'c' vai variar de 0-9
    vetor3.append(vetor1[c])#começa adicionando com elemento do vetor1, 'c' posição equivalente do 'vetor1'
    vetor3.append(vetor2[c])#em seguida adiciona elemento do vetor2, 'c' posição equivalente do 'vetor2'
    #programa entra em looping até ter as 10 posições de cada vetor na lista com 20 elementos
print (f'''Vetor 1: {vetor1}
Vetor 2: {vetor2}
Vetor 3: {vetor3}''')


##Exercício 4
texto = '''The Python Software Foundation and the global Python community
welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each
other live up to these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you'''
texto = texto.lower()#transformar todas as letras em minusculas
texto = texto.replace('.',' ').replace(':',' ').replace(',',' ')#tirar caracteres especiais
texto = texto.split()#transformar cada palavra em um elemento de uma lista
lista = []#criei uma lista vazia
for p in texto:#para cada palavra (='p') no 'texto'
    if p[0]in 'python' or p[-1]in'python':#se a primeira letra ou última está contida no conjunto 'python'
        lista.append(p)#se verdadeiro, adiciona esse elemento/palavra (= 'p') na 'lista'
print(f'''Palavras em que a primeira ou última letra estão
contidas na palavra ''python'': {lista}''')


##Exercício 5
texto = '''The Python Software Foundation and the global Python community
welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each
other live up to these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you'''
texto = texto.lower()#transformar todas as letras em minusculas
texto = texto.replace('.',' ').replace(':',' ').replace(',',' ')#tirar caracteres especiais
texto = texto.split()#transformar cada palavra em um elemento de uma lista
def contempython(palavra):#criando uma função
  for letra in palavra:#pra ada letra de palavra
    if letra in 'python':#se a letra estiver contida em python
      return True #verdade: memoriza a palavra
  return False #falso: descarta a palavra
lista = []#criei lista vazia
for p in texto:#para cada elemento em texto
    if len(p) > 4 and contempython(p):#se o elemento ter mais de 4 letras e atender a função
        lista.append(p)#adicione a palavra na lista vazia
print(f'O número de palavras é {len(lista)}.')
