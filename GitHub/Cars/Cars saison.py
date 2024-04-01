# Saison Cars
from random import *
from time import *
import pygame
import matplotlib.pyplot as plt
import math

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('C:/Users/ewanh/Desktop/Ewan/Codage/Mini-code/Cars/real_gone.mp3')

b = 1  # boucle de jeu, ne pas toucher

re_vi = []  # Par défaut
vit_max = 300  # 300
nb_de_tour = 3  # 3
taille_tour = 4000  # 4000            Dure environ 2min 50
entre_tour = 0 # 1
proba_acc = 50  # 50
proba_der = 60  # 60

liste_numero_car = ["43", "86", "95", "20",
                    "02", "07", "01",
                    "06", "05", "08",
                    "24", "09", "04",
                    "34", "11", "10",
                    "44", "47", "40",
                    "51", "55", "59",
                    "62", "64", "63",
                    "71", "74", "78",
                    "38", "87", "88",
                    "90", "93", "99",
                    "03", "12", "23",
                    "35", "45", "56"]

liste_voiture_ref = {
    "95": 'Flash Mqueen',
    "43": 'The King',
    "86": 'Chick Hicks',
    "20": 'Jackson Storm',
    "51": 'Doc Hudson ',
    "01": "Francesco Bernoulli",
    "02": "Lewis Hamilton",
    "05": "Miguel Camino",
    "08": "Carla Veloso",
    "06": "Raoul ÇaRoule",
    "09": "Nigel Gearsley",
    "07": "Shu Todoroki",
    "04": "Max Schnell",
    "10": "Rip Clutchgoneski",
    "11": "Junior Moon",
    "34": "River Scott",
    "90": "Ponchy Wipeout",
    "24": "Brick Yardley",
    '44': 'Turbo Thunder',
    '47': 'Blitz Lightning',
    '40': 'Rapid Runner',
    '55': 'Velocity Vortex',
    '59': 'Power Surge',
    '62': 'Nitro Nova',
    '64': 'Sonic Speedster',
    '63': 'Swift Striker',
    '71': 'Rocket Racer',
    '74': 'Fury Falcon',
    '78': 'Thunder Thrust',
    '38': 'Supersonic Streak',
    '87': 'Vortex Voyager',
    '88': 'Stealth Sprinter',
    '12': 'Blaze Bolt',
    '93': 'Lightning Lancer',
    '99': 'Flashfire Flame',
    '03': 'Whirlwind Warrior',
    '23': 'Thunderbolt Tempest',
    '35': 'Blast Burner',
    "45": "Retro Racer",
    "56": "Turbo Thruster"}

liste_old_cars = ["51", "11", "34", "6", "44", "88", "40"]
liste_new_cars = ["1", "8", "20", "59", '99']


class Old_Cars:
    def __init__(self):
        self.random = [[4, 8], [0, 5], [-2, 4], [-2, 3], [-3, 3], [-3, 1]]
        self.limite_var = [[0, 15], [0, 8], [-3, 6], [-4, 5], [-5, 5], [-6, 2]]


class Modern_Cars:
    def __init__(self):
        self.random = [[3, 7], [0, 4], [-1, 3], [-2, 3], [-3, 3], [-3, 2]]
        self.limite_var = [[0, 15], [0, 8], [-2, 6], [-3, 5], [-4, 4], [-5, 2]]


class New_Cars:
    def __init__(self):
        self.random = [[2, 6], [0, 3], [0, 3], [-2, 3], [-2, 2], [-3, 2]]
        self.limite_var = [[0, 15], [0, 8], [0, 6], [-2, 5], [-3, 3], [-4, 2]]


class Voiture:
    def __init__(self, numero, depart, name=''):
        self.var = 0
        self.var_min = 0
        self.var_max = 10
        self.stock_var = 0
        self.num = int(numero)
        self.speed = 0
        self.score = depart
        self.name = name
        if str(self.num) in liste_old_cars:
            self.type = Old_Cars()
        elif str(self.num) in liste_new_cars:
            self.type = New_Cars()
        else:
            self.type = Modern_Cars()

    def resultat(self):
        if self.speed < 100:
            self.var = randint(self.type.random[0][0], self.type.random[0][1])
            self.var_max = self.type.limite_var[0][1]
            self.var_min = self.type.limite_var[0][0]
        elif 100 <= self.speed < 150:
            self.var = randint(self.type.random[1][0], self.type.random[1][1])
            self.var_max = self.type.limite_var[1][1]
            self.var_min = self.type.limite_var[1][0]
        elif 150 <= self.speed < 200:
            self.var = randint(self.type.random[2][0], self.type.random[2][1])
            self.var_max = self.type.limite_var[2][1]
            self.var_min = self.type.limite_var[2][0]
        elif 200 <= self.speed < 250:
            self.var = randint(self.type.random[3][0], self.type.random[3][1])
            self.var_max = self.type.limite_var[3][1]
            self.var_min = self.type.limite_var[3][0]
        elif 250 <= self.speed < 290:
            self.var = randint(self.type.random[4][0], self.type.random[4][1])
            self.var_max = self.type.limite_var[4][1]
            self.var_min = self.type.limite_var[4][0]
        else:
            self.var = randint(self.type.random[5][0], self.type.random[5][1])
            self.var_max = self.type.limite_var[5][1]
            self.var_min = self.type.limite_var[5][0]
        self.stock_var += self.var
        if self.stock_var > self.var_max:
            self.stock_var = self.var_max
        elif self.stock_var < self.var_min:
            self.stock_var = self.var_min
        self.speed += self.stock_var
        if self.speed > vit_max:
            self.speed = vit_max
        self.score += self.speed / 3.6
    
    def get_pos(self, liste_voiture):
        for i in range(len(liste_voiture)):
            if liste_voiture[i].num == self.num:
                return i+1
        


