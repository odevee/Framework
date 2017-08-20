import math
import random
def p_s_geg_a(a,s):
    if(grid[a[1]][a[0]]==2):
        if a==s:
            #print("p von "+ str(s) +" gegeben "+ str(a)+" ist 1")
            return 0.5
        else:
            #print("p von "+ str(s) +" gegeben "+ str(a)+" ist 0")
            return 0.1


    else:
        if a==s:
            #print("p von "+ str(s) +" gegeben "+ str(a)+" ist 1")
            return 1
        else:
            #print("p von "+ str(s) +" gegeben "+ str(a)+" ist 0")
            return 0

        #Kulberg leibner als Extra Funktion
def Kulberg_Leibner(a,s,p_s):
    if p_s==0:
        return 0
    elif(p_s_geg_a(a,s)==0):
        return 0
    else:
        #print (p_s_geg_a(a,s))
        #print (p_s_geg_a(a,s)/p_s)
        ausgabe = p_s_geg_a(a,s)*math.log2(p_s_geg_a(a,s)/p_s)
        return ausgabe

def p_a_nächstes_unnormiert(a, menge_s,p_a, dict_p_s):
    p_strich = 0
    for s in menge_s:
        p_strich = p_strich + Kulberg_Leibner(a,s,dict_p_s[s])
    p_strich = p_a*math.exp(p_strich)
    return p_strich

def p_s(s ,menge_a, dict_p_a):
    ergebnis = 0
    for a in menge_a:
        #print("p von "+ str(a) + "gegeben "+str(s)+" mal p von "+ str(a)+ " ist " + str(p_s_geg_a(a,s)*dict_p_a[a]))
        ergebnis = ergebnis + p_s_geg_a(a,s)*dict_p_a[a]
    #print("p von "+ str(s) +" ist "+ str(ergebnis))
    return ergebnis

def aktualisiere_p_a(menge_a, menge_s, dict_p_a, dict_p_s):
    dict_p_a_neu = {}
    for a in menge_a:
        dict_p_a_neu.update({a:p_a_nächstes_unnormiert(a, menge_s,dict_p_a[a],dict_p_s)})
    normierungsfaktor = 0
    for a in menge_a:
        normierungsfaktor = normierungsfaktor + dict_p_a_neu[a]
    dict_ausgabe = {}
    normierungsfaktor = 1/normierungsfaktor
    for a in menge_a:
        dict_ausgabe.update({a:normierungsfaktor*dict_p_a_neu[a]})
    return dict_ausgabe

def aktualisiere_p_s(menge_a, menge_s, dict_p_a):
    dict_p_s={}
    for s in menge_s:
        dict_p_s.update({s:p_s(s,menge_a, dict_p_a)})
    return dict_p_s

def zufallszahlennormiert_zuordene(menge):
    summebisher = 0
    dict_neu = {}
    for a in menge:
        zahl = random.random()+0.05
        dict_neu.update({a:zahl})
        summebisher = summebisher + zahl
    dict_ausgabe={}
    for a in menge:
        dict_ausgabe.update({a:(dict_neu[a]/summebisher)})
    #print(dict_ausgabe)
    return dict_ausgabe

def empowerment_probab(menge_a, menge_s):
    dict_p_a = zufallszahlennormiert_zuordene(menge_a)
    while 1:
        dict_p_s = aktualisiere_p_s(menge_a, menge_s, dict_p_a)
        dict_p_a_neu = aktualisiere_p_a(menge_a, menge_s, dict_p_a, dict_p_s)
        #print("P von s")
        #print(dict_p_s)
        #print("P von a")
        #print(dict_p_a)
        fehler = 0
        for a in menge_a:
            fehler = fehler + abs(dict_p_a_neu[a] - dict_p_a[a])
        #print(str(fehler) + " ist der Fehler")
        if fehler < 0.01:
            break
        dict_p_a = dict_p_a_neu
    empowerment = 0
    for a in menge_a:       #Doppelsumme
        innere_summe = 0
        for s in menge_s:
            innere_summe = innere_summe + Kulberg_Leibner(a,s,dict_p_s[s])
        empowerment = empowerment+ innere_summe * dict_p_a[a]
    return empowerment

