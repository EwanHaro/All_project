def creer_pile_vide():
    return []


def est_vide(pile):
    return len(pile) == 0


def empiler(pile, valeur):
    pile.append(valeur)


def depiler(pile):
    if not est_vide(pile):
        return pile.pop()


def hauteur_pile(pile):
    return len(pile)


def max_pile(pile, limite):
    if est_vide(pile):
        return -1  # Retourne une valeur indiquant que la pile est vide

    max_val = 0
    max_index = 0

    for i in range(limite, len(pile)):
        if pile[i] > max_val:
            max_val = pile[i]
            max_index = i

    return max_index


def tri_crepes(pile):
    de = 0
    for i in range(len(pile)):
        taille_pile = hauteur_pile(pile)
        i_max_crepe = max_pile(pile, de)
        retourner_pile(pile, len(pile) - i_max_crepe)
        retourner_pile(pile, len(pile)- de)
        de += 1


def retourner_pile(pile, k):
    temp_pile = creer_pile_vide()

    for _ in range(k):
        empiler(temp_pile, depiler(pile))
        print(pile)
    temp_pile.reverse()
    while not est_vide(temp_pile):
        empiler(pile, depiler(temp_pile))
        print(pile)


# Exemple d'utilisation
pile_crepes = creer_pile_vide()
for diametre in [5, 2, 8, 3, 1, 7, 4, 6]:
    empiler(pile_crepes, diametre)

print("Pile de crêpes avant le tri :", pile_crepes)
tri_crepes(pile_crepes)
print("Pile de crêpes après le tri :", pile_crepes)
