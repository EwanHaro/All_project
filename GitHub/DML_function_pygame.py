from DML_function import *
import math


def print_sprite(liste_sprite, x, screen, shadow_of_sprite):
    y = 270
    for i in range(len(liste_sprite)):
        screen.blit(shadow_of_sprite, (x, (y + i * 150) + 100))
        screen.blit(liste_sprite[i], (x, y + i * 150))


def print_statistique(list_dragon, font, screen, x, code_color, taille_icon_power, side, modif_color, direction_print,
                      is_red):
    """affiche les statistiques sur l'interface pygame, var_for_mult_things permet de compter les tours"""
    y_health_bar = 250
    var_for_mult_things = 0
    for i in statistique(list_dragon):

        screen.blit(pygame.transform.scale(
            pygame.image.load(f"Sprite//sprite_{side}//hit_point_bar//barre_de_vie_{math.ceil(i[0] * 4)}.png"),
            (200, 50)),
            (x, y_health_bar + var_for_mult_things * 150))
        surface_hp = font.render(
            f"{list_dragon[var_for_mult_things].health}/{list_dragon[var_for_mult_things].health_max}", True,
            (255, 255, 255))
        screen.blit(surface_hp, (x + is_red, y_health_bar + var_for_mult_things * 150))
        y = (y_health_bar + var_for_mult_things * 150) + 50

        for j in range(len(i[1])):
            screen.blit(i[1][j][0], (x + (modif_color + (j * taille_icon_power[0])) * direction_print, y))
            surface_effect = font.render(i[1][j][1], True, code_color)
            screen.blit(surface_effect, (x + (modif_color + (j * taille_icon_power[0])) * direction_print, y))
        var_for_mult_things += 1


def skip_button(rect_buttom, screen, screen_width, screen_height, surface_skip_button, mouse_pos):
    pygame.draw.rect(screen, (0, 0, 0), rect_buttom, 5)
    screen.blit(surface_skip_button, ((screen_width // 2) - 87, screen_height - 75))


def create_image_power(liste_rectangle_coll_drag, list_dragon, lap_player, is_red, direction_team):
    """construit les image de tout les pouvoir d'une équipe, avec son png, sa position x y,son carré
    de collision, son dragon et son pouvoir. is_red permet le décalage pour l'équipe rouge"""
    liste_power_image_create = []
    for i in range(len(liste_rectangle_coll_drag)):
        liste_coin_calc_pos_image_power = [liste_rectangle_coll_drag[i].topright,
                                           liste_rectangle_coll_drag[i].topleft]
        posxy = liste_coin_calc_pos_image_power[lap_player]

        for j in range(len(list_dragon[i].power)):
            image_power = dico_image_effect_power[list_dragon[i].power[j]]

            pos_x_image_power = posxy[0] - is_red + (j // 2 * taille_icon_power[0]) * direction_team
            pos_y_image_power = posxy[1] + 70 * (j % 2)
            image_power_rect_coll = pygame.Rect(pos_x_image_power, pos_y_image_power, 75, 75)
            liste_power_image_create.append(
                Power(image_power, list_dragon[i].power[j], list_dragon[i], pos_x_image_power, pos_y_image_power,
                      image_power_rect_coll))
    return liste_power_image_create


'''
[image_power, pos_x_image_power, pos_y_image_power, image_power_rect_coll, list_dragon[i],
                 list_dragon[i].power[j]])'''


def print_power(liste_image_power, screen):
    """ affiche les povoirs d'une équipe avec leur image
    liste_image_power contient 6 information:
     l'image, la position x, la position y, le rectangle de colision de l'image,le dragon et le pouvoir """
    for i in range(len(liste_image_power)):
        screen.blit(liste_image_power[i].image_load, (liste_image_power[i].pos_x, liste_image_power[i].pos_y))
        # pygame.draw.rect(screen, (0, 0, 0), liste_image_power[i][3], 3) -> Permet de voir la colision du pouvoir


def if_power_is_click(liste_image_power, mouse_pos):
    """Vérifie si un power est cliqué"""
    for i in range(len(liste_image_power)):
        if liste_image_power[i].rect_coll.collidepoint(mouse_pos):  #vérifie la colision
            if is_dead_interface(liste_image_power[i].dragon):
                print("Votre dragon est mort")
            else:
                if liste_image_power[i].dragon.is_affect_stun():
                    print("impossible, ce dragon est assomé")
                else:
                    return [True, liste_image_power[i].dragon, liste_image_power[i]]  #renvoie le dragon et le pouvoir
    return [False, "None", "None"]


def mouvement_power_icon_select(power_select, mouse_pos, screen):
    """Lorsqu'un power est sélectionné, l'icône bouge en fonction de la souris"""
    image_power_select = power_select.image_load
    screen.blit(image_power_select, (mouse_pos[0] - 33, mouse_pos[1] - 33))


def if_power_is_send(power_click, list_rectangle_coll_drag, list_dragon, mouse_pos):
    end = False
    """Vérifie si le pouvoir a été laché sur une cible, et applique les effets"""
    dragon_use = power_click[0]
    power_use = power_click[1]
    if power_use.str in power_damage:
        info_verfif_unclick = verif_unclick_in_rect(list_rectangle_coll_drag[1], mouse_pos)
        if info_verfif_unclick[0]:
            if is_dead_interface(list_dragon[1][info_verfif_unclick[1]]):
                print("Votre cible est morte, veuillez réessayer")
            else:
                dragon_use.attack(list_dragon[1], info_verfif_unclick[1])
                dragon_use.dico_power[power_use.str](list_dragon[1], info_verfif_unclick[1])
                end = boucle_jeu(list_dragon[1], list_dragon[0])

    elif power_use.str in power_support:
        info_verfif_unclick = verif_unclick_in_rect(list_rectangle_coll_drag[0], mouse_pos)
        if info_verfif_unclick[0]:
            if is_dead_interface(list_dragon[0][info_verfif_unclick[1]]):
                print("Votre cible est morte, veuillez réessayer")
            else:
                dragon_use.dico_power[power_use.str](list_dragon[0], info_verfif_unclick[1])
                end = boucle_jeu(list_dragon[1], list_dragon[0])
    else:
        info_verfif_unclick = verif_unclick_in_rect(list_rectangle_coll_drag[1], mouse_pos)
        if info_verfif_unclick[0]:
            if is_dead_interface(list_dragon[1][info_verfif_unclick[1]]):
                print("Votre cible est morte, veuillez réessayer")
            else:
                dragon_use.dico_power[power_use.str](list_dragon[1], info_verfif_unclick[1])
                end = boucle_jeu(list_dragon[1], list_dragon[0])
    return end


def verif_unclick_in_rect(liste_rect, mouse_pos):
    for i in range(len(liste_rect)):
        if liste_rect[i].collidepoint(mouse_pos):
            return [True, i]
    return [False, "None"]
