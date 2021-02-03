# -*- coding: utf-8 -*-
import numpy as np
from numpy import matmul, transpose
import matplotlib.pyplot as plt
import pylab as p
import serial


    
#####MACIERZE OBROTU#############

M0 = [[1, 0], [0, 1]]
MNZ90 = [[0, -1], [1, 0]]
MNZ180 = [[-1, 0], [0, -1]]
MNZ270 = [[0, 1], [-1, 0]]

MNZ360 = M0

MZ90 = [[0, 1], [-1, 0]]
MZ180 = [[-1, 0], [0, -1]]
MZ270 = [[0, -1], [1, 0]]
MZ360 = M0

########### Zmienne ##############
Poczatek = [0.5, 2.5]
trasa_orientacja = []
orientacja = 0
V = [0, 1]
wspolrzedne_trasy = []
pozycja = [0,0]
wspolrzedne_trasy_y = []
wspolrzedne_trasy_x = []   
index_rep = [] 
nowax= []
noway = []  
tabela_ruchow = []
Trasa = []
marker_list = []
Ostateczne_nowa = []
Ostateczne_nowa_y = []
Ostateczne_nowa_x = []

########### OTRZYMANA TRASA ################
##probne trasy do wygenerowania
#Trasa= ['F', 'F', 'L', 'F', 'R','R', 'F', 'L', 'F', 'F','K']#if R== MNZ90 or R==MZ270:
#Trasa=['F', 'F', 'L', 'L',  'F', 'F', 'R', 'R', 'F', 'F', 'F', 'L', 'F', 'F','R', 'F',  'L', 'F','F', 'R', 'R', 'F', 'F', 'F', 'L', 'R', 'F', 'F', 'F','K']
#Trasa = ['F', 'L', 'L', 'R', 'R', 'F', 'F', 'R','F', 'F', 'R','F', 'L', 'L', 'F', 'F', 'F', 'F', 'L', 'F', 'F','R', 'R', 'F', 'F', 'F', 'R', 'F', 'F' , 'F', 'L', 'F', 'F', 'R', 'F', 'F', 'K' ]
#Trasa = ['R', 'F', 'F', 'F', 'L', 'L', 'F', 'F', 'R', 'F', 'F', 'R', 'F', 'F', 'F', 'R', 'R', 'F', 'F','F', 'L', 'F','L', 'L', 'R', 'R', 'F', 'L', 'L', 'R', 'F','K']

#praca 
#Trasa= ['F', 'R', 'F', 'R', 'F', 'L', 'L', 'R', 'R', 'F', 'L', 'L', 'R', 'R', 'F', 'R', 'F', 'L', 'R', 'R', 'F', 'L', 'L', 'F', 'L', 'F', 'L', 'R', 'R', 'F', 'R', 'F', 'F', 'F', 'R', 'F', 'K']
#Trasa= ['F', 'R', 'F', 'R', 'F', 'L', 'F', 'L', 'L', 'R', 'R', 'F', 'R', 'F', 'F', 'R', 'R', 'F', 'L', 'L', 'R', 'R', 'F', 'L', 'L', 'R', 'F', 'L', 'L', 'F', 'F', 'K'] 

#Trasa= ['F', 'L', 'L', 'R', 'F', 'F', 'R', 'F', 'F', 'F', 'R', 'F', 'R', 'R', 'F', 'L', 'F', 'F', 'L', 'F', 'L', 'L', 'R', 'R', 'F', 'F', 'L', 'L', 'F', 'R', 'R', 'F', 'F', 'L', 'L', 'K'] 

##########BLUETOOTH##########

ser = serial.Serial(
  port='COM5',
  baudrate = 9600,
 timeout=20
)
print ("Serial is open: " + str(ser.isOpen()))
a =ser.write('1')
ser.flushInput()
ser.flushOutput()
b = ser.read(40)


print b, len(b)
for i in range(len(b)):
        Trasa.append(str(b[i]))


                        
