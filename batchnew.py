import os

def elementoemlista(l,y):
	l.append(y)
	if len(l) == 9:
		for z in range(9):
			for w in range(z+1,9):
				if l[z] == l[w]:
					if l[z] != ' ':
						return False
	return True

def distancialinha(a,b,l):
	l = []
	for i in range(a,b):
	    for j in range(3):
	    	if elementoemlista(l,matriz[i][j]) == False :
	    		return False
	l = []
	for i in range(a,b):
	    for j in range(3,6):
	    	if elementoemlista(l,matriz[i][j]) == False :
	    		return False
	l = []       
	for i in range(a,b):
	    for j in range(6,9):
	    	if elementoemlista(l,matriz[i][j]) == False :
	    		return False
	return True

def matrizquadrantes():
	lista1 = []
	if distancialinha(0,3,lista1) == False:
            return False
	elif distancialinha(3,6,lista1) == False:
            return False
	elif distancialinha(6,9,lista1) == False:
            return False
        
	return True



def comparelinhas():
	listaL = []
	a = 0
	if a == 0:
		for i in range(9):
			for j in range(9):
				if elementoemlista(listaL,matriz[i][j]) == False :
					return False
			listaL = []
		return True
		

def comparecolunas():
	listaC = []
	a = 0
	if a == 0:
		for j in range(9):
			for i in range(9):
				if elementoemlista(listaC,matriz[i][j]) == False :
					return False
			listaC = []
		return True
	

def jogadainvalida():
    if matrizquadrantes() == False or comparelinhas() == False or comparecolunas() == False:
        return False
    return True

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
    with open("entradas.txt") as file:
        lfile = file.readlines()
        lfile = [i.replace("\n","") for i in lfile] #Retira as quebras de linha
        lfile = [i.replace(" ","") for i in lfile] #Retira os espaços
        lfile = [i.replace(",","") for i in lfile] #Retira as vírgulas
        lfile = [i.replace(":","") for i in lfile] #Retira os dois pontos
    file.close
    melnachupeta = len(lfile)
    for i in range(melnachupeta):
        qw = lfile[i]
        qw = str(qw)
        hj = l4.find(qw[0])
        jh = int(qw[1])-1
        matriz[jh][hj] = int(qw[2])    
        os.system("cls")
        print_da_matriz(l3,l2,l1)
        lista_de_jogadas_invalidas = []
        
        if jogadainvalida() == False:
            print("Jogada inválida")
            print(melnachupeta)
            for l in range(melnachupeta):
                lista_de_jogadas_invalidas.append(lfile[l])
                if l+1 == melnachupeta:
                    print(lista_de_jogadas_invalidas)

    else:
        val = False