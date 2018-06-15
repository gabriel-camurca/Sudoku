import os

def limpar_lista(x):
	x = x
	x = [i.replace("\n","") for i in x]
	x = [i.replace(" ","") for i in x] #Retira os espaços
	x = [i.replace(",","") for i in x] #Retira as vírgulas
	x = [i.replace(":","") for i in x] #Retira os dois pontos
	return x

listaValidador0 = [] #Cria varias listas para cada linha da matriz
listaValidador1 = []
listaValidador2 = []
listaValidador3 = []
listaValidador4 = []
listaValidador5 = []
listaValidador6 = []
listaValidador7 = []
listaValidador8 = []

listaValidadorC0 = [] #Cria varias listas para cada coluna da matriz
listaValidadorC1 = []
listaValidadorC2 = []
listaValidadorC3 = []
listaValidadorC4 = []
listaValidadorC5 = []
listaValidadorC6 = []
listaValidadorC7 = []
listaValidadorC8 = []

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
matriz = [[0 for i in range(9)] for j in range(9)] #Cria uma matriz 9x9 de 0s
x = len(s) #Lê a quantidade de elementos da lista contendo todo o texto do arquivo
for i in range(x):
	a = s[i] #Armazena o valor o "i-ésimo" elemento da lista
	a = str(a)
	k = l4.find(a[0]) #Procura nas possibilidades de letras(coordenada das colunas) a que foi digitada
	j = int(a[1])-1 #Lê a coordenada das linhas que foi inserida e diminui 1, pois o sudoku vai de 1 até 9 mas a posição é de 0 até 8, com 0 sendo o primeiro elemento e 8 o último
	matriz[k][j] = int(a[2]) #Adiciona na posição das cooordenadas k(coluna),j(linhas) o valor

	if k == 0: #Coloca os elementos das linhas da matriz base nas suas respectivas listas
		listaValidador0.append(a[2])
	if k == 1:
		listaValidador1.append(a[2])
	if k == 2:
		listaValidador2.append(a[2])
	if k == 3:
		listaValidador3.append(a[2])
	if k == 4:
		listaValidador4.append(a[2])
	if k == 5:
		listaValidador5.append(a[2])
	if k == 6:
		listaValidador6.append(a[2])
	if k == 7:
		listaValidador7.append(a[2])
	if k == 8:
		listaValidador8.append(a[2])

	if a[0] == "A": #Coloca os elementos das colunas da matriz base nas suas respectivas listas
		listaValidadorC0.append(a[2])
	if a[0] == "B":
		listaValidadorC1.append(a[2])
	if a[0] == "C":
		listaValidadorC2.append(a[2])
	if a[0] == "D":
		listaValidadorC3.append(a[2])
	if a[0] == "E":
		listaValidadorC4.append(a[2])
	if a[0] == "F":
		listaValidadorC5.append(a[2])
	if a[0] == "G":
		listaValidadorC6.append(a[2])
	if a[0] == "H":
		listaValidadorC7.append(a[2])
	if a[0] == "I":
		listaValidadorC8.append(a[2])

print(l3)
for i in range(9):
	if i == 3 or i == 6:
		print('',l2)
	else:
		print('',l1)
	for j in range(9):
		if j == 0:
			print('{}|| {} |'.format(i+1,matriz[i][j]),end ='')
		elif j > 0 and j<8:
			if j == 2 or j == 5:
				print(' {} ||'.format(matriz[i][j]), end ='')
			elif j == 7:
				print(' {} |'.format(matriz[i][j]), end ='')
			else:
				print(' {} |'.format(matriz[i][j]), end ='')
		else:
			print(' {} ||{}'.format(matriz[i][j], i+1))
	if i == 8:
		print('',l1)
print(l3)

lista_entradas = [] #Recebe as entradas do jogador
val = True #Validador de continuidade das jogadas

