import os

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

print(l3)
for i in range(9):
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