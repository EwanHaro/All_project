"""
Options:
Jouer contre un mur: Cherchez dans la class rectangle,
"""

import time
import pygame
import cv2
import sys
import math
import numpy as np
from random import *

Longueur = 1920
Largeur = 1080

pygame.init()
fenetre = pygame.display.set_mode((Longueur, Largeur))
pygame.display.set_caption('Pong Eternal')

video_path = 'theonlythingtheyfeartest.mp4'
video = cv2.VideoCapture(video_path)

pygame.mixer.music.load('tottfiy.mp3')
pygame.mixer.music.play()


def reset():
    balle.x = Longueur // 2
    balle.y = Largeur // 2
    balle_2.x = Longueur // 2 + 30
    balle_2.x = Largeur // 2 - 30
    for i in liste_balle:
        i.dx = randint(-(Longueur // 266), (Longueur // 266))
        nombre_partie1 = randint(-10, -3)
        nombre_partie2 = randint(3, 10)
        if choice([True, False]):
            nombre_final = nombre_partie1
        else:
            nombre_final = nombre_partie2
        i.dy = nombre_final
        i.couleur = 'white'
    joueur_1.x = 0
    joueur_2.x = Longueur - Largeur // 50
    joueur_1.color = 255
    joueur_2.color = 255
    Fond_couleur.fond_rouge = 0


class Map:
    def __init__(self):
        self.tour = True
        self.framrouge = 0
        self.fond_rouge = 0

    def fond(self):
        self.framrouge += 1
        if self.framrouge == 6:
            self.framrouge = 0
            self.fond_rouge += 1
            if self.fond_rouge == 255:
                self.tour = False



class ball:
    def __init__(self, l, n):
        self.x = Longueur // 2
        self.y = Largeur // 2
        if n == 'b2':
            self.x += 30
            self.y -= 30
        self.dx = randint(-(Longueur // 266), (Longueur // 266))
        nombre_partie1 = randint(-10, -3)
        nombre_partie2 = randint(3, 10)
        if choice([True, False]):
            nombre_final = nombre_partie1
        else:
            nombre_final = nombre_partie2
        self.dy = nombre_final
        self.couleur = (255, 255, 255)
        self.rayon = 20
        self.l = l

    def visuel(self):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.rayon)

    def moove(self):
        self.x += self.dx
        self.y += self.dy

    def colision(self):
        if self.x + self.rayon <= 0:
            reset()
            joueur_2.points += 1
            time.sleep(0.5)
        if self.x - self.rayon >= Longueur:
            reset()
            joueur_1.points += 1
            time.sleep(0.5)
        if self.y - self.rayon <= 0 or self.y + self.rayon >= Largeur:
            self.dy = -self.dy

    def col_rect(self):
        for i in self.l:
            if i == joueur_1:
                if joueur_1.x <= self.x - self.rayon <= joueur_1.x + joueur_1.l \
                        and joueur_1.y <= self.y <= joueur_1.y + joueur_1.h:
                    self.dx = -self.dx + 1
                elif joueur_1.x <= self.x - self.rayon <= joueur_1.x + joueur_1.l \
                        and joueur_1.y <= self.y + self.rayon <= joueur_1.y + joueur_1.h:
                    self.dx = -self.dx + 1
                elif joueur_1.x <= self.x - self.rayon <= joueur_1.x + joueur_1.l \
                        and joueur_1.y <= self.y - self.rayon <= joueur_1.y + joueur_1.h:
                    self.dx = -self.dx + 1
            elif i == joueur_2:
                if joueur_2.x <= self.x + self.rayon <= joueur_2.x + joueur_2.l \
                        and joueur_2.y <= self.y <= joueur_2.y + joueur_2.h:
                    self.dx = -self.dx - 1
                elif joueur_2.x <= self.x + self.rayon <= joueur_2.x + joueur_2.l \
                        and joueur_2.y <= self.y + self.rayon <= joueur_2.y + joueur_2.h:
                    self.dx = -self.dx - 1
                elif joueur_2.x <= self.x + self.rayon <= joueur_2.x + joueur_2.l \
                        and joueur_2.y <= self.y - self.rayon <= joueur_2.y + joueur_2.h:
                    self.dx = -self.dx - 1

    def col_ball(self, liste_ball):
        for i in liste_ball:
            if i != self:
                distance = math.sqrt((self.x - i.x) ** 2 + (self.y - i.y) ** 2)
                if distance <= self.rayon + i.rayon:
                    s = self.dx
                    s1 = self.dy
                    self.dx = i.dx
                    self.dy = i.dy
                    i.dx = s
                    i.dy = s1

    def limite(self):
        if self.dx >= 20:
            self.couleur = 'black'
            self.dx = 20
        elif self.dx <= -20:
            self.couleur = 'black'
            self.dx = -20


class rectangle:
    def __init__(self, x, y, n):
        self.frame_color = 0
        self.x = x
        self.y = y
        self.color = 255
        self.couleur = (self.color, self.color, self.color)
        self.h = Largeur // 5
        '''if n == 'j2':
            self.h = Longueur'''
        self.l = Largeur // 50
        self.points = 0

    def visuel(self):
        pygame.draw.rect(fenetre, self.couleur, (self.x, self.y, self.l, self.h))

    def change_color(self):
        self.frame_color += 1
        if self.frame_color == 5:
            self.frame_color = 0
            self.color -= 1
            self.couleur = (self.color, self.color, self.color)

    def colision(self):
        if self.y < 0:
            self.y = 0
        elif self.y + self.h > Largeur:
            self.y = Largeur - self.h
        if self == joueur_1:
            if self.x < 0:
                self.x = 0
            elif self.x + self.l > Longueur // 2:
                self.x = Longueur // 2 - self.l
        if self == joueur_2:
            if self.x + self.l > Longueur:
                self.x = Longueur - self.l
            elif self.x < Longueur // 2:
                self.x = Longueur // 2


class points:
    def __init__(self, x, y):
        self.points = None
        self.surface = None
        self.x = x
        self.y = y
        self.ma_police = pygame.font.Font(None, 50)
        self.couleur = (255, 255, 255)
        self.position = (self.x, self.y)

    def affiche(self, player):
        self.points = player.points
        self.surface = self.ma_police.render(str(self.points), True, self.couleur)
        fenetre.blit(self.surface, self.position)


def moove_1(keys):
    if keys[pygame.K_z]:
        joueur_1.y -= Largeur // 60
    elif keys[pygame.K_s]:
        joueur_1.y += Largeur // 60
    if keys[pygame.K_q]:
        joueur_1.x -= Largeur // 60
    elif keys[pygame.K_d]:
        joueur_1.x += Largeur // 60


def moove_2(keys):
    if keys[pygame.K_UP]:
        joueur_2.y -= Largeur // 60
    elif keys[pygame.K_DOWN]:
        joueur_2.y += Largeur // 60
    if keys[pygame.K_LEFT]:
        joueur_2.x -= Largeur // 60
    elif keys[pygame.K_RIGHT]:
        joueur_2.x += Largeur // 60


def pause(keys):
    if keys[pygame.K_SPACE]:
        clock.tick(0)


joueur_1 = rectangle(0, 0, 'j1')
joueur_2 = rectangle(Longueur - Largeur // 50, Largeur - Largeur // 5, 'j2')
liste_joueur = [joueur_1, joueur_2]
balle = ball(liste_joueur, 'b1')
balle_2 = ball(liste_joueur, 'b2')
liste_balle = [balle, balle_2]
pts_1 = points(Longueur * 0.33, Largeur * 0.05)
pts_2 = points(Longueur * 0.66, Largeur * 0.05)
Fond_couleur = Map()

running = True
clock = pygame.time.Clock()

while running:

    if Fond_couleur.tour:
        Fond_couleur.fond()
        fenetre.fill((Fond_couleur.fond_rouge,0,0))
    else:
        ret, frames = video.read()
        if ret:
            frame = cv2.resize(frames, (Longueur, Largeur))
            frame = cv2.flip(frame, -1)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.rot90(frame)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            fenetre.blit(frame, (0, 0))

    balle.visuel()
    balle.colision()
    balle.moove()
    balle.col_rect()
    balle.limite()

    if balle.couleur == 'black':
        balle_2.visuel()
        balle_2.colision()
        balle_2.moove()
        balle_2.col_rect()
        balle_2.limite()
        balle_2.col_ball(liste_balle)

    joueur_1.visuel()
    joueur_1.colision()
    moove_1(pygame.key.get_pressed())

    joueur_2.visuel()
    joueur_2.colision()
    moove_2(pygame.key.get_pressed())

    pts_1.affiche(joueur_1)
    pts_2.affiche(joueur_2)
    pause(pygame.key.get_pressed())

    if joueur_1.color != 0:
        joueur_2.change_color()
        joueur_1.change_color()

    pause(pygame.key.get_pressed())

    pygame.display.update()

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
video.release()
sys.exit()