print 'Trasa', Trasa, 'len', len(Trasa)
##################### Tworzenie tablicy orientacji #######################
for i in range(len(Trasa)):
        if Trasa[i] == 'S':
            orientacja = orientacja
            trasa_orientacja.append(orientacja)
            marker_list.append('x')
        if Trasa[i] == 'F':
            orientacja = orientacja
            trasa_orientacja.append(orientacja)
            marker_list.append('^')
        if Trasa[i] == 'L':
            orientacja = orientacja -90
            trasa_orientacja.append(orientacja)
            marker_list.append('^')
        if Trasa[i] == 'R':
            orientacja = orientacja +90
            trasa_orientacja.append(orientacja)
            marker_list.append('^')
        if Trasa[i] == 'K': 
            orientacja = orientacja
            trasa_orientacja.append(orientacja)
            marker_list.append('x')
            
        if orientacja == 360 or orientacja == -360:
            orientacja =0
        

############### Definicje funkji ########################33
def Dodaj_pol(x, y):
    for i in range(len(x)):
        x[i] = x[i] + 0.5
    for i in range(len(y)):
        y[i] = y[i] + 0.5
    return x, y

def Add(wektor1, wektor2):
    nowy_wektor0 = wektor1[0] + wektor2[0]
    nowy_wektor1 = wektor1[1] + wektor2[1]
    suma = [nowy_wektor0, nowy_wektor1]
    return suma 
    
def Odejmij(wektor1, wektor2):
    nowy_wektor0 = wektor1[0] - wektor2[0]
    nowy_wektor1 = wektor1[1] - wektor2[1]
    roznica = [nowy_wektor0, nowy_wektor1]
    return roznica
    
def Multiplication(wektor1, wektor2):
    for i in range(1):
        for j in range(1):
            N11 = wektor1[0]* wektor2[0] 
            N12 = wektor1[1]* wektor2[0]
            N21 = wektor1[0]* wektor2[1]
            N22 = wektor1[1]* wektor2[1]
            Rodw = [[N11, N12], [N21, N22]]
            return Rodw
