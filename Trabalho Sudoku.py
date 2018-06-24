import os

#Checa se há elementos repetidos em uma lista com 9 elementos
def ErrorCheck(l,y):
	l.append(y)
	if len(l) == 9:
		for z in range(9):
			for w in range(z+1,9):
				if l[z] == l[w]:
					if l[z] != ' ':
						return False
	return True
#Define o quadrante a ser checado por erros
def QdrAux(a,b,l):
	l = []
	for i in range(a,b):
		for j in range(3):
			if ErrorCheck(l,matriz[i][j]) == False :
				return False
	l = []
	for i in range(a,b):
		for j in range(3,6):
			if ErrorCheck(l,matriz[i][j]) == False :
				return False
	l = []       
	for i in range(a,b):
		for j in range(6,9):
			if ErrorCheck(l,matriz[i][j]) == False :
				return False
	return True
#Define a seção de possíveis quadrantes a serem checados
def QuadrantCheck(qdr):
	lista1 = []
	if qdr == 1 or qdr == 4 or qdr == 7:
		if QdrAux(0,3,lista1) == False:
				return False
		return True
	if qdr == 2 or qdr == 5 or qdr == 8:
		if QdrAux(3,6,lista1) == False:
				return False
		return True
	if qdr == 3 or qdr == 6 or qdr == 9:
		if QdrAux(6,9,lista1) == False:
				return False
		return True
	return True


#Define a linha a ser checada por erros
def LineCheck(lin):
	listaL = []
	for j in range(9):
		if ErrorCheck(listaL,matriz[lin][j]) == False:
			return False
	listaL = []
	return True
#Define a coluna a ser checada por erros
def ColumnCheck(col):
	listaC = []
	for i in range(9):
		if ErrorCheck(listaC,matriz[i][col]) == False:
			return False
	listaC = []
	return True
#Retorna 'False' caso exista algum erro na matriz
def jogada_invalida(qdr,lin,col):
	if QuadrantCheck(qdr) == False or LineCheck(lin) == False or ColumnCheck(col) == False:
		return False
	return True

#Desenha a matriz
def print_matriz(x,y,z):                                                           
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

#Lê os arquivos .txt
def Archive(g):
	with open(g) as f: #Abre o arquivo e se refere ao mesmo como "f"
		s = f.readlines() #Adiciona a uma lista("s") todas as linhas de texto do documento
		s = [i.replace("\n","") for i in s] #Retira as quebras de linha
		s = [i.replace(" ","") for i in s] #Retira os espaços
		s = [i.replace(",","") for i in s] #Retira as vírgulas
		s = [i.replace(":","") for i in s] #Retira os dois pontos
		f.close
		return s

#'Assets' da Interface
l1 = "++---+---+---++---+---+---++---+---+---++"
l2 = "++===+===+===++===+===+===++===+===+===++"
l3 = '    A   B   C    D   E   F    G   H   I  '
l4 = 'ABCDEFGHI'

#Menu
print("")
print("Digite 1 para escolher o modo interativo do sudoku.")
print("Digite 2 para escolher o modo batch do sudoku.")
print("")
choice = int(input("Insira um valor: "))

#Código do modo interativo
if choice == 1:
	arq = Archive("dicas.txt")
	matriz = [[' ' for i in range(9)] for j in range(9)] #Cria uma matriz 9x9 de com espaços vazios
	x = len(arq) #Variável auxiliar que define o loop de acordo com o tamanho do arquivo de dicas
	for i in range(x):
		a = arq[i] #Armazena o valor do "i-ésimo" elemento da lista
		a = str(a) #Transforma o valor em cadeia para uso futuro
		#Seta os elementos nas posiçoes corretas da matriz
		k = l4.find(a[0]) 
		j = int(a[1])-1 
		matriz[j][k] = int(a[2]) 
	print_matriz(l3,l2,l1)
	lista_de_entradas = [] #Recebe as entradas
	val = True #Mantém o loop de entradas
	while val == True: #Loop de entrada das jogadas
		erro = False #Controla as mensagens de erro
		entrada = input('Entre sua jogada: ') #Recebe a jogada que vai ser colocada na matriz
		entrada_formatada = entrada.upper() #Formata a entrada para poder receber letras minúsculas e maiúsculas
		if len(entrada) < 10**100000: 
			lista_de_entradas.append(entrada_formatada) #Adiciona todas as jogadas na lista
			val = True
			lista_de_entradas = [i.replace(",","") for i in lista_de_entradas] #Retira as virgulas
			lista_de_entradas = [i.replace(":","") for i in lista_de_entradas] #Retira os dois pontos
			lista_de_entradas = [i.replace(" ","") for i in lista_de_entradas] #Retira os espaços 
			p = len(lista_de_entradas) 
			for z in range(p): #Checagem para designar o local da entrada
				g = lista_de_entradas[z] 
				o = l4.find(g[0]) 
				q = int(g[1]) - 1 
				matriz[q][o]= int(g[2]) 
			if matriz[q][o] != 0:
				os.system("cls") #Limpa a tela das interaçoes anteriores
				#Checa o quadrante no qual a entrada está designada
				if o >= 0 and o < 3:
					if q == 0 or q == 1 or q == 2:                 
						qdr = 1                                     
					if q == 3 or q == 4 or q == 5:                     
						qdr = 2                                     
					if q == 6 or q == 7 or q == 8:                 
						qdr = 3                                    
				if o >= 3 and o < 6:                               
					if q == 0 or q == 1 or q == 2:                 
						qdr = 4                                     
					if q == 3 or q == 4 or q == 5:                   
						qdr = 5                                     
					if q == 6 or q == 7 or q == 8:                 
						qdr = 6                                    
				if o >= 6 and o < 9:                               
					if q == 0 or q == 1 or q == 2:                 
						qdr = 7                                     
					if q == 3 or q == 4 or q == 5:                   
						qdr = 8                                     
					if q == 6 or q == 7 or q == 8:                 
						qdr = 9
				if jogada_invalida(qdr,q,o) == False: #Caso positivo, aciona a variável de erro
					matriz[q][o] = ' '
					erro = True
				print_matriz(l3,l2,l1) #Printa a matriz novamente para continuar o jogo
				if erro == True:
					print("Jogada invalida! ")
				for i in range(9):
					if (' ') not in matriz[i] and jogada_invalida(qdr,q,o) == True: #Verifica se a matriz está toda preenchida
						val = False
			else:
				print("Jogada invalida! ")
		else:
			val = False #Encerra o jogo
	print('A grade foi preenchida com sucesso!')

#Codigo do modo Batch
if choice == 2:
	s = Archive("dicas.txt")
	matriz = [[' ' for i in range(9)] for j in range(9)] #Cria uma matriz 9x9 com espaços vazios
	x = len(s) #Variável auxiliar que define o loop de acordo com o tamanho do arquivo de dicas
	cont = 0
	while cont < x:
		a = s[cont] #Armazena o valor do "i-ésimo" elemento da lista
		a = str(a) #Transforma o valor em cadeia para uso futuro
		#Seta os elementos nas posiçoes corretas da matriz
		o = l4.find(a[0]) 
		q = int(a[1])-1 
		matriz[q][o] = int(a[2])
		if o>=0 and o<3:
			if q == 0 or q == 1 or q == 2:
				qdr = 1
			elif q == 3 or q == 4 or q == 5:
				qdr = 2
			elif q == 6 or q == 7 or q == 8:
				qdr = 3
		elif o>=3 and o<6:
			if q == 0 or q == 1 or q == 2:
				qdr = 4
			elif q == 3 or q == 4 or q == 5:
				qdr = 5
			elif q == 6 or q == 7 or q == 8:
				qdr = 6
		elif o>=6 and o<9:
			if q == 0 or q == 1 or q == 2:
				qdr = 7
			elif q == 3 or q == 4 or q == 5:
				qdr = 8
			elif q == 6 or q == 7 or q == 8:
				qdr = 9
		if jogada_invalida(qdr,q,o) == False:
			print("Arquivo invalido")
			cont = x
		cont += 1

	#Codigo referente a leitura e aplicaçao das entradas BATCH
	arq = Archive("entradas_PLS.txt")
	y = len(arq)
	conta = 0
	jogadas_invalidas = []
	while conta < y:
		a = arq[conta] #Armazena o valor o "i-ésimo" elemento da lista
		a = str(a)
		o = l4.find(a[0]) 
		q = int(a[1])-1 
		matriz[q][o] = int(a[2])
		if o>=0 and o<3:
			if q == 0 or q == 1 or q == 2:
				qdr = 1
			elif q == 3 or q == 4 or q == 5:
				qdr = 2
			elif q == 6 or q == 7 or q == 8:
				qdr = 3
		elif o>=3 and o<6:
			if q == 0 or q == 1 or q == 2:
				qdr = 4
			elif q == 3 or q == 4 or q == 5:
				qdr = 5
			elif q == 6 or q == 7 or q == 8:
				qdr = 6
		elif o>=6 and o<9:
			if q == 0 or q == 1 or q == 2:
				qdr = 7
			elif q == 3 or q == 4 or q == 5:
				qdr = 8
			elif q == 6 or q == 7 or q == 8:
				qdr = 9
		if jogada_invalida(qdr,q,o) == False:
			matriz[q][o] = ' '
			jogadas_invalidas.append(a)
		conta += 1
	#Checa se existem jogadas invalidas, e caso positvo, printa
	for i in range (len(jogadas_invalidas)):
		jogada = str(jogadas_invalidas[i])
		print('A jogada ({},{}) = {} eh invalida!'.format(jogada[0],jogada[1],jogada[2]))
	#Checa se o jogo foi concluido
	if jogadas_invalidas == []:
		print('A grade foi preenchida com sucesso!')
	else:
		print('A grade nao foi preenchida!')
	input()