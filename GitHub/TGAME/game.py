from random import *
from chambre import random_chambre
from Personnage import *

GAME = True
t = '1'


def action_inventaire():
    ac = str(input('1: ouvrir 2: inspecter 3: supprimer, 4: retour'))
    if ac != '1' and ac != '2' and ac != '3' and ac != '4':
        print('erreur d action')
        return action_inventaire()
    else:
        return ac


def fin():
    banane = str(input('Etes vous sur de vouloir quitter?\n1 pour rester, 0 pour quitter'))
    if banane == '0':
        print('FIN DE PARTIE')
        return False
    else:
        return True


while GAME:
    t = str(input("1:inventaire, 2:pièce suivante, 3:quitter"))
    while t == '1':
        action = action_inventaire()
        if action == '1':
            hero.inventaire.afficher_inventaire()
            print(f'pv:{hero.pv}/{hero.max_pv}', hero.gold, 'gold')
        elif action == '2':
            hero.inventaire.inspecter()
        elif action == '3':
            hero.inventaire.afficher_inventaire()
            hero.inventaire.jeter(int(input('Qu elle objet souhaitez vous supprimer?')))
        elif action == '4':
            t = '0'
    while t == '2':
        random_chambre()
        t = '0'
    while t == '3':
        t = '0'
        GAME = fin()
