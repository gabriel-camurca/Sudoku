import os

def elementoemlista(l,y):
	cont = 0
	l.append(y)
	if len(l) == 9:
		for z in range(9):
			for w in range(z+1,9):
				if l[z] == l[w]:
					if l[z] != ' ' and cont == 0:
						print("Jogada inválida!")
						cont = 1
						l = []
						return cont

def distancialinha(a,b,l):
	l = []
	for i in range(a,b):
		for j in range(3):
			elementoemlista(l,matriz[i][j])
	l = []
	for i in range(a,b):
		for j in range(3,6):
			elementoemlista(l,matriz[i][j])
	l = []       
	for i in range(a,b):
		for j in range(6,9):
			elementoemlista(l,matriz[i][j])
	
	return

def matrizquadrantes():
	lista1 = []
	distancialinha(0,3,lista1)
	distancialinha(3,6,lista1)
	distancialinha(6,9,lista1)
	return

def print_da_matriz(x,y,z):
	print(x)
	for i in range(9):
		if i == 3 or i == 6:
			print('',y)
		else:
			print('',z)
		for j in range(9):
			if j == 0:
				print('{}|| {} |'.format(i+1,matriz[i][j]),end ='')
			elif j > 0 and j < 8:
				if j == 2 or j == 5:
					print(' {} ||'.format(matriz[i][j]), end ='')
				elif j == 7:
					print(' {} |'.format(matriz[i][j]), end ='')
				else:
					print(' {} |'.format(matriz[i][j]), end ='')
			else:
				print(' {} ||{}'.format(matriz[i][j], i+1))
		if i == 8:
			print('',z)
	print(x)
	return

def compareLinhas():
	listaL = []
	a = 0
	if a == 0:
		for i in range(9):
			for j in range(9):
				a = elementoemlista(listaL,matriz[i][j])
			listaL = []
		print(a)
		return

def compareColunas():
	listaC = []
	a = 0
	if a == 0:
		for j in range(9):
			for i in range(9):
				a = elementoemlista(listaC,matriz[i][j])
			listaC = []
		return

with open("pls.txt") as f: #Abre o arquivo e se refere ao mesmo como "f"
	s = f.readlines() #Adiciona a uma lista("s") todas as linhas de texto do documento
	s = [i.replace("\n","") for i in s] #Retira as quebras de linha
	s = [i.replace(" ","") for i in s] #Retira os espaços
	s = [i.replace(",","") for i in s] #Retira as vírgulas
	s = [i.replace(":","") for i in s] #Retira os dois pontos
#---Interface---#
l1 = "++---+---+---++---+---+---++---+---+---++"
l2 = "++===+===+===++===+===+===++===+===+===++"
l3 = '    A   B   C    D   E   F    G   H   I  '
l4 = 'ABCDEFGHI'
#---------------#

f.close #Fecha o arquivo
matriz = [[' ' for i in range(9)] for j in range(9)] #Cria uma matriz 9x9 de "''s"
x = len(s) #Lê a quantidade de elementos da lista contendo todo o texto do arquivo
for i in range(x):
	a = s[i] #Armazena o valor o "i-ésimo" elemento da lista
	a = str(a)
	k = l4.find(a[0]) #Procura nas possibilidades de letras(coordenada das colunas) a que foi digitada
	j = int(a[1])-1 #Lê a coordenada das linhas que foi inserida e diminui 1, pois o sudoku vai de 1 até 9 mas a posição é de 0 até 8, com 0 sendo o primeiro elemento e 8 o último
	matriz[j][k] = int(a[2]) #Adiciona na posição das cooordenadas k(coluna),j(linhas) o valor

print_da_matriz(l3,l2,l1)

lista_entradas = [] #Recebe as entradas do jogador
val = True #Validador de continuidade das jogadas
xx = 0

while val == True: #Loop de entrada das jogadas
	entrada = input('Entre sua jogada: ')
	entrada_correta = entrada.upper()
	if len(entrada) < 10:
		lista_entradas.append(entrada_correta) #Adiciona todas as jogadas a lista
		val = True #Continua a receber entradas
		lista_entradas = [i.replace(",","") for i in lista_entradas] #Retira as virgulas
		lista_entradas = [i.replace(":","") for i in lista_entradas] #Retira os dois pontos
		lista_entradas = [i.replace(" ","") for i in lista_entradas] #Retria os espacos # Agora a entrada esta no Formato X00
		p = len(lista_entradas) #Recebe o numero de elementos da lista de entrada
		for z in range(p): #Checagem para reconhecer onde a entrada vai ser colocada
			g = lista_entradas[z] #Recebe o elemento em questao a ser analisado
			o = l4.find(g[0]) #Procura a letra que foi entrada
			q = int(g[1]) - 1 #Procura a linha que vai ser colocada
			matriz[q][o]= int(g[2]) #Substitui o valor que foi selecionado na posicao indicada acima

		print_da_matriz(l3,l2,l1)
		compareLinhas()
		compareColunas()
		matrizquadrantes()
		
	else:
		val = False
