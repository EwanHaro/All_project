import pygame

pygame.init()
"""Initialisation de l'interface pygame"""
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
pygame.display.set_caption("Dragon Mania Legend")

clock = pygame.time.Clock()


