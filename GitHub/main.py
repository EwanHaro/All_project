from init_game import *

"""Lancement de l'interface pygame, déjà préparé dans init_screen"""
screen = pygame.display.set_mode((screen_width, screen_height))
fond = pygame.image.load('home_image.jpeg')
fond = pygame.transform.scale(fond, (screen_width, screen_height))
home_page = True
while home_page:
    screen.fill((0, 0, 0))
    screen.blit(fond, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (88, 41, 0), rect_start_button, 15)
    screen.blit(text_start_button, rect_text_start_button)
    screen.blit(text_title_breitfield, (screen_width * 0.18, 0))
    screen.blit(text_title_and_the_quest, (screen_width * 0.2, 200))
    screen.blit(text_title_for_perfection, (screen_width * 0.15, 350))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_start_button.collidepoint(mouse_pos):
                home_page = False
    pygame.display.flip()

fond = pygame.image.load('image_fond_amine_color.png')
fond = pygame.transform.scale(fond, (screen_width, screen_height))
running_pick = False

while running_pick:
    screen.fill((0, 0, 0))
    screen.blit(fond, (0, 0))
    for i in range(len(liste_power)):
        screen.blit(dico_image_effect_power[liste_power[i]], (
            (screen_width // 2) - (len(liste_power) // 2 * taille_icon_power[0]) + (taille_icon_power[0] * i),
            screen_height // 2))
    pygame.display.flip()

"""Récupère les informations si jamais un power est selectionné"""
power_click = ["None", "None"]
user_click_on_power = False

"""Vérification si la partie est fini"""
end = False
frames_since_end_condition_met = 0

running = True
while running:
    # Effacement de l'écran
    screen.fill((0, 0, 0))

    screen.blit(fond, (0, 0))

    surface_text_lap = font_lap.render(f"Au tour de l'équipe {Color_of_lap.get_lap_color()}!", True, (255, 255, 255))
    screen.blit(surface_text_lap, rect_texte_lap)

    print_power(liste_image_power_blue, screen)
    print_power(liste_image_power_red, screen)

    print_statistique(list_dragon_blue, font_blue, screen, 550,
                      (0, 0, 255), taille_icon_power, "left", 0, -1, 0)
    print_statistique(list_dragon_red, font_red, screen, 1170,
                      (255, 0, 0), taille_icon_power, "right", 150, 1, 110)

    mouse_pos = pygame.mouse.get_pos()

    skip_button(rect_skip_buttom, screen, screen_width, screen_height, surface_skip_button, mouse_pos)

    print_sprite(liste_sprite_left, 620, screen, shadow_of_sprite)
    print_sprite(liste_sprite_right, 1200, screen, shadow_of_sprite)

    if user_click_on_power:
        mouvement_power_icon_select(power_click[1], mouse_pos, screen)

    '''Fin du jeu'''
    if end:
        screen.blit(surface_end, text_end_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if Color_of_lap.get_lap_color() == "Blue":
                result_is_power_is_click = if_power_is_click(liste_image_power_blue, mouse_pos)
            else:
                result_is_power_is_click = if_power_is_click(liste_image_power_red, mouse_pos)

            user_click_on_power = result_is_power_is_click[0]
            power_click = [result_is_power_is_click[1], result_is_power_is_click[2]]

            if rect_skip_buttom.collidepoint(mouse_pos):
                if Color_of_lap.get_lap_color() == "Blue":
                    boucle_jeu(list_dragon_red, list_dragon_blue)
                else:
                    boucle_jeu(list_dragon_blue, list_dragon_red)
        elif event.type == pygame.MOUSEBUTTONUP and user_click_on_power:
            if Color_of_lap.get_lap_color() == "Blue":
                end = if_power_is_send(power_click,
                                       [liste_rectangle_coll_drag_bl, liste_rectangle_coll_drag_re],
                                       [list_dragon_blue, list_dragon_red], mouse_pos)
            else:
                end = if_power_is_send(power_click,
                                       [liste_rectangle_coll_drag_re, liste_rectangle_coll_drag_bl],
                                       [list_dragon_red, list_dragon_blue], mouse_pos)
            user_click_on_power = False

    # Mise à jour de l'affichage
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
print("Fermeture de l'interface"
      "Crédit: Haro Ewan(code), Chourfi Amine(Art), Haro Maxime and Thomas Balthazar(Alpha Testeur)"
      "Merci d'avoir joué :)")