menge_a=['a',1,(0,1)]
menge_s={'a',1,(0,1)}

#empowerment_probab(menge_a, menge_s)
#print(math.log2(len(menge_a)))




def findenachbarn(x,y,grid):
    setOfNeighbours = {(x,y)}
    for xi in (x-1, x, x+1):
        if (grid[y][xi]): #accessible
            setOfNeighbours.add((xi,y))
    for yi in (y-1, y+1):
        if (grid[yi][x]): #accessible
            setOfNeighbours.add((x,yi))
    setOfNeighbours = set(setOfNeighbours)
    return setOfNeighbours

def finde_n_te_nachbarn(x,y,grid,n):
    if(grid[y][x]==0):
        return set([])
    setAnNachbarn = {(x,y)}
    for i in range(n):
        setAnNeuenNachbarn = {(x,y)}
        for elem in setAnNachbarn:
            setAnNeuenNachbarn= setAnNeuenNachbarn | findenachbarn(elem[0], elem[1], grid)
        setAnNachbarn = setAnNachbarn | setAnNeuenNachbarn
    return setAnNachbarn



def wohinlaufen(x,y,grid,denkweite):
    ziel = (x,y)
    bewertungmax = -1
    for i in finde_n_te_nachbarn(x,y,grid, 1):
        nachbarn = finde_n_te_nachbarn(i[0],i[1],grid,denkweite)
        bewertung = empowerment_probab(nachbarn,nachbarn)
        if bewertung > bewertungmax:
            ziel = (i[0], i[1])
            bewertungmax = bewertung
        else:
            if bewertung == bewertungmax:
                if(random.random() < 0.5):
                    ziel = (i[0], i[1])
                pass
    return (ziel,bewertungmax)


#Test
grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0]]
x = 1
y = 1
print(x,y)
for index in range(50):
    tripel = wohinlaufen(x,y,grid,9)
    tupel = tripel[0]
    x = tupel[0]
    y = tupel[1]
    print(tripel)
"""
def findenachbarn(x,y,grid):
    setOfNeighbours = {(x,y)}
    for xi in (x-1, x, x+1):
        if (grid[y][xi]): #accessible
            setOfNeighbours.add((xi,y))
    for yi in (y-1, y+1):
        if (grid[yi][x]): #accessible
            setOfNeighbours.add((x,yi))
    setOfNeighbours = set(setOfNeighbours)
    return setOfNeighbours

def finde_n_te_nachbarn(x,y,grid,n):
    if(grid[y][x]==0):
        return set([])
    setAnNachbarn = {(x,y)}
    for i in range(n):
        setAnNeuenNachbarn = {(x,y)}
        for elem in setAnNachbarn:
            setAnNeuenNachbarn= setAnNeuenNachbarn | findenachbarn(elem[0], elem[1], grid)
        setAnNachbarn = setAnNachbarn | setAnNeuenNachbarn
    return setAnNachbarn

def berechne_empowerment(x,y,grid,thinkwide):
    if(grid[y][x]==0):
        return 0
    return len(finde_n_te_nachbarn(x,y,grid,thinkwide))
    #return math.log2(len(finde_n_te_nachbarn(x,y,grid,thinkwide)))

def wohinlaufen(x,y,grid,thinkwide):
    ziel = (x,y)
    bewertungmax = -1
    for i in finde_n_te_nachbarn(x,y,grid, 1):
        bewertung = berechne_empowerment(i[0],i[1],grid,thinkwide)
        if bewertung > bewertungmax:
            ziel = (i[0], i[1])
            bewertungmax = bewertung
        else:
            if bewertung == bewertungmax:
                if(random.random() < 0.5):
                    ziel = (i[0], i[1])
                pass
    return (ziel,bewertungmax)



#Test

text = ""
for j in range (len(grid)):
    for i in range(len(grid[0])):
        emp = round(empowerment_probab(i, j))
        if emp < 10:
            text = text + "  " + str(emp)
        else:
            text = text + " " + str(emp)
    text = text + "\n"
print(text)

"""
