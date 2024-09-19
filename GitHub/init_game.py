from random import *
from DML_function_pygame import *

"""Bouton Start et son rectangle"""
rect_start_button = pygame.Rect(screen_width * 0.3, screen_height * 0.6, screen_width * 0.4, screen_height * 0.2)
font_start_button = pygame.font.Font(None, 80)
text_start_button = font_start_button.render("START", True, (88, 41, 0))
rect_text_start_button = text_start_button.get_rect()
rect_text_start_button.center = rect_start_button.center

"""Nom du jeu sur la page home"""
font_title_breitfield = pygame.font.Font(None, 320)
font_title_and_the_quest = pygame.font.Font(None, 240)
font_title_for_perfection = pygame.font.Font(None, 280)

text_title_breitfield = font_title_breitfield.render("BREITFIELD", True, (0, 0, 255))
text_title_and_the_quest = font_title_and_the_quest.render("AND THE QUEST", True, (255, 0, 0))
text_title_for_perfection = font_title_for_perfection.render("for PERFECTION", True, (182, 102, 210))

"""Texte qui annonce à qui le tour"""
font_lap = pygame.font.Font(None,50)
surface_text_lap = font_lap.render(f"Au tour de l'équipe {Color_of_lap.get_lap_color()}!", True, (0, 0, 0))
rect_texte_lap = surface_text_lap.get_rect()
rect_texte_lap.centerx = screen_width // 2


"""Immense if else qui différencie si l'utilisateur demande à faire une vrai partie ou une partie de test"""
if int(input("0: Mod Test; 1: Mod Pick")) == 1:
    liste_power_dragon_generated = team_dragon_pick()
    list_dragon_blue = []
    list_dragon_red = []
    for j in range(liste_power_dragon_generated[-1]):
        list_dragon_blue.append(Dragon(f'Dragon_bleu_{j + 1}', 500, 100, 100, liste_power_dragon_generated[0][j],
                                       liste_power_dragon_generated[1][j]))
        list_dragon_red.append(Dragon(f'Dragon_rouge_{j + 1}', 500, 100, 100, liste_power_dragon_generated[2][j],
                                      liste_power_dragon_generated[3][j]))
    list_dragon_blue.append("Blue")
    list_dragon_red.append("Red")

else:
    choice_random_or_not = int(input("Quel type de partie? 0: random; 1: normal"))
    if choice_random_or_not == 1:
        list_dragon_blue = [
            Dragon(f'Dragon_bleu_{1}', 500, 100, 100, ["metal", "legendary"],
                   [1, 1, 1]),
            Dragon(f'Dragon_bleu_{2}', 500, 100, 100, ["earth", "poison"],
                   [1, 1, 1]),
            Dragon(f'Dragon_bleu_{3}', 500, 100, 100, ["disease", "shadow"],
                   [1, 1, 1]),
            "Blue"
        ]
        list_dragon_red = [
            Dragon(f'Dragon_rouge_{1}', 500, 100, 100, ["fire", "wind"],
                   [1, 1, 1]),
            Dragon(f'Dragon_rouge_{2}', 500, 100, 100, ["void", "wind"],
                   [1, 1, 1]),
            Dragon(f'Dragon_rouge_{3}', 500, 100, 100, ["metal", "poison"],
                   [1, 1, 1]),
            "Red"
        ]
    else:
        liste_power_random_blue = sample(liste_power,6)
        liste_power_random_red = sample(liste_power, 6)
        list_dragon_blue = [
            Dragon(f'Dragon_bleu_{1}', 500, 100, 100, [liste_power_random_blue[0],liste_power_random_blue[1]],
                   [1, 1, 1]),
            Dragon(f'Dragon_bleu_{2}', 500, 100, 100, [liste_power_random_blue[2],liste_power_random_blue[3]],
                   [1, 1, 1]),
            Dragon(f'Dragon_bleu_{3}', 500, 100, 100, [liste_power_random_blue[4],liste_power_random_blue[5]],
                   [1, 1, 1]),
            "Blue"
        ]
        list_dragon_red = [
            Dragon(f'Dragon_rouge_{1}', 500, 100, 100, [liste_power_random_red[0],liste_power_random_red[1]],
                   [1, 1, 1]),
            Dragon(f'Dragon_rouge_{2}', 500, 100, 100, [liste_power_random_red[2],liste_power_random_red[3]],
                   [1, 1, 1]),
            Dragon(f'Dragon_rouge_{3}', 500, 100, 100, [liste_power_random_red[4],liste_power_random_red[5]],
                   [1, 1, 1]),
            "Red"
        ]

'''Définitions des rectangles de collision ET association de chaque perso à ses animations'''
liste_rectangle_coll_drag_bl = []
liste_rectangle_coll_drag_re = []
for i in range(3):
    liste_rectangle_coll_drag_bl.append(
        pygame.Rect(640, 285 + i * 150,
                    80, 120))
for i in range(3):
    liste_rectangle_coll_drag_re.append(
        pygame.Rect(1220, 285 + i * 150,
                    80, 120))

"""Conceptions des image lié au pouvoir, renvoie une liste contenant pour chaque pouvoir:
    l'image, position x, position y, rectangle de colision de l'image,le dragon et le pouvoir """
liste_image_power_blue = create_image_power(liste_rectangle_coll_drag_bl, list_dragon_blue, 0, 0, 1)
liste_image_power_red = create_image_power(liste_rectangle_coll_drag_re, list_dragon_red, 1, 50, -1)

if MUSIC == 1:
    pygame.mixer.music.load("Music//music_no_more_heroes.mp3")
    pygame.mixer.music.play(-1)

"""définie la police d'écriture, dans son style et sa taille"""
font_end = pygame.font.Font(None, round(screen_height // 15))
font_neutral = pygame.font.Font(None, round(screen_height // 20))
font_blue = pygame.font.Font(None, round(screen_height // 30))
font_red = pygame.font.Font(None, round(screen_height // 30))

surface_end = font_end.render("Fin de partie!", True, (0, 0, 0))
text_end_rect = surface_end.get_rect()
text_end_rect.center = (screen_width // 2, screen_height // 2)

"""Définitions du rectangle du bouton skip"""
rect_skip_buttom = pygame.Rect((screen_width // 2) - 150, screen_height - 100, 200, 100)
surface_skip_button = font_neutral.render("skip", True, (0, 0, 0))

liste_sprite_left = []
liste_sprite_right = []
liste_health_bar_left = []
liste_health_bar_right = []
shadow_of_sprite = pygame.image.load("Sprite//neutral//ombre.png")
shadow_of_sprite = pygame.transform.scale(shadow_of_sprite, (125, 43))

for i in range(3):
    sprite_left = pygame.image.load("Sprite//sprite_left//sprite_01.png")
    sprite_left = pygame.transform.scale(sprite_left, (125, 125))
    liste_sprite_left.append(sprite_left)

    sprite_right = pygame.image.load("Sprite//sprite_right//sprite_00.png")
    sprite_right = pygame.transform.scale(sprite_right, (125, 125))
    liste_sprite_right.append(sprite_right)
