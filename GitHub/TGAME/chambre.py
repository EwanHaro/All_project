from random import *
from Personnage import *
from object_game import *

etage_chambre = 0
liste_type_chambre = ['chambre_chest', 'chambre_commerce', 'chambre_fight']


def chambre_chest():
    coffre_obj = create_object()
    coffre_gold = randint(1, 10)
    hero.gold += coffre_gold
    print(f'C est une salle de coffre!\n Vous avez trouvé {coffre_obj.name} et {coffre_gold} gold!')
    hero.inventaire.ajouter(coffre_obj)


def chambre_marchand():
    s = '1'
    marchand = Marchand()
    for i in range(marchand.nb_place):
        obj_cr = create_object()
        marchand.inventaire.ajouter(obj_cr)
    print(marchand.dialog_renc)
    while s != '0':
        s = str(input(
            f'\n1: inventaire, 2: inspecter, 3: acheter, 4: vendre,\n5: inventaire {hero.name}, 6: inspecter {hero.name} 0: quitter\n'))
        if s == '1':
            marchand.inventaire.afficher_inventaire()
        elif s == '3':
            ach = int(input(marchand.dialog_ach))
            if ach <= 0 or ach >= marchand.inventaire.stockage[0]:
                print('erreur de sélection!')
            else:
                if marchand.inventaire.stockage[ach].prix > hero.gold:
                    print('fond insufisant')
                else:
                    verif_ajout = hero.inventaire.ajouter(marchand.inventaire.stockage[ach])
                    if verif_ajout:
                        hero.gold -= marchand.inventaire.stockage[ach].prix
                        marchand.inventaire.jeter(ach)
        elif s == '2':
            marchand.inventaire.inspecter()
        elif s == '4':
            ven = int(input(marchand.dialog_ven))
            if ven <= 0 or ven >= hero.inventaire.stockage[0]:
                print('erreur de sélection!')
            else:
                verif_achat = int(input(
                    f'Etes vous sur de vouloir vendre {hero.inventaire.stockage[ven].name} pour {round(hero.inventaire.stockage[ven].prix * 0.9, 0)}?\n1 pour confirmer, 0 pour annuler'))
                if verif_achat == 1:
                    verif_ajout = marchand.inventaire.ajouter(hero.inventaire.stockage[ven])
                    if verif_ajout:
                        hero.gold += round(hero.inventaire.stockage[ven].prix * 0.9, 0)
                        hero.inventaire.jeter(ven)
        elif s == '5':
            hero.inventaire.afficher_inventaire()
            print(f'pv:{hero.pv}/{hero.max_pv}', hero.gold, 'gold')
        elif s == '6':
            hero.inventaire.inspecter()


def random_chambre():
    global etage_chambre
    etage_chambre += 1
    print('étage n°', etage_chambre)
    x = randint(1, 2)
    if x == 1:
        chambre_marchand()
    else:
        chambre_chest()
    # globals()[choice(liste_type_chambre)]


def create_object():
    chosen_class_name = choice(liste_objet)

    # Créez une instance de la classe correspondante
    if chosen_class_name == 'Sword':
        return Sword()
    elif chosen_class_name == 'Potion':
        return Potion()
