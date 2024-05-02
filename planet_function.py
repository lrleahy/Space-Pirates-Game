from configs import *
from button import BUTTON


def expedition(player_spaceship, planet):

    results = {
        'dead' : 0,
        'injured' : 0,
        'food' : 0,
        'water' : 0
    }
    deckhands = 0
    buccaneers = 0
    threat1 = [4,5,6]
    threat2 = [8,9,10]
    threat3 = [12,13,14]
    threat4 = [16,17,18]
    threat5 = [20,21,22]

    if planet['threat'] == 1:
        dmg = threat1
    elif planet['threat'] == 2:
        dmg = threat2
    elif planet['threat'] == 3:
        dmg = threat3
    elif planet['threat'] == 4:
        dmg = threat4
    elif planet['threat'] == 5:
        dmg = threat5
    else:
        dmg = [0]

    for crewmate in player_spaceship.crewmates_alive:
        if crewmate.expedition == True and crewmate.busy == False:
            if crewmate.job == "DECKHAND":
                deckhands += 1
            else:
                buccaneers += 1

    if planet['atmosphere'] == "UNINHABITABLE":
        for crewmate in player_spaceship.crewmates_alive:
            if crewmate.expedition == True and crewmate.busy == False:
                crewmate.health = 0
                results['dead'] += 1
        return results

    for crewmate in player_spaceship.crewmates_alive:
        if crewmate.expedition == True and crewmate.busy == False:
            start_health = crewmate.health
            if crewmate.job == "DECKHAND":
                crewmate.health -= (random.choice(dmg) - (2 * buccaneers)) if (random.choice(dmg) - (5 * buccaneers)) > 0 else 0
                if crewmate.health > 0:
                    results['food'] += planet['food']
                    results['water'] += planet['water']
            if crewmate.job == "BUCCANEER":
                crewmate.health -= (random.choice(dmg) - (2 * (buccaneers - 1))) if (random.choice(dmg) - (3 * (buccaneers))) > 0 else 0
            if crewmate.health <= 0:
                results['dead'] += 1
            else:
                if crewmate.health < start_health:
                    results['injured'] += 1

    return results

