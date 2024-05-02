from configs import *
from button import BUTTON
from spaceship import *


def roll(low, high) -> int:
    return random.randint(low, high)


# MAIN FUNCTION #
def screen_ship_ii(player_spaceship, friendly):
    print("LOGS:    now in screen_ship_ii function")
    # TIME #
    time_start = time.time()
    rolling_start = time.time()
    # GAME VARIABLES #
    player_dmg = "X"
    game_dmg = "X"
    player_roll_choice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    player_flee_roll = "X"
    player_cannon_roll = "X"
    game_cannon_roll = "X"
    player_decided = False
    title_color = ORANGE
    resources = ["FOOD", "WATER", "FUEL"]
    amount = [10, 15, 20]
    instr_str = ""
    instr_str1 = ""
    instr_str2 = ""
    instr_str3 = ""
    note_str = ""
    bribe = 2
    flee = 12
    other_ship = SPACESHIP()
    if random.randint(0,1) == 0:
        other_ship.health = random.randint(35,45)
    else:
        other_ship.health = 50
    other_ship.deckhands = random.randint(2,5)
    other_ship.fuel = random.randint(5,15)
    other_ship.food = random.randint(5,15)
    other_ship.water = random.randint(5,15)
    crewmates_dead = 0
    crewmates_injured = 0
    # SURFACES #
    title_surface = TEXT_MEDIUM.render("SHIP DETECTED", True, title_color)
    # BUTTONS #
    option1_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.6, str="")
    option2_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.7, str="")
    option3_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.8, str="")
    continue_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.9, ypos=SCREEN_HEIGHT*0.9, str="CONTINUE")
    # SCREENS #
    option1_button.enabled = True
    option2_button.enabled = True
    option3_button.enabled = True

    friendly_toggle = False
    hostile_toggle = False

    attacking = False
    if friendly:

        game_resource = random.choice(resources)
        game_amount = random.choice(amount)
        resources.remove(game_resource)
        player_resource = random.choice(resources)
        player_amount = math.ceil(game_amount * 0.6)

        instr_str1 = "TRADE OFFER NL "
        instr_str1 += f"+ {game_amount} {game_resource} NL "
        instr_str1 += f"- {player_amount} {player_resource} NL "
        instr_str2 = ""
        instr_str3 = ""

        friendly_toggle = True
        title_color = GREEN
        title_surface = TEXT_MEDIUM.render("FRIENDLY SHIP DETECTED", True, title_color)
        option1_button.str = "ACCEPT TRADE"
        option2_button.str = "DECLINE TRADE"
        option3_button.str = "ENGAGE"
    else:
        instr_str1 = "ROLL TO FIRE CANNONS NL "
        instr_str1 += f"YOUR ROLL NL [ {player_cannon_roll} ] NL "
        instr_str1 += f"ENEMY ROLL NL [ {game_cannon_roll} ] NL "
            

        instr_str2 = "BRIBE NL "
        #instr_str2 += "ESCAPE NL "
        instr_str2 += f"- {bribe} CARGO NL "

        instr_str3 = "ROLL TO FLEE NL "
        instr_str3 += f"DIFFICULTY [ {flee} ] NL "
        instr_str3 += f"YOUR ROLL NL [ {player_flee_roll} ] NL "
        hostile_toggle = True
        title_color = RED
        title_surface = TEXT_MEDIUM.render("HOSTILE SHIP DETECTED", True, title_color)
        option1_button.str = "ROLL TO FIRE CANNONS"
        option2_button.str = "BRIBE"
        option3_button.str = "ROLL TO FLEE"

    # GAME LOOP #
    running = True
    while running:

        if attacking == True:
            friendly_toggle = False
            hostile_toggle = True
            instr_str1 = "ROLL TO FIRE CANNONS NL "
            instr_str1 += f"YOUR ROLL NL [ {player_cannon_roll} ] NL "
            instr_str1 += f"ENEMY ROLL NL [ {game_cannon_roll} ] NL "
                

            instr_str2 = "BRIBE NL "
            #instr_str2 += "ESCAPE NL "
            instr_str2 += f"- {bribe} CARGO NL "

            instr_str3 = "ROLL TO FLEE NL "
            instr_str3 += f"DIFFICULTY [ {flee} ] NL "
            instr_str3 += f"YOUR ROLL NL [ {player_flee_roll} ] NL "
            hostile_toggle = True
            title_color = RED
            title_surface = TEXT_MEDIUM.render("HOSTILE SHIP DETECTED", True, title_color)
            option1_button.str = "ROLL TO FIRE CANNONS"
            option2_button.str = "BRIBE"
            option3_button.str = "ROLL TO FLEE"
            attacking = False
        # TIME & BACKGROUND #
        time_current = time.time()
        rolling_current = time.time()
        SCREEN.fill(BLACK)
        SCREEN.blit(sun_image, (0,SCREEN_HEIGHT-sun_image.get_height()))


        stats_ship_str = f"{player_spaceship.name} NL "
        stats_ship_str += f"{player_spaceship.health_string()} NL "
        stats_ship_str += f"{player_spaceship.fuel_string()} NL "
        stats_ship_str += f"{player_spaceship.food_string()} NL "
        stats_ship_str += f"{player_spaceship.water_string()} NL "
        stats_ship_str += f"{player_spaceship.rum_string()} NL "
        stats_ship_str += f"AVAILABLE DECKHANDS:  {player_spaceship.get_deckhands()}"
        blit_paragraph(string=stats_ship_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)
        stats_othr_ship_str = "FOREIGN SHIP NL "
        stats_othr_ship_str += f"{other_ship.health_string()} NL "
        stats_othr_ship_str += f"{other_ship.fuel_string()} NL "
        stats_othr_ship_str += f"{other_ship.food_string()} NL "
        stats_othr_ship_str += f"{other_ship.water_string()} NL "
        stats_othr_ship_str += f"AVAILABLE DECKHANDS:  {other_ship.deckhands}"
        blit_paragraph(string=stats_othr_ship_str,xpos=SCREEN_WIDTH*0.7,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)
        


        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.2))
        blit_paragraph(string=note_str,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.75,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        option1_button.draw(SCREEN)
        option2_button.draw(SCREEN)
        option3_button.draw(SCREEN)
        continue_button.draw(SCREEN)

        if friendly_toggle:
            #title_surface = TEXT_MEDIUM.render("FRIENDLY SHIP DETECTED", True, title_color)

            blit_paragraph(string=instr_str1,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            blit_paragraph(string=instr_str2,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            blit_paragraph(string=instr_str3,xpos=SCREEN_WIDTH*0.7,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        elif hostile_toggle:
            #title_surface = TEXT_MEDIUM.render("HOSTILE SHIP DETECTED", True, title_color)

            blit_paragraph(string=instr_str1,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            blit_paragraph(string=instr_str2,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            blit_paragraph(string=instr_str3,xpos=SCREEN_WIDTH*0.7,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.75,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        else:
            print("LOGS:    ERROR; toggle unknown")

        if player_decided == True:
            option1_button.enabled = False
            option2_button.enabled = False
            option3_button.enabled = False
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
                option1_button.hovering_color(mouse_pos)
                option2_button.hovering_color(mouse_pos)
                option3_button.hovering_color(mouse_pos)
                continue_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_button.hovering_check(mouse_pos):
                    option1_button.clicked = True
                if option2_button.hovering_check(mouse_pos):
                    option2_button.clicked = True
                if option3_button.hovering_check(mouse_pos):
                    option3_button.clicked = True
                if continue_button.hovering_check(mouse_pos):
                    continue_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if (continue_button.hovering_check(mouse_pos) and continue_button.clicked == True and continue_button.enabled) and player_decided:
                    running = False
                # ACCEPT TRADE
                if (option1_button.hovering_check(mouse_pos) and option1_button.clicked == True and option1_button.enabled) and friendly_toggle:
                    if player_resource == "FOOD":
                        if game_resource == "WATER":
                            if player_spaceship.food >= player_amount:
                                player_spaceship.food -= player_amount
                                player_spaceship.water += game_amount
                                if player_spaceship.water > player_spaceship.max_water:
                                    player_spaceship.water = player_spaceship.max_water
                                    instr_str1 = "TRADE OFFER NL "
                                    instr_str1 += f"&GREEN +{game_amount} {game_resource} NL "
                                    instr_str1 += f"&RED -{player_amount} {player_resource} NL "
                                player_decided = True
                            else:
                                note_str = "YOU DO NOT HAVE ENOUGH FOOD TO TRADE."
                        elif game_resource == "FUEL":
                            if player_spaceship.food >= player_amount:
                                player_spaceship.food -= player_amount
                                player_spaceship.fuel += game_amount
                                if player_spaceship.fuel > player_spaceship.max_fuel:
                                    player_spaceship.fuel = player_spaceship.max_fuel
                                    instr_str1 = "TRADE OFFER NL "
                                    instr_str1 += f"&GREEN +{game_amount} {game_resource} NL "
                                    instr_str1 += f"&RED -{player_amount} {player_resource} NL "
                                player_decided = True
                            else:
                                note_str = "YOU DO NOT HAVE ENOUGH FOOD TO TRADE."
                        else:
                            pass
                    elif player_resource == "WATER":
                        if game_resource == "FOOD":
                            if player_spaceship.water >= player_amount:
                                player_spaceship.water -= player_amount
                                player_spaceship.food += game_amount
                                if player_spaceship.food > player_spaceship.max_food:
                                    player_spaceship.food = player_spaceship.max_food
                                    instr_str1 = "TRADE OFFER NL "
                                    instr_str1 += f"&GREEN +{game_amount} {game_resource} NL "
                                    instr_str1 += f"&RED -{player_amount} {player_resource} NL "
                                player_decided = True
                            else:
                                note_str = "YOU DO NOT HAVE ENOUGH WATER TO TRADE."
                        elif game_resource == "FUEL":
                            if player_spaceship.water >= player_amount:
                                player_spaceship.water -= player_amount
                                player_spaceship.fuel += game_amount
                                if player_spaceship.fuel > player_spaceship.max_fuel:
                                    player_spaceship.fuel = player_spaceship.max_fuel
                                    instr_str1 = "TRADE OFFER NL "
                                    instr_str1 += f"&GREEN +{game_amount} {game_resource} NL "
                                    instr_str1 += f"&RED -{player_amount} {player_resource} NL "
                                player_decided = True
                            else:
                                note_str = "YOU DO NOT HAVE ENOUGH WATER TO TRADE."
                        else:
                            pass
                    elif player_resource == "FUEL":
                        if game_resource == "FOOD":
                            if player_spaceship.fuel >= player_amount:
                                player_spaceship.fuel -= player_amount
                                player_spaceship.food += game_amount
                                if player_spaceship.food > player_spaceship.max_food:
                                    player_spaceship.food = player_spaceship.max_food
                                    instr_str1 = "TRADE OFFER NL "
                                    instr_str1 += f"&GREEN +{game_amount} {game_resource} NL "
                                    instr_str1 += f"&RED -{player_amount} {player_resource} NL "
                                player_decided = True
                            else:
                                note_str = "YOU DO NOT HAVE ENOUGH FUEL TO TRADE."
                        elif game_resource == "WATER":
                            if player_spaceship.fuel >= player_amount:
                                player_spaceship.fuel -= player_amount
                                player_spaceship.water += game_amount
                                if player_spaceship.water > player_spaceship.max_water:
                                    player_spaceship.water = player_spaceship.max_water
                                    instr_str1 = "TRADE OFFER NL "
                                    instr_str1 += f"&GREEN +{game_amount} {game_resource} NL "
                                    instr_str1 += f"&RED -{player_amount} {player_resource} NL "
                                player_decided = True
                            else:
                                note_str = "YOU DO NOT HAVE ENOUGH FUEL TO TRADE."
                        else:
                            pass
                    else:
                        pass
                # DECLINE TRADE
                if (option2_button.hovering_check(mouse_pos) and option2_button.clicked == True and option2_button.enabled) and friendly_toggle:
                    player_decided = True
                # ENGAGE
                if (option3_button.hovering_check(mouse_pos) and option3_button.clicked == True and option3_button.enabled) and friendly_toggle:
                    note_str = ""
                    attacking = True

                # FIRE CANNONS
                if (option1_button.hovering_check(mouse_pos) and option1_button.clicked == True and option1_button.enabled) and hostile_toggle:
                    roll_audio = diceroll_audio_pack[random.randint(1,3)]
                    roll_audio.play()
                    pygame.time.wait(int(roll_audio.get_length() * 1000))
                    for _ in range(3):
                        laser_audio_pack[random.randint(1,3)].play()
                        pygame.time.wait(int(random.randint(1,3) * 100))
                    player_cannon_roll = (random.randint(0,player_spaceship.get_deckhands()))
                    player_dmg = player_cannon_roll * 4
                    game_cannon_roll = (random.randint(0,other_ship.deckhands))
                    game_dmg = game_cannon_roll * 4

                    instr_str1 = "ROLL TO FIRE CANNONS NL "
                    #instr_str1 += f"YOUR ROLL NL [ {player_cannon_roll} ] NL "
                    instr_str1 += f"YOUR ROLL NL [ { player_cannon_roll } ] NL { player_cannon_roll } x 4 NL [ { player_cannon_roll * 4 } ] NL "
                    instr_str1 += f"ENEMY ROLL NL [ { game_cannon_roll } ] NL { game_cannon_roll } x 4 NL [ { game_cannon_roll * 4 } ] NL "
                    #instr_str1 += f"ENEMY ROLL NL [ {game_cannon_roll} ] NL "

                    other_ship.health -= player_dmg
                    if other_ship.health <= 0:
                        explosion_audio_pack[random.randint(1,3)].play()
                        title_color = GREEN
                        title_surface = TEXT_MEDIUM.render("HOSTILE SHIP DESTROYED", True, title_color)
                        #instr_str1 = ""
                        instr_str2 = ""
                        instr_str3 = ""
                        instr_str = "&GREEN ENEMY VESSEL DESTROYED NL "
                        instr_str += "SUPPLIES SALVAGED NL "
                        instr_str += f"&GREEN + {other_ship.fuel} FUEL NL " if other_ship.fuel > 0 else f"&WHITE + {other_ship.fuel} FUEL NL "
                        instr_str += f"&GREEN + {other_ship.food} FOOD NL " if other_ship.food > 0 else f"&WHITE + {other_ship.food} FOOD NL "
                        instr_str += f"&GREEN + {other_ship.water} WATER NL " if other_ship.water > 0 else f"&WHITE + {other_ship.water} WATER NL "
                        player_spaceship.fuel += other_ship.fuel
                        if player_spaceship.fuel > player_spaceship.max_fuel:
                            player_spaceship.fuel = player_spaceship.max_fuel
                        player_spaceship.food += other_ship.food
                        if player_spaceship.food > player_spaceship.max_food:
                            player_spaceship.food = player_spaceship.max_food
                        player_spaceship.water += other_ship.water
                        if player_spaceship.water > player_spaceship.max_water:
                            player_spaceship.water = player_spaceship.max_water
                        other_ship.fuel = 0
                        other_ship.food = 0
                        other_ship.water = 0
                        player_decided = True
                    else:
                        if bribe == 2:
                            bribe = 4
                        if flee == 12:
                            flee = 16
                        instr_str2 = "BRIBE NL "
                        instr_str2 += f"- {bribe} CARGO NL "

                        instr_str3 = "ROLL TO FLEE NL "
                        instr_str3 += f"DIFFICULTY [ {flee} ] NL "
                        instr_str3 += f"YOUR ROLL NL [ {player_flee_roll} ] NL "
                        player_spaceship.health -= game_dmg
                        if player_spaceship.health <= 0:
                            explosion_audio_pack[random.randint(1,3)].play()
                            title_color = RED
                            title_surface = TEXT_MEDIUM.render("SHIP DESTROYED", True, title_color)
                            yarrr_sound.play()
                            instr_str = "&RED YER *$#%@ VESSEL BE DESTROYED NL "
                            #instr_str1 = ""
                            instr_str2 = ""
                            instr_str3 = ""
                            player_decided = True
                        else:
                            instr_str = "DAMAGE DEALT NL "
                            instr_str += f"&GREEN {player_dmg} NL "
                            instr_str += "DAMAGE RECEIVED NL "
                            instr_str += f"&RED {game_dmg} NL "
                    if player_decided == False:
                        if game_dmg > 0:
                            for crewmate in player_spaceship.crewmates_alive:
                                # CHANCE FOR INJURY = 10%
                                if random.choice([0,1,2,3,4,5,6,7,8,9]) == 0:
                                    # CREWMATE DMG = 10 - 25% of max health
                                    crewmate_damage = math.ceil(random.randint(int(crewmate.max_health / 10), int(crewmate.max_health / 4)))
                                    crewmate.health -= crewmate_damage
                                    if crewmate.health <= 0:
                                        crewmates_dead += 1
                                    else:
                                        crewmates_injured += 1
                        instr_str += f"&RED {crewmates_dead} DEAD NL "
                        instr_str += f"&ORANGE {crewmates_injured} INJURED NL "
                

                # BRIBE
                if (option2_button.hovering_check(mouse_pos) and option2_button.clicked == True and option2_button.enabled) and hostile_toggle:
                    if player_spaceship.rum_crates >= bribe:
                        title_color = ORANGE
                        title_surface = TEXT_MEDIUM.render("BRIBE ACCEPTED", True, title_color)
                        player_decided = True
                        player_spaceship.rum_crates -= bribe
                        instr_str2 = "BRIBE NL "
                        #nstr_str2 += "&GREEN ESCAPE NL "
                        instr_str2 += f"&RED - {bribe} CARGO NL "

                        instr_str1 = ""
                        instr_str3 = ""
                        inst_str = ""
                    else:
                        warp_fail_audio.play()
                        instr_str = "YE CAN'T AFFORD TO BRIBE 'EM! NL"
                        instr_str += "BEST GET TO FLEEIN' 'O FIRIN'! NL "
                # FLEE
                if (option3_button.hovering_check(mouse_pos) and option3_button.clicked == True and option3_button.enabled) and hostile_toggle:
                    roll_audio = diceroll_audio_pack[random.randint(1,3)]
                    roll_audio.play()
                    pygame.time.wait(int(roll_audio.get_length() * 1000))
                    warp_escape_audio.play()
                    player_flee_roll = random.choice(player_roll_choice)
                    if (player_flee_roll + (2 * player_spaceship.get_helmsmen())) > flee:
                        yarrr_sound.play()
                        instr_str3 = "ROLL TO FLEE NL "
                        instr_str3 += f"DIFFICULTY [ {flee} ] NL "
                        instr_str3 += f"YOUR ROLL NL [ { player_flee_roll } ] NL { player_flee_roll } + (2 x { player_spaceship.get_helmsmen() }) NL [ { (player_flee_roll + (2 * player_spaceship.get_helmsmen())) } ] NL "
                        instr_str = "&GREEN PASSED NL "
                        instr_str1 = ""
                        instr_str2 = ""
                        title_color = GREEN
                        title_surface = TEXT_MEDIUM.render("FLEEING ENEMY SHIP", True, title_color)
                        player_decided = True
                    else:
                        warp_fail_audio.play()
                        instr_str3 = "ROLL TO FLEE NL "
                        instr_str3 += f"DIFFICULTY [ {flee} ] NL "
                        instr_str3 += f"YOUR ROLL NL [ { player_flee_roll } ] NL { player_flee_roll } + (2 x { player_spaceship.get_helmsmen() }) NL [ { (player_flee_roll + (2 * player_spaceship.get_helmsmen())) } ] NL "
                        instr_str = "&RED FAILED NL "
                        game_cannon_roll = (random.randint(0,other_ship.deckhands))
                        game_dmg = game_cannon_roll * 4
                        player_spaceship.health -= game_dmg
                        if player_spaceship.health <= 0:
                            explosion_audio_pack[random.randint(1,3)].play()
                            title_color = RED
                            title_surface = TEXT_MEDIUM.render("SHIP DESTROYED", True, title_color)
                            yarrr_sound.play()
                            instr_str = "&RED YER *$#%@ VESSEL BE DESTROYED NL "
                            #instr_str1 = ""
                            instr_str2 = ""
                            instr_str3 = ""
                            player_decided = True
                        else:
                            instr_str += "DAMAGE RECEIVED NL "
                            instr_str += f"&RED {game_dmg} NL "

                option1_button.clicked = False
                option2_button.clicked = False
                option3_button.clicked = False
                continue_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)