def position_de_depart():
    shuffle(liste_numero_car)
    for x in range(len(liste_numero_car)):
        liste_pos.append(x * -3)


def tour():
    for i in liste_cars:
        i.resultat()
    liste_voiture_trie = sorted(liste_cars, key=lambda x: x.score, reverse=True)
    return liste_voiture_trie


def sim_accident(liste_voiture):
    if randint(0, proba_acc) == proba_acc:
        voiture_acc = liste_voiture[randint(0, len(liste_voiture) - 1)]
        voiture_acc.speed = -20  # -20 pour simuler le redémarrage du véhicule
        print(f'accident pour la voiture n°{voiture_acc.num}! ')
    for rien in range(0, 3):
        if randint(0, proba_der) == proba_der:
            voiture_derap = liste_voiture[randint(0, len(liste_voiture) - 1)]
            voiture_derap.speed = round(voiture_derap.speed * (randint(90, 99) / 100))
            print(f'dérapage pour la voiture n°{voiture_derap.num}! ')
    return liste_voiture


def affiche_position(liste_voiture):
    print('\n')
    print(f'tour {math.floor(liste_voiture[0].score / taille_tour) + 1}/{nb_de_tour}            {(liste_voiture[0].score/taille_tour)*100}')
    print(
        f'1er :  n°{liste_voiture[0].num}  speed: {liste_voiture[0].speed}km/h                      {liste_voiture[0].name}')
    for i in range(1, 9):
        print(f'{i + 1}eme:  n°{liste_voiture[i].num}  speed: {liste_voiture[i].speed}km/h,'
              f' dif_mètre: {round(liste_voiture[i - 1].score - liste_voiture[i].score)}    {liste_voiture[i].name}')
    for i in range(9, 40):
        print(f'{i + 1}eme: n°{liste_voiture[i].num}  speed: {liste_voiture[i].speed}km/h,'
              f' dif_mètre: {round(liste_voiture[i - 1].score - liste_voiture[i].score)}    {liste_voiture[i].name}')


def course():
    nb_sec = 0
    initialisation_course()
    stat_voiture_vit = [[] for i in range(len(liste_cars))]
    stat_voiture_pos = [[] for i in range(len(liste_cars))]
    print('Départ de la course!')
    affiche_position(liste_cars)
    sleep(5)
    print('3\n')
    sleep(1)
    print('2\n')
    sleep(1)
    print('1\n')
    sleep(1)
    r = tour()
    r = sim_accident(r)
    affiche_position(r)
    for y in range(len(liste_cars)):
        stat_voiture_vit[y].append(liste_cars[y].speed)
    sleep(entre_tour)
    while r[0].score / taille_tour < nb_de_tour:  # boucle de course
        r = tour()
        r = sim_accident(r)
        #affiche_position(r)  # affiche à chaque tour
        nb_sec += 1
        for y in range(len(liste_cars)):
            stat_voiture_vit[y].append(liste_cars[y].speed)
            stat_voiture_pos[y].append(liste_cars[y].get_pos(r))
        sleep(entre_tour)
    affiche_position(r)                              #affiche seulement l'arrivée
    print(f'durée de la course = {nb_sec // 60} minutes et {nb_sec % 60} secondes')
    return stat_voiture_vit


def initialisation_course():
    position_de_depart()
    position = 0
    for i in liste_numero_car:
        ref = liste_voiture_ref[i]
        liste_cars.append(Voiture(i, liste_pos[position], ref))
        position += 1


def statistique_voiture(resultat_vitesse):
    ind = int(input("Qu'elle voiture voulez vous analyser?"))
    global re
    for i in range(len(liste_cars)):
        if liste_cars[i].num == ind:
            re = i
    l_n = []
    for i in range(len(resultat_vitesse[re])):
        l_n.append(i)
    x = l_n
    y = resultat_vitesse[re]
    moy_speed = 0
    for i in resultat_vitesse[re]:
        moy_speed += i
    moy_speed = moy_speed / len(resultat_vitesse[re])
    print(f'vitesse moyenne de la voiture n°{ind}, {liste_cars[re].name}: {moy_speed}')
    plt.plot(x, y)
    plt.title(f'statistique de la voiture n°{ind}, {liste_cars[re].name}')
    plt.xlabel('Seconde')
    plt.ylabel('Vitesse(km/h)')
    plt.show()


while b != 0:
    a = int(input('1: course, 2: analyser, 3: couper la music, 4: quitter'))
    if a == 1:
        if int(input('Musique? 1:oui, 0: non')) == 1:
            pygame.mixer.music.play()
        liste_pos = []
        liste_cars = []
        re_vi = course()
    elif a == 2:
        statistique_voiture(re_vi)
    elif a == 3:
        pygame.mixer.music.stop()
    elif a == 4:
        b = 0
