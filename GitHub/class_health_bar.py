import pygame


class HealthBar:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health
        self.width = 200
        self.height = 20
        self.bar_surface = pygame.Surface((self.width, self.height))

    def update(self, health):
        self.current_health = health
        # Calcul du pourcentage de points de vie restants
        health_percentage = self.current_health / self.max_health
        # Mise à jour de la largeur de la surface de la barre de points de vie
        self.bar_surface = pygame.Surface((int(self.width * health_percentage), self.height))

    def draw(self, surface, x, y):
        surface.blit(self.bar_surface, (x, y))