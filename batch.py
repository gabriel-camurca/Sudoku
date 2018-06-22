def elementoemlista(l,y):
	cont = 0
	l.append(y)
	if len(l) == 9:
		for z in range(9):
			for w in range(z+1,9):
				if l[z] == l[w]:
					if l[z] != ' ' and cont == 0:
						print("Dicas nao sao validas")
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

def compareLinhas():
	listaL = []
	a = 0
	if a == 0:
		for i in range(9):
			for j in range(9):
				a = elementoemlista(listaL,matriz[i][j])
			listaL = []
		
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


l4 = 'ABCDEFGHI'
with open("pls.txt") as f: #Abre o arquivo e se refere ao mesmo como "f"
	s = f.readlines() #Adiciona a uma lista("s") todas as linhas de texto do documento
	s = [i.replace("\n","") for i in s] #Retira as quebras de linha
	s = [i.replace(" ","") for i in s] #Retira os espaços
	s = [i.replace(",","") for i in s] #Retira as vírgulas
	s = [i.replace(":","") for i in s] #Retira os dois pontos


f.close #Fecha o arquivo
matriz = [[' ' for i in range(9)] for j in range(9)] #Cria uma matriz 9x9 de "''s"
x = len(s) #Lê a quantidade de elementos da lista contendo todo o texto do arquivo
for i in range(x):
	a = s[i] #Armazena o valor o "i-ésimo" elemento da lista
	a = str(a).upper()
	k = l4.find(a[0]) #Procura nas possibilidades de letras(coordenada das colunas) a que foi digitada
	j = int(a[1])-1 #Lê a coordenada das linhas que foi inserida e diminui 1, pois o sudoku vai de 1 até 9 mas a posição é de 0 até 8, com 0 sendo o primeiro elemento e 8 o último
	matriz[j][k] = int(a[2]) #Adiciona na posição das cooordenadas k(coluna),j(linhas) o valor

compareLinhas()
compareColunas()
matrizquadrantes()


