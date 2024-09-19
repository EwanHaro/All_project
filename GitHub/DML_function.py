from class_dragon import *
from class_power import *

MUSIC = int(input("Music? 0:non, 1:oui"))

if MUSIC == 1:
    pygame.mixer.music.load("Music//Lol_song_partie_1.mp3")
    pygame.mixer.music.play(-1)

"""Class Lap permet sert uniquement de renseignement, elle contient la couleur de l'équipe qui est en train de jouer"""


class Lap:
    def __init__(self):
        self.lap_color = 'Blue'

    def get_lap_color(self):
        return self.lap_color

    def set_lap_color(self, color):
        self.lap_color = color



Color_of_lap = Lap()


def statistique(l_drag):
    """Met en forme les statistiques à afficher sur l'interface pygame"""
    liste_statistique = []
    for i in range(len(l_drag) - 1):
        info_l0 = l_drag[i].health/l_drag[i].health_max
        info_l1 = l_drag[i].list_effect_actif
        liste_element = [info_l0, info_l1]
        liste_statistique.append(liste_element)

    return liste_statistique


def print_liste(liste):
    """transforme une liste d'élément en str"""
    string_liste = ""
    if liste == []:
        return string_liste
    string_liste += f"{liste[0]}"
    for i in range(1, len(liste)):
        string_liste += f", {liste[i]}"
    return string_liste


def boucle_jeu(team, ennemy):
    """affect les effets aux ennemis et comptabilise les tours qui passent"""
    liste_of_teams = [team, ennemy]
    for i in range(len(team) - 1):
        team[i].list_effect_actif = []
        ennemy[i].list_effect_actif = []
        team[i].is_affect_poison()
        team[i].is_sick()
        team[i].round_wind -= 1
        team[i].round_earth -= 1
        team[i].round_metal -= 1
        team[i].round_legendary -= 1
        team[i].stun -= 1
        for k in [team, ennemy]:
            k[i].what_effect()
    for i in range(len(liste_of_teams)):
        if check_dead_team(liste_of_teams[i]):
            print(f"L'équipe de {liste_of_teams[i - 1][-1]} remporte la partie!")
            return True
    print(f"Au tour de l'équipe {team[-1]}!")
    Color_of_lap.set_lap_color(team[-1])


def check_dead_team(team):
    """Compte les morts, vérifie si une équipe a perdu, et rend les dragons morts intouchable et inutilisable"""
    dead = 0
    for i in range(len(team) - 1):
        if team[i].health <= 0:
            team[i].health = 0
            dead += 1
            if team[i] in liste_drag_dead:
                pass
            else:
                liste_drag_dead.append(team[i])
                print(f'{team[i].name} est mort')
                team[i].name += "(mort)"

    if dead == len(team) - 1:
        return True
    else:
        return False


def is_dead_interface(dragon):
    """Vérifie si un dragon est mort"""
    if dragon in liste_drag_dead:
        return True
    else:
        return False


def team_dragon_pick():
    """Système de sélection du jeu(ban et choix des pouvoirs, classe des dragons..."""
    global liste_power
    liste_power_dragon_blue = []
    liste_power_dragon_red = []
    liste_type_drag_blue = []
    liste_type_drag_red = []
    print("Règle")
    nb_of_dragon = 3
    nb_of_power = int(input("Combien de power par dragon?(2 par défault)"))
    liste_power = start_ban_power(liste_power)
    print("Mise en place des Dragons!")
    if MUSIC == 1:
        pygame.mixer.music.load("Music//Lol_song_partie_3.mp3")
        pygame.mixer.music.play(-1)
    for i in range(nb_of_dragon):
        print(f"Pick du Dragon Bleu n°{i + 1}")
        liste_power_dragon_blue = power_pick(nb_of_power, liste_power_dragon_blue)
        liste_type_drag_blue = type_pick(liste_type_drag_blue)
        print(f"Pick du Dragon Rouge n°{i + 1}")
        liste_power_dragon_red = power_pick(nb_of_power, liste_power_dragon_red)
        liste_type_drag_red = type_pick(liste_type_drag_red)
    return [liste_power_dragon_blue, liste_type_drag_blue, liste_power_dragon_red, liste_type_drag_red,
            nb_of_dragon]  #3 = nombre de dragon


def start_ban_power(liste_power):
    """Lance le système de ban"""
    if MUSIC == 1:
        pygame.mixer.music.load("Music//Lol_song_partie_2.mp3")
        pygame.mixer.music.play(-1)
    for i in ["Blue", "Red"]:
        liste_power = ban_power(liste_power, i)
    return liste_power


def ban_power(liste_power, player):
    """Système de ban"""
    print(liste_power)
    power_ban = str(input(f"Joueur {player}! Quel power banissez vous?"))
    if power_ban == "skip":
        print(f"Aucun pouvoir n'a été banni par le joueur {player}!")
        return liste_power
    elif power_ban in liste_power:
        liste_power.remove(power_ban)
        print(f"Vous avez Banni le power {power_ban}!")
        return liste_power
    else:
        print("Le pouvoir n'existe pas, ou a déjà été ban! Veuillez réessayer")
        return ban_power(liste_power, player)


def power_pick(nb_of_power, liste_power_dragon_total):
    """Choix des pouvoirs"""
    liste_power_dragon = []
    print(liste_power)
    for j in range(nb_of_power):
        start_pick_power = str(input(f"pouvoir n°{j + 1}?"))
        if start_pick_power in liste_power:
            print("Power accordé!")
            liste_power_dragon.append(start_pick_power)
        else:
            print("Erreur de sélection, le pouvoir n'existe pas ou il a été ban! On reccomence! Bon courage... :)")
            return power_pick(nb_of_power, liste_power_dragon_total)
    liste_power_dragon_total.append(liste_power_dragon)
    return liste_power_dragon_total


def type_pick(liste_type_total):
    """Choix des classes de dragons"""
    print(list(dico_type_dragon.keys()))
    start_type_pick = str(input("Type de dragon?"))
    if start_type_pick in dico_type_dragon.keys():
        print("Type accordé!")
        liste_type_total.append(dico_type_dragon[start_type_pick])
        return liste_type_total
    else:
        print("Erreur de sélection, le type n'existe pas! On reccomence! Bon courage... :)")
        return type_pick(liste_type_total)
