from random import *


class Humain:
    def __init__(self, name):
        self.pv = randint(70, 130)
        self.max_pv = self.pv
        self.att = randint(5, 10)
        self.inventaire = Inventaire(5)
        self.gold = randint(0, 2000)
        self.xp = 0
        self.name = name


class Inventaire:
    def __init__(self, place_init):
        self.stockage = [place_init]

    def afficher_inventaire(self):
        for i in range(1, len(self.stockage)):
            print(i, ':', self.stockage[i].name)

    def ajouter(self, objet):
        choix = str(input('Voulez vous ajouter cet objet à votre inventaire?\n 1:oui, 0:non'))
        if choix == '1':
            if len(self.stockage) >= self.stockage[0]:
                print('impossible, inventaire plein!')
                return False
            else:
                self.stockage.append(objet)
                print(f'{objet.name} ajouté!')
                return True
        elif choix == '0':
            print('élément ingnoré avec succès!')
            return False

    def ajouter_marchand(self, objet):
        if len(self.stockage) >= self.stockage[0]:
            print('impossible, inventaire plein!')
            return False
        else:
            self.stockage.append(objet)
            print(f'{objet.name} ajouté!')
            return True

    def jeter(self, n_objet):
        if n_objet <= 0 or n_objet >= self.stockage[0]:
            print('erreur de sélection!')
        elif len(self.stockage) <= n_objet:
            print('l emplacement est vide')
        else:
            self.stockage.pop(n_objet)
            print('élément supprimé!')

    def inspecter(self):
        ins = int(input('Qu elle objet à inspecter?'))
        if ins <= 0 or ins >= len(self.stockage):
            print('erreur de sélection')
        else:
            self.stockage[ins].afficher_caracteristique()

    def up_stock(self):
        self.stockage[0] += 1


class Marchand:
    def __init__(self):
        self.nb_objet = randint(3, 5)
        self.dialog_renc = 'Bonjour etranger! J ai quelque chose qui pourrait vous interesser...'
        self.dialog_ach = 'Qu elle objet souhaitez vous acheter?'
        self.dialog_ven = 'Qu elle objet souhaitez vous vendre?'
        self.dialog_conclu = 'Marché conclu!'
        self.dialog_quit = 'à bientôt!'
        self.nb_place = randint(3, 6)
        self.inventaire = Inventaire_Marchand(self.nb_place)


class Inventaire_Marchand:
    def __init__(self, place_init):
        self.stockage = [place_init + 5]

    def afficher_inventaire(self):
        for i in range(1, len(self.stockage)):
            print(i, ':', self.stockage[i].name)

    def ajouter(self, objet):
        if len(self.stockage) >= self.stockage[0]:
            return False
        else:
            self.stockage.append(objet)
            return True

    def jeter(self, n_objet):
        if n_objet <= 0 or n_objet >= self.stockage[0]:
            print('erreur de sélection!')
        elif len(self.stockage) <= n_objet:
            print('l emplacement est vide')
        else:
            self.stockage.pop(n_objet)

    def inspecter(self):
        ins = int(input('Qu elle objet à inspecter?'))
        if ins <= 0 or ins >= len(self.stockage):
            print('erreur de sélection')
        else:
            self.stockage[ins].afficher_caracteristique()


hero = Humain('ewan')
