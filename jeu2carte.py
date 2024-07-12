import random


#Liste de carte random de 0 à 53
def jeudecarte():
    tas_random=[]
    for i in range(0,54):
        tas_random.append(i)
        #print(i)
    random.shuffle(tas_random)
    return tas_random


def tri(carte):
    n=len(carte)
    for i in range(n-1 ):
        j= i+1
        if carte[i] >= carte[j]:
            carte[i],carte[j]=carte[j],carte[i]
        
        #ChatGpt
        #for j in range(0, n-i-1):
            #if carte[j] > carte[j+1]:
                # Swap the elements
                #carte[j], carte[j+1] = carte[j+1], carte[j]
    return carte


def conversion(liste_carte):
    #13 cartes par couleur
    jeux=[]
    #4 couleurs (trefle,pique,coeur,carreau)
    couleur=[]
    for i in range (0,54):
        if liste_carte[i]>=0 and liste_carte[i]<=12:
            couleur.append(str(i+1) + ' de coeur')
        elif liste_carte[i]>=13 and liste_carte[i]<=25 :
            couleur.append(str(i-12) + ' de trefle')
        elif liste_carte[i]>=26 and liste_carte[i]<=38 :
            couleur.append(str(i-25) + ' de carreau')
        elif liste_carte[i]>=39 and liste_carte[i]<=51 :
            couleur.append(str(i-38) +' de pique')
        else:
            couleur.append('joker')
    return couleur



#jeu=[2,5,7,3,8,9,4,1]
deck=jeudecarte()

for k in range(0,53):
    jeu=tri(deck)

for k in range(0,53):
    convers=conversion(jeu)
    #print (convers[k+1])
#print (convers[1][0]+convers[0][0])
print (convers)
#print(jeu)

