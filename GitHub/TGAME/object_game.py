from random import *

liste_prenom_epee = ['Excalibur', 'Durandal', 'Caliburn', 'Gelée', 'Andúril', 'Narsil', 'Épeclair', 'Séraphlame',
                     'Égiscroc', 'Mercure']
liste_nom_epee = ["de l'Ombre", 'de la Nuit', 'Solaire', 'des Etoiles', 'de Sang', 'du serment', 'de la Flamme',
                  'du Givre', 'Runique', 'du Grand']

liste_nom_potion = ['Élixir', 'Philtre', 'Breuvage', 'Potion', 'Infusion', 'Fiole', 'Remède', 'Infusion', 'Boisson',
                    'Sortilège']

liste_objet = ['Sword', 'Potion']


class Sword:
    def __init__(self):
        self.level = randint(1, 10)
        self.degats = round((randint(5, 10) + (10 * random())) * (1 + self.level / 10), 0)
        self.durability = randint(0, 80) + 20
        prenom = choice(liste_prenom_epee)
        nom = choice(liste_nom_epee)
        self.prix = round(self.degats * self.level * self.durability * 0.1, 0)
        self.name = prenom + ' ' + nom

    def afficher_caracteristique(self):
        print('nom:', self.name, 'lvl:', self.level, '\ndegats:', self.degats, 'durabilité:', self.durability, 'prix:',
              self.prix)


class Potion:
    def __init__(self):
        self.level = randint(1, 10)
        self.durability = 1
        self.name = choice(liste_nom_potion)
        self.regeneration = round(randint(10, 20) * (1 + self.level / 10), 2)
        self.prix = round(self.regeneration * self.level, 0)

    def afficher_caracteristique(self):
        print('nom:', self.name, 'lvl:', self.level, '\nsoin:', self.regeneration, 'durabilité:', self.durability,
              'prix:', self.prix)
