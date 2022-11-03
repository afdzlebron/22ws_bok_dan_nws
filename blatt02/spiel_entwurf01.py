
def spiel(strategie: int, zufallsgen, verborse = True): 
    pass
    
def main(): 

    Gewonnen = 0
    strategie = int
    # For now just default value
    bereich = 2

    nichterlaubt = set()

    for i in range(0,anzahl-1):
        gewinnTuer = auswahl(nichterlaubt,bereich)
        if verbose == True: 
            print("Gewinntür ausgewählt")
        nichterlaubt.add(gewinnTuer)
        # Spielerin-Tür
        spielerinTuer = auswahl({},bereich)
        if verbose == True: 
            print("Spielerintür ausgewählt")
        nichterlaubt.add(spielerinTuer)
        # geöffnete Tür
        moderatorinTuer = auswahl(nichterlaubt,bereich)
        if verbose == True: 
            print("Moderatorintür ausgewählt")
        nichterlaubt.add(moderatorinTuer)

        if strategie == 1: 
            nichterlaubt.remove(gewinnTuer)
            spielerinTuer = auswahl(nichterlaubt,bereich)
            if verbose == True: 
                print("Spielerin wechselt von Tür")
        else: 
            pass
        
        if spielerinTuer == gewinnTuer: 
            if verbose == True: 
                print("Spielerin hat gewonnen")
            Gewonnen += 1
            return True
        nichterlaubt.clear()
        pass 

if __name__ == "__main__": 
    main()





    _______________________________
#c1
def auswahl(nichterlaubt, bereich):
    x=randrange(bereich)
    for x in range(bereich):
        if x not in nichterlaubt:
            return x
tead=[1, 2, 3]

auswahl(tead, 3)

#c2
#strategie=0:bleibt, strategie=1: wechselt
def spiel(strategie, bereich, verbose=True):
    gewinnTuer=randrange(bereich)
    if verbose: 
            print('Gewinntür ausgewählt: Tür {:0}'.format(gewinnTuer))
    spielerinTuer=randrange(bereich)
    if verbose: 
            print('Spielerintür ausgewählt: Tür {:0}'.format(spielerinTuer))
    list1=[gewinnTuer, spielerinTuer]
    moderatorinTuer=auswahl(list1, bereich)
    if verbose: 
            print('Moderatorintür ausgewählt: Tür {:0}'.format(moderatorinTuer))
    if strategie==0:
        if verbose: 
            print("Spielerin bliebt")
        if spielerinTuer==gewinnTuer:
                return True
        else:
                return False
    elif strategie==1:
        list2=[moderatorinTuer, spielerinTuer]
        switch=auswahl(list2, bereich)
        if verbose: 
            print("Spielerin wechselt")
        if switch==gewinnTuer:
                return True
        else:
                return False            

spiel(1, 3, verbose=True)



#Der Durchschnitt mit der Rekursionsformel
def mean(xss):
    N=0
    for x in xss:
        N+=1
        if N==1:
            xN=x
        else:
            xNN=xN+(x-xN)/N
            xN=xNN
    return (xN)


    def spielen(anzahl, bereich, strategie, verbose):
    gewinnAnteil=[]
    Ergebniss=[]
    anzhl=[]
    wins=0
    for i in range(1, anzahl+1):
        anzhl.append(i)
        ergebnis=int(spiel(strategie, bereich, verbose))
        wins+=ergebnis
        Ergebniss.append(ergebnis)
        gewinnAnteil.append(mean(ergebniss))
    return print('Gewonnen:{:0} aus {:1} Spielen oder {:2.2f}% gewonnen'.format(wins, anzahl, wins/anzahl *100)), plt.plot(anzhl, gewinnAnteil), plt.xlabel('Anzahl der Spieliterationen'),plt.ylabel('Gewinn-Anteil')