while val == True: #Loop de entrada das jogadas
	booole = False
	entrada = input('Entre sua jogada: ')
	xy = entrada.upper()
	if len(entrada) < 10:
		lista_entradas.append(xy) #Adiciona todas as jogadas a lista
		val = True #Continua a receber entradas
		p = len(lista_entradas)
		lista_entradas = [i.replace(",","") for i in lista_entradas] #Retira as virgulas
		lista_entradas = [i.replace(":","") for i in lista_entradas] #Retira os dois pontos
		lista_entradas = [i.replace(" ","") for i in lista_entradas] #Retria os espacos # Agora a entrada esta no Formato X00
		for z in range(p): #Checagem para reconhecer onde a entrada vai ser colocada
			g = lista_entradas[z] #Recebe o elemento em questao a ser analisado
			o = l4.find(g[0]) #Procura a letra que foi entrada
			q = int(g[1]) - 1 #Procura a linha que vai ser colocada

		g = lista_entradas[z]
		q = int(g[1]) - 1

		#LINHA VALIDADOR
		if q == 0: #Analisa em qual linha o elemento esta e o coloca em sua respectiva lista
			listaValidador0.append(g[2])
		elif q == 1:
			listaValidador1.append(g[2])
		elif q == 2:
			listaValidador2.append(g[2])
		elif q == 3:
			listaValidador3.append(g[2])
		elif q == 4:
			listaValidador4.append(g[2])
		elif q == 5:
			listaValidador5.append(g[2])
		elif q == 6:
			listaValidador6.append(g[2])
		elif q == 7:
			listaValidador7.append(g[2])
		elif q == 8:
			listaValidador8.append(g[2])

		for x in range(len(listaValidador0)): #Comparacao dos valores de cada lista
			for y in range(x+1, (len(listaValidador0))):
				if listaValidador0[x] == listaValidador0[y]: 
					booole = True
					listaValidador0.pop()
		for x in range(len(listaValidador1)):
			for y in range(x+1, (len(listaValidador1))):
				if listaValidador1[x] == listaValidador1[y]:
					booole = True
					listaValidador1.pop()
		for x in range(len(listaValidador2)):
			for y in range(x+1, (len(listaValidador2))):
				if listaValidador2[x] == listaValidador2[y]:
					booole = True
					listaValidador2.pop()
		for x in range(len(listaValidador3)):
			for y in range(x+1, (len(listaValidador3))):
				if listaValidador3[x] == listaValidador3[y]:
					booole = True
					listaValidador3.pop()
		for x in range(len(listaValidador4)):
			for y in range(x+1, (len(listaValidador4))):
				if listaValidador4[x] == listaValidador4[y]:
					booole = True
					listaValidador4.pop()
		for x in range(len(listaValidador5)):
			for y in range(x+1, (len(listaValidador5))):
				if listaValidador5[x] == listaValidador5[y]:
					booole = True
					listaValidador5.pop()
		for x in range(len(listaValidador6)):
			for y in range(x+1, (len(listaValidador6))):
				if listaValidador6[x] == listaValidador6[y]:
					booole = True
					listaValidador6.pop()
		for x in range(len(listaValidador7)):
			for y in range(x+1, (len(listaValidador7))):
				if listaValidador7[x] == listaValidador7[y]:
					booole = True
					listaValidador7.pop()
		for x in range(len(listaValidador8)):
			for y in range(x+1, (len(listaValidador8))):
				if listaValidador8[x] == listaValidador8[y]:
					booole = True
					listaValidador8.pop()

		#COLUNA VALIDADOR
		if g[0] == "A": #Analisa em qual coluna o elemento esta e o coloca em sua respectiva lista
			listaValidadorC0.append(g[2])
		elif g[0] == "B":
			listaValidadorC1.append(g[2])
		elif g[0] == "C":
			listaValidadorC2.append(g[2])
		elif g[0] == "D":
			listaValidadorC3.append(g[2])
		elif g[0] == "E":
			listaValidadorC4.append(g[2])
		elif g[0] == "F":
			listaValidadorC5.append(g[2])
		elif g[0] == "G":
			listaValidadorC6.append(g[2])
		elif g[0] == "H":
			listaValidadorC7.append(g[2])
		elif g[0] == "I":
			listaValidadorC8.append(g[2])

		for x in range(len(listaValidadorC0)):
			for y in range(x+1, (len(listaValidadorC0))):
				if listaValidadorC0[x] == listaValidadorC0[y]:
					booole = True
					listaValidadorC0.pop()
		for x in range(len(listaValidadorC1)):
			for y in range(x+1, (len(listaValidadorC1))):
				if listaValidadorC1[x] == listaValidadorC1[y]:
					booole = True
					listaValidadorC1.pop()
		for x in range(len(listaValidadorC2)):
			for y in range(x+1, (len(listaValidador2))):
				if listaValidadorC2[x] == listaValidadorC2[y]:
					booole = True
					listaValidadorC2.pop()
		for x in range(len(listaValidadorC3)):
			for y in range(x+1, (len(listaValidadorC3))):
				if listaValidadorC3[x] == listaValidadorC3[y]:
					booole = True
					listaValidadorC3.pop()
		for x in range(len(listaValidadorC4)):
			for y in range(x+1, (len(listaValidadorC4))):
				if listaValidadorC4[x] == listaValidadorC4[y]:
					booole = True
					listaValidadorC4.pop()
		for x in range(len(listaValidadorC5)):
			for y in range(x+1, (len(listaValidadorC5))):
				if listaValidadorC5[x] == listaValidadorC5[y]:
					booole = True
					listaValidadorC5.pop()
		for x in range(len(listaValidadorC6)):
			for y in range(x+1, (len(listaValidadorC6))):
				if listaValidadorC6[x] == listaValidadorC6[y]:
					booole = True
					listaValidadorC6.pop()
		for x in range(len(listaValidadorC7)):
			for y in range(x+1, (len(listaValidadorC7))):
				if listaValidadorC7[x] == listaValidadorC7[y]:
					booole = True
					listaValidadorC7.pop()
		for x in range(len(listaValidadorC8)):
			for y in range(x+1, (len(listaValidadorC8))):
				if listaValidadorC8[x] == listaValidadorC8[y]:
					booole = True
					listaValidadorC8.pop()

		matriz[q][o]= int(g[2]) #Substitui o valor que foi selecionado na posicao indicada acima
		
		print(l3)
		for i in range(9):
			if i == 3 or i == 6:
				print('',l2)
			else:
				print('',l1)
			for j in range(9):
				if j == 0:
					print('{}|| {} |'.format(i+1,matriz[i][j]),end ='')
				elif j > 0 and j<8:
					if j == 2 or j == 5:
						print(' {} ||'.format(matriz[i][j]), end ='')
					elif j == 7:
						print(' {} |'.format(matriz[i][j]), end ='')
					else:
						print(' {} |'.format(matriz[i][j]), end ='')
				else:
					print(' {} ||{}'.format(matriz[i][j], i+1))
			if i == 8:
				print('',l1)
		print(l3)
		
	
	else:
		val = False

	if booole == True:
		print("Jogada nao eh valida, insira outro valor")