# MAIN FUNCTION #
def screen_planet(player_spaceship):
    print("LOGS:    now in screen_planet function")
    # TIME #
    time_start = time.time()
    rolling_start = time.time()
    # GAME VARIABLES #
    title_color = ORANGE
    planet = {
        'atmosphere' : 'UNINHABITABLE' if random.randint(0,2) == 0 else 'HABITABLE',
        'threat' : random.randint(0,5),
        'food' : random.randint(0,5),
        'water' : random.randint(0,5),
    }

    planet_str = "PLANET ANALYSIS NL "
    planet_str += "--------------- NL "
    planet_str += "ATMOSPHERE NL "
    planet_str += (f"&GREEN {planet['atmosphere']} NL " if planet['atmosphere'] == 'HABITABLE' else f"&RED {planet['atmosphere']} NL ") if player_spaceship.get_scientists() >= 1 else "&ORANGE UNAVAILABLE NL "
    planet_str += "SURFACE THREAT LEVEL NL "
    if player_spaceship.get_scientists() < 1:
        planet_str += "&ORANGE UNAVAILABLE NL "
    else:
        if planet['threat'] == 0 or  planet['threat'] == 1:
            planet_str += f"&GREEN {planet['threat']} / 5 NL "
        elif planet['threat'] == 2 or  planet['threat'] == 3:
            planet_str += f"&YELLOW {planet['threat']} / 5 NL "
        else:
            planet_str += f"&RED {planet['threat']} / 5 NL "
    planet_str += "FOOD RESOURCE NL "
    planet_str += (f"&GREEN YES NL " if planet['food'] > 0 else f"&RED NO NL ") if player_spaceship.get_scientists() >= 2 else "&ORANGE UNAVAILABLE NL "
    planet_str += "WATER RESOURCE NL "
    planet_str += (f"&GREEN YES NL " if planet['water'] > 0 else f"&RED NO NL ") if player_spaceship.get_scientists() >= 2 else "&ORANGE UNAVAILABLE NL "
    planet_str += "--------------- NL "

    instr_str = "ANALYSIS CHART NL "
    instr_str += "--------------- NL "
    instr_str += "&GREEN HABITABLE: PLANET SUPPORTS HUMAN LIFE NL "
    instr_str += "&RED UNINHABITABLE: PLANET DOES NOT SUPPORT HUMAN LIFE NL "
    instr_str += "SURFACE THREAT LEVEL: DEGREE OF POTENTIAL DANGER NL "
    instr_str += "&GREEN LEVEL 0: NOT DANGEROUS NL "
    instr_str += "&GREEN LEVEL 1: BARELY DANGEROUS NL "
    instr_str += "&YELLOW LEVEL 2: DANGEROUS NL "
    instr_str += "&YELLOW LEVEL 3: VERY DANGEROUS NL "
    instr_str += "&RED LEVEL 4: EXTREMELY DANGEROUS NL "
    instr_str += "&RED LEVEL 5: INSANELY DANGEROUS NL "
    instr_str += "--------------- NL "


    if player_spaceship.get_scientists() == 1:
        planet_str += "&ORANGE RESOURCE DETECTION UNAVAILABLE, 1+ MORE SCIENTIST(S) NEEDED NL "
    if player_spaceship.get_scientists() == 0:
        planet_str += "&RED ANALYSIS UNAVAILABLE, NO SCIENTIST(S) AVAILABLE NL "
    # SURFACES #
    title_surface = TEXT_MEDIUM.render("PLANET DETECTED", True, title_color)
    # BUTTONS #
    expedition_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.7, str="SEND EXPEDITION")
    sail_on_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.8, str="SAIL ON")
    continue_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.9, ypos=SCREEN_HEIGHT*0.9, str="CONTINUE")
    # SCREENS #
    sail_on_button.enabled = True
    expedition_toggle = False

    expedition_str = "EXPEDITION TEAM NL "
    expedition_str += "--------------- NL "
    expedition_button.enabled = False
    for crewmate in player_spaceship.crewmates_alive:
        if crewmate.expedition == True and crewmate.busy == False:
            expedition_button.enabled = True
            if crewmate.distressed:
                expedition_str += f"&RED {crewmate.job} {crewmate.name} NL "
            else:
                expedition_str += f"&GREEN {crewmate.job} {crewmate.name} NL "
    expedition_str += "--------------- NL "
    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        rolling_current = time.time()
        SCREEN.fill(BLACK)
        SCREEN.blit(sun_image, (0,SCREEN_HEIGHT-sun_image.get_height()))

        stats_ship_str = f"{player_spaceship.name} NL "
        stats_ship_str += f"{player_spaceship.food_string()} NL "
        stats_ship_str += f"{player_spaceship.water_string()} NL "
        stats_ship_str += f"AVAILABLE BUCCANEERS:  {player_spaceship.get_buccaneers()} NL "
        stats_ship_str += f"AVAILABLE DECKHANDS:  {player_spaceship.get_deckhands()} NL "
        blit_paragraph(string=stats_ship_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)

        title_surface = TEXT_MEDIUM.render("PLANET DETECTED", True, title_color)

        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.2))
        blit_paragraph(string=expedition_str,xpos=SCREEN_WIDTH*0.25,ypos=SCREEN_HEIGHT*0.25,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        blit_paragraph(string=planet_str,xpos=SCREEN_WIDTH*0.75,ypos=SCREEN_HEIGHT*0.25,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.6,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)

        expedition_button.draw(SCREEN)
        sail_on_button.draw(SCREEN)

        if expedition_toggle == False:
            pass
        else:
            continue_button.draw(SCREEN)
            expedition_button.enabled = False
            sail_on_button.enabled = False
            continue_button.enabled = True

        
        # EVENTS #
        for event in pygame.event.get():

            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # KEY EVENTS #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("LOGS:    esc pressed")
                    running = False
                    pygame.quit()
                    sys.exit()
            # MOUSE EVENTS #
            if event.type == pygame.MOUSEMOTION:
                expedition_button.hovering_color(mouse_pos)
                sail_on_button.hovering_color(mouse_pos)
                continue_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if expedition_button.hovering_check(mouse_pos):
                    expedition_button.clicked = True
                if sail_on_button.hovering_check(mouse_pos):
                    sail_on_button.clicked = True
                if continue_button.hovering_check(mouse_pos):
                    continue_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if continue_button.hovering_check(mouse_pos) and continue_button.clicked == True and continue_button.enabled:
                    running = False
                if expedition_button.hovering_check(mouse_pos) and expedition_button.clicked == True and expedition_button.enabled:
                    results = expedition(player_spaceship, planet)
                    expedition_str = "EXPEDITION RESULTS NL "
                    expedition_str += "--------------- NL "
                    expedition_str += f"&RED {results['dead']} DEAD NL "
                    expedition_str += f"&ORANGE {results['injured']} INJURED NL "
                    expedition_str += f"&GREEN + {results['food']} FOOD NL " if results['food'] > 0 else f"&WHITE + {results['food']} FOOD NL "
                    expedition_str += f"&GREEN + {results['water']} WATER NL " if results['water'] > 0 else f"&WHITE + {results['water']} WATER NL "
                    expedition_str += "--------------- NL "
                    player_spaceship.food += results['food']
                    if player_spaceship.food > player_spaceship.max_food:
                        player_spaceship.food = player_spaceship.max_food
                    player_spaceship.water += results['water']
                    if player_spaceship.water > player_spaceship.max_water:
                        player_spaceship.water = player_spaceship.max_water
                    expedition_toggle = True
                # NAVIGATION EVENT
                if (sail_on_button.hovering_check(mouse_pos) and sail_on_button.clicked and sail_on_button.enabled):
                    #warp_travel_audio_pack[random.randint(1,4)].play()
                    running = False
                
                expedition_button.clicked = False
                sail_on_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)