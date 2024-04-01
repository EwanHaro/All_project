from random import *

liste_objet = ['Sword','Potion']

def create_object():
    type = globals()[choice(liste_objet)]
    print(type)

create_object()    