###################### Tworzenie wspolrzednych trasy ######################
wspolrzedne_trasy.append(pozycja)
print trasa_orientacja
for i in range(len(Trasa)):
    if Trasa[i] == 'F':
        if trasa_orientacja[i] == 0:
            pozycja = Add(pozycja, V)           
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -90:
            przesuniecie = np.matmul(MNZ90, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 90:
            przesuniecie = np.matmul(MZ90, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
            
        if trasa_orientacja[i] == 180:
            przesuniecie = np.matmul(MZ180, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -180:
            przesuniecie = np.matmul(MNZ180, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 270:
            przesuniecie = np.matmul(MZ270, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -270:
            przesuniecie = np.matmul(MNZ270, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)

    if Trasa[i] == 'L':
        if trasa_orientacja[i] == 0:
            przesuniecie = (0, 1)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -90:
             
            przesuniecie = np.matmul(MNZ90, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 90:
             
            przesuniecie = np.matmul(MZ90, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -180:
             
            przesuniecie = np.matmul(MNZ180, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 180:
             
            przesuniecie = np.matmul(MZ180, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -270:
             
            przesuniecie = np.matmul(MNZ270, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 270:
             
            przesuniecie = np.matmul(MZ270, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -360:
             
            przesuniecie = np.matmul(MNZ360, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 360:
             
            przesuniecie = np.matmul(MZ360, V)
            pozycja = Add(pozycja, przesuniecie)
            wspolrzedne_trasy.append(pozycja)
    
    
      
    if Trasa[i] == 'R':
        if trasa_orientacja[i] == -90:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 90:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 0:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 180:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -180:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 270:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -270:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == 360:
            wspolrzedne_trasy.append(pozycja)
        if trasa_orientacja[i] == -360:
            wspolrzedne_trasy.append(pozycja)  
            
   
    
        
    
     

########Tworzenie tabeli wszystkich ruchow [wspolrzedne, index, ruch] ###############
for i in range(len(wspolrzedne_trasy)):
    
    bufor=[]  
    bufor.append(wspolrzedne_trasy[i])
    bufor.append(0)
    bufor.append(Trasa[i])
    tabela_ruchow.append(bufor)
    print 'bufor',bufor 
    
######### Podzial na wspolrzednych trasy na x i y (potrzebne do plot) #################
for i in range(len(wspolrzedne_trasy)):
    wspolrzedne_trasy_x.append(wspolrzedne_trasy[i][0])
    wspolrzedne_trasy_y.append(wspolrzedne_trasy[i][1])
print 'lukaj tu', tabela_ruchow
######### Funkcja znajdująca indeksy powtarzających się pól #########################3
stop = False
for i in range(len(tabela_ruchow)):
    for j in range(len(tabela_ruchow)):
            if j <i:
                    tabela_ruchow[i][1] = i
                    if tabela_ruchow[i][0] == tabela_ruchow[j][0]:
                        if tabela_ruchow[i][0] != tabela_ruchow[i-1][0]:
                            index_rep.append(i)
                            print 'index', index_rep, 'i', i
                            
                        elif tabela_ruchow[i][0] == tabela_ruchow[i-2][0]:
                            index_rep.append(i)
                            print 'i', i
                            
                        elif tabela_ruchow[i][2] != tabela_ruchow[i-1][2]:
                            index_rep.append(i)
                            print 'index', index_rep, 'i', i
                        
print 'index_rep', index_rep
################## Usuwanie powtorek w indexach ######
unique=[]
for ele in index_rep:
    if ele not in unique:
        unique.append(ele)
############# Tworzenie uproszczenia- iusuwa ostani index po ciagu indexow inkrementowanych o 1 ##########
uproszczenie = []
for i in range(len(unique)):
    zmienna= unique[i-1] - unique[i]
    if zmienna == -1:
        uproszczenie.append(unique[i-1])

################ Tworzenie nowej tablicy z indeksami uzyskanymi powyżej ############
nowax = []
noway = []
for i in uproszczenie:
    nowax.append(wspolrzedne_trasy_x[i])
    noway.append(wspolrzedne_trasy_y[i])

###############  Ostateczne indeksy to indeksy ktore odpowiadaja slepej uliczce   
ostateczne_indeksy = []
for i in uproszczenie:
    for j in range(len(wspolrzedne_trasy)):
        if wspolrzedne_trasy[i] == wspolrzedne_trasy[j]:
            ostateczne_indeksy.append(j)

print "uproszczenie", uproszczenie
print 'ostatecznie_indeksy', ostateczne_indeksy


########### Usuwanie powtorek z ostatecznych indeksow ################
ost_indeksy = []
for ele in ostateczne_indeksy:
    if ele not in ost_indeksy:
        ost_indeksy.append(ele)
print 'ost_indeksy', ost_indeksy

############# Tworzenie tablic ze wspolrzednymi wyznaczonej nowej trasy ###########
Ostateczne_x = []
Ostateczne_y = []

Ostateczne_x = np.delete(wspolrzedne_trasy_x, ost_indeksy)
Ostateczne_y = np.delete(wspolrzedne_trasy_y, ost_indeksy)

Odwrocona_x = []
Odwrocona_y = []

for i in ost_indeksy:
    for j in range(len(wspolrzedne_trasy_x)):
        if wspolrzedne_trasy_x[i] == wspolrzedne_trasy_x[j]:
            Odwrocona_x.append(wspolrzedne_trasy_x[i])

                   
            
            
print 'ciota', (Ostateczne_y)
print 'ciota',(Odwrocona_y)

Ostateczne = []
for i in range(len(Ostateczne_x)):
    bufor=[]
    bufor.append(Ostateczne_x[i])
    bufor.append(Ostateczne_y[i])
    Ostateczne.append(bufor)


############ Ostatnie i pierwsze pole ############
startstop_x = []
startstop_y = []
startstop_x.append(wspolrzedne_trasy_x[0])
startstop_x.append(wspolrzedne_trasy_x[-1])

startstop_y.append(wspolrzedne_trasy_y[0])
startstop_y.append(wspolrzedne_trasy_y[-1])


############ przesuwam wszystko o [0.5, 0.5] ##############
################### PLOTY ###################3


fig, (ax1)= plt.subplots()
#fig, (ax2)= plt.subplots()
#fig, (ax3)= plt.subplots()
print Ostateczne_x

for i in range(len(Ostateczne)):
    bufor = []
    bufor.append(Ostateczne[i][0] + 0.5)
    bufor.append(Ostateczne[i][1] + 0.5)
    Ostateczne_nowa.append(bufor)
for i in range(len(Ostateczne_nowa)):
    Ostateczne_nowa_x.append(Ostateczne_nowa[i][0])
    Ostateczne_nowa_y.append(Ostateczne_nowa[i][1])
       
print Ostateczne_nowa_x
print 'yolyolyoy', type(Ostateczne_nowa_y)

startstop_x, startstop_y = Dodaj_pol(startstop_x, startstop_y)
nowax, noway = Dodaj_pol(nowax, noway)
wspolrzedne_trasy_x, wspolrzedne_trasy_y = Dodaj_pol(wspolrzedne_trasy_x, wspolrzedne_trasy_y)

#ax1.plot(Ostateczne_nowa_x, Ostateczne_nowa_y, color = 'c')
uni2 = []
for i in range(1,len(wspolrzedne_trasy),1):
    wektor_orientacji = Odejmij(wspolrzedne_trasy[i], wspolrzedne_trasy[i-1])
    uni2.append(wektor_orientacji)
'''
for i in range(len(uni2)):
    if uni2[i] == [0, 0]:
        pass
    if uni2[i] == [0, 1]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.6, wspolrzedne_trasy[i][1]+0.5, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    if uni2[i] == [-1, 0]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.5, wspolrzedne_trasy[i][1]+0.6, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    if uni2[i] == [0, -1]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.4, wspolrzedne_trasy[i][1]+0.5, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    
    if uni2[i] == [1, 0]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.5, wspolrzedne_trasy[i][1]+0.4, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    
'''

################## 1. plot

for i in range(len(uni2)):
    if uni2[i] == [0, 0]:
        pass
    if uni2[i] == [0, 1]:
        ax1.arrow(wspolrzedne_trasy[i][0]+0.6, wspolrzedne_trasy[i][1]+0.5, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    if uni2[i] == [-1, 0]:
        ax1.arrow(wspolrzedne_trasy[i][0]+0.5, wspolrzedne_trasy[i][1]+0.6, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    if uni2[i] == [0, -1]:
        ax1.arrow(wspolrzedne_trasy[i][0]+0.4, wspolrzedne_trasy[i][1]+0.5, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    
    if uni2[i] == [1, 0]:
        ax1.arrow(wspolrzedne_trasy[i][0]+0.5, wspolrzedne_trasy[i][1]+0.4, uni2[i][0]*0.4, uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )

ax1.scatter(wspolrzedne_trasy_x, wspolrzedne_trasy_y, marker='s', s =500, color= 'black', label = 'przejechana trasa')
   
ax1.scatter(startstop_x[0], startstop_y[0], s=500, marker='s', c = 'green', label = 'Poczatek')
ax1.scatter(startstop_x[1], startstop_y[1], s=500, marker='s', c = 'red', label = 'Koniec')
ax1.scatter(nowax, noway, s= 500, marker='x', c = 'white', label = 'slepa uliczka')
##############2. plot
#########funkcja rysująca strzalki w orientac
'''
for i in range(len(uni2)):
    if uni2[i] == [0, 0]:
        pass
    if uni2[i] == [0, 1]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.6, wspolrzedne_trasy[i][1]+0.5, uni2[i][0]*0.4,
        uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    if uni2[i] == [-1, 0]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.5, wspolrzedne_trasy[i][1]+0.6, uni2[i][0]*0.4,
        uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    if uni2[i] == [0, -1]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.4, wspolrzedne_trasy[i][1]+0.5, uni2[i][0]*0.4,
        uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    
    if uni2[i] == [1, 0]:
        ax2.arrow(wspolrzedne_trasy[i][0]+0.5, wspolrzedne_trasy[i][1]+0.4, uni2[i][0]*0.4,
        uni2[i][1]*0.4, color = 'c',head_width=0.2, head_length=0.3 )
    
ax2.scatter(startstop_x[0], startstop_y[0], s=500, marker='s', c = 'green', label = 'Poczatek')
ax2.scatter(startstop_x[1], startstop_y[1], s=500, marker='s', c = 'red', label = 'Koniec')
ax2.scatter(wspolrzedne_trasy_x, wspolrzedne_trasy_y, marker='s', s =500, color= 'black', label = 'przejechana trasa')
#ax2.scatter(nowax, noway, s= 500, marker='x', c = 'white', label = 'slepa uliczka')
'''

############ 3. plot na dola programu




#ax[0].scatter(wspolrzedne_trasy_x, wspolrzedne_trasy_y, marker='s', s =500, color= 'black')
#ax1.scatter(wspolrzedne_trasy_x, wspolrzedne_trasy_y, marker='s', s =500, color= 'black', label = 'przejechana trasa')
#ax[1].scatter(wspolrzedne_trasy_x, wspolrzedne_trasy_y, marker='s', s =500, color= 'black')
#ax[0].legend()


#ax[0].scatter(startstop_x[0], startstop_y[0], s=500, marker='s', c = 'green')
#ax[0].scatter(startstop_x[1], startstop_y[1], s=500, marker='s', c = 'red')
#ax1.scatter(startstop_x[0], startstop_y[0], s=500, marker='s', c = 'green', label = 'Poczatek')
#ax1.scatter(startstop_x[1], startstop_y[1], s=500, marker='s', c = 'red', label = 'Koniec')
#ax[1].scatter(startstop_x[0], startstop_y[0], s=500, marker='s', c = 'green')
#ax[1].scatter(startstop_x[1], startstop_y[1], s=500, marker='s', c = 'red')

#ax1.scatter(nowax, noway, s= 500, marker='x', c = 'white', label = 'slepa uliczka')
#ax[1].scatter(nowax, noway, s= 500, marker='x', c = 'white')




#ax[0].grid()
#ax[1].grid()


################ Tworzenie tablicy z wektorami przesuniecia  ####################
lista_wektorow = [[0, 0]]
print "ost          ", Ostateczne
Ostateczne =  Ostateczne[::-1]
print "ost odwrocone", Ostateczne




for i in range(len(Ostateczne)-2):
    if Ostateczne[i] == Ostateczne[i+1]:
        print 'ciota'    
        if Ostateczne[i+1] == Ostateczne[i+2]:
            Ostateczne.pop(i+2)

uni=[]
for ele in Ostateczne:
    if ele not in uni:
        uni.append(ele)
        
#lista_wektorow.append([0, 0])
print uni
for i in range(1,len(uni),1):
    wektor_orientacji = Odejmij(uni[i], uni[i-1])
    lista_wektorow.append(wektor_orientacji)
    
    
print "ost   po upgarde", uni
print 'lista wektorow', lista_wektorow                      
'''
########## Przetwarza tablice z wektorami przesuniec na tablice rozumiana przez mikroprocesor ##############
do_wyslania_od_poczatku = []
for i in range(len(lista_wektorow)-1):
    if lista_wektorow[i] == [0,1]:
        if lista_wektorow[i+1] == lista_wektorow[i]:
            do_wyslania_od_poczatku.append('F')
  #          marker_list.append('^')
        if lista_wektorow[i+1] == [-1,0]:
            do_wyslania_od_poczatku.append('L')
 #           marker_list.append('<')
        if lista_wektorow[i+1] == [0,0]:
            do_wyslania_od_poczatku.append('R')
  #          marker_list.append('>')
    if lista_wektorow[i] == [-1,0]:
        if lista_wektorow[i+1] == lista_wektorow[i]:
            do_wyslania_od_poczatku.append('F')
        if lista_wektorow[i+1] == [0, -1]:
            do_wyslania_od_poczatku.append('L')
        if lista_wektorow[i+1] == [0, 0]:
            if lista_wektorow[i+2] == lista_wektorow[i]:
                pass
            else:    
                do_wyslania_od_poczatku.append('R')
    if lista_wektorow[i] == [1, 0]:
        if lista_wektorow[i+1] == lista_wektorow[i]:
            do_wyslania_od_poczatku.append('F')
        if lista_wektorow[i+1] == [0, 1]:
            do_wyslania_od_poczatku.append('L')
        if lista_wektorow[i+1] == [0, 0]:
            do_wyslania_od_poczatku.append('R')           
    if lista_wektorow[i] == [0, -1]:
        if lista_wektorow[i+1] == lista_wektorow[i]:
            do_wyslania_od_poczatku.append('F')
        if lista_wektorow[i+1] == [1, 0]:
            do_wyslania_od_poczatku.append('L')
        if lista_wektorow[i+1] == [0, 0]:
            print 'ciota1'
            do_wyslania_od_poczatku.append('R')
    if lista_wektorow[i] == [0, 0]:
        if lista_wektorow[i+1] == [0, 1]:
            do_wyslania_od_poczatku.append('F')
        if lista_wektorow[i+1] == [0, -1]:
            do_wyslania_od_poczatku.append('F')
        if lista_wektorow[i+1] == [1, 0]:
            do_wyslania_od_poczatku.append('F')    
        if lista_wektorow[i+1] == [-1, 0]:
            do_wyslania_od_poczatku.append('F')    
            
print 'do_wyslania_od_poczatku', do_wyslania_od_poczatku
'''

do_wyslania_od_konca = []
for i in range(len(lista_wektorow)-1):
    print lista_wektorow[i]
    if lista_wektorow[i] == [0, 0]:
        if lista_wektorow[i+1] == [0, 1]:
            do_wyslania_od_konca.append('F')
        if lista_wektorow[i+1] == [0, -1]:
            do_wyslania_od_konca.append('F')
        if lista_wektorow[i+1] == [1, 0]:
            do_wyslania_od_konca.append('F')    
        if lista_wektorow[i+1] == [-1, 0]:
            do_wyslania_od_konca.append('F')   
    if lista_wektorow[i] == [0, -1]:
        if lista_wektorow[i+1] == [1, 0]:
            do_wyslania_od_konca.append('L')
        if lista_wektorow[i+1] == [-1, 0]:
            do_wyslania_od_konca.append('R')
        if lista_wektorow[i+1] == [0, -1]:
            do_wyslania_od_konca.append('F')
    if lista_wektorow[i] == [1, 0]:
        if lista_wektorow[i+1] == [0, -1]:
            do_wyslania_od_konca.append('R')
        if lista_wektorow[i+1] == [0, 1]:
            do_wyslania_od_konca.append('L')
        if lista_wektorow[i+1] == [1, 0]:
            do_wyslania_od_konca.append('F')

    if lista_wektorow[i] == [-1, 0]:
        if lista_wektorow[i+1] == [0, 0]:
            pass
        if lista_wektorow[i+1] == [0, 1]:
            do_wyslania_od_konca.append('R')
        if lista_wektorow[i+1] == [-1, 0]:
            do_wyslania_od_konca.append('F')
        if lista_wektorow[i+1] == [0, -1]:
            do_wyslania_od_konca.append('L')
    if lista_wektorow[i] == [0, 1]:
        if lista_wektorow[i+1] == [0, 0]:
            pass
        if lista_wektorow[i+1] == [1, 0]:
            do_wyslania_od_konca.append('R')
        if lista_wektorow[i+1] == [-1, 0]:
            do_wyslania_od_konca.append('L')
        if lista_wektorow[i+1] == [0, 1]:
            do_wyslania_od_konca.append('F')
###########BLUETOOTH 2

print ("Serial is open: " + str(ser.isOpen()))
print 'do_wyslania_od_konca', do_wyslania_od_konca
############ W kazde wolne pole dodaje koniec

nowa_tablica = do_wyslania_od_konca
for i in range(40- len(do_wyslania_od_konca)):
    nowa_tablica.append('K')
raw_input()
a =ser.write(nowa_tablica)
ser.close()

#print 'do_wyslania_od_poczatku', do_wyslania_od_poczatku
print 'nowa_tablica', nowa_tablica
 ################3. PLOT'
'''
ax2.scatter(startstop_x[0], startstop_y[0], s=500, marker='s', c = 'green', label = 'Poczatek')
ax2.scatter(startstop_x[1], startstop_y[1], s=500, marker='s', c = 'red', label = 'Koniec')
ax2.scatter(wspolrzedne_trasy_x, wspolrzedne_trasy_y, marker='s', s =500, color= 'black', label = 'przejechana trasa')
ax2.scatter(nowax, noway, s= 500, marker='x', c = 'white', label = 'slepa uliczka')
'''
'''
for i in range(len(uni)-1):
    ax1.arrow(uni[i][0]+0.5, uni[i][1]+0.5, lista_wektorow[i+1][0]*0.3, lista_wektorow[i+1][1]*0.3, color = 'c',head_width=0.3, head_length=0.5 )
'''
chartBox = ax1.get_position()
ax1.set_position([chartBox.x0, chartBox.y0*1.5, chartBox.width, chartBox.height])
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=4)
#ax1.grid()
plt.xticks([], [])
plt.yticks([], [])
p.axis('equal')
print '1'
p.show() 

#p.arrow(uni[0][0]+0.5, uni[0][1]+0.5, lista_wektorow[1][0]*0.01, lista_wektorow[1][1]*0.01, color = 'b',head_width=0.3, head_length=0.5 )

