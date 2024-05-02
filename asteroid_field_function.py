from configs import *
from button import BUTTON


def roll(low, high) -> int:
    return random.randint(low, high)

# MAIN FUNCTION #
def screen_asteroids(player_spaceship):
    print("LOGS:    now in screen_asteroids function")
    alarm_audio.play()
    # TIME #
    time_start = time.time()
    rolling_start = time.time()
    # GAME VARIABLES #
    player_roll_choice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    game_roll_choice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    player_roll = -1
    game_roll = -1
    instr_str = ""
    player_decided = False
    title_color = ORANGE
    # SURFACES #
    title_surface = TEXT_MEDIUM.render("ASTEROID FIELD DETECTED", True, title_color)
    # BUTTONS #
    roll_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.7, str="ROLL TO NAVIGATE")
    no_roll_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.8, str="SAIL AROUND")
    continue_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.9, ypos=SCREEN_HEIGHT*0.9, str="CONTINUE")
    # SCREENS #
    player_str = "YOUR ROLL NL [ X ]"
    game_str = "ASTEROID FIELD DIFFICULTY NL [ X ]"
    roll_button.str = "ROLL TO NAVIGATE"
    no_roll_button.str = "SAIL AROUND"
    roll_button.enabled = True
    no_roll_button.enabled = True

    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        rolling_current = time.time()
        SCREEN.fill(BLACK)
        SCREEN.blit(sun_image, (0,SCREEN_HEIGHT-sun_image.get_height()))

        stats_ship_str = f"{player_spaceship.name} NL "
        stats_ship_str += f"{player_spaceship.health_string()} NL "
        stats_ship_str += f"{player_spaceship.fuel_string()} NL "
        stats_ship_str += f"AVAILABLE HELMSMEN:  {player_spaceship.get_helmsmen()} NL "
        blit_paragraph(string=stats_ship_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)

        title_surface = TEXT_MEDIUM.render("ASTEROID FIELD DETECTED", True, title_color)

        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.2))
        continue_button.draw(SCREEN)

        roll_button.draw(SCREEN)
        no_roll_button.draw(SCREEN)

        blit_paragraph(string=game_str,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        blit_paragraph(string=player_str,xpos=SCREEN_WIDTH*0.7,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        if abs(time_start - time_current) < 3:
            if abs(rolling_start - rolling_current) < 0.1:
                game_roll = random.choice(game_roll_choice)
                game_str = f"ASTEROID FIELD DIFFICULTY NL [ { game_roll } ]"
                rolling_start = rolling_current
        else:
            if player_decided == False:
                roll_button.enabled = True
                no_roll_button.enabled = True
            else:
                roll_button.enabled = False
                no_roll_button.enabled = False

        
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
                continue_button.hovering_color(mouse_pos)
                roll_button.hovering_color(mouse_pos)
                no_roll_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.hovering_check(mouse_pos):
                    continue_button.clicked = True
                if roll_button.hovering_check(mouse_pos):
                    roll_button.clicked = True
                if no_roll_button.hovering_check(mouse_pos):
                    no_roll_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if continue_button.hovering_check(mouse_pos) and continue_button.clicked == True and continue_button.enabled:
                    running = False
                # ASTEROID EVENT
                if (roll_button.hovering_check(mouse_pos) and roll_button.clicked and roll_button.enabled):
                    # ROLL TO NAVIGATE
                    roll_audio = diceroll_audio_pack[random.randint(1,3)]
                    roll_audio.play()
                    pygame.time.wait(int(roll_audio.get_length() * 1000))
                    player_decided = True
                    roll_button.enabled = False
                    no_roll_button.enabled = False
                    player_roll = random.choice(player_roll_choice)
                    helmsmen = player_spaceship.get_helmsmen()
                    player_str = f"YOUR ROLL NL [ { player_roll } ] NL { player_roll } + (2 x { helmsmen }) NL [ { (player_roll + (2 * helmsmen)) } ] NL "
                    if (player_roll + (2 * helmsmen)) >= game_roll:
                        #warp_travel_audio_pack[random.randint(1,4)].play()
                        title_color = GREEN
                        instr_str = "&GREEN PASSED NL "
                        instr_str += "&GREEN 0% DAMAGE TO SHIP NL "
                        instr_str += "&GREEN 0 DEAD NL "
                        instr_str += "&GREEN 0 INJURED NL "
                    else:
                        title_color = RED
                        crewmates_injured = 0
                        crewmates_dead = 0
                        ship_damage = 0
                        # SHIP DMG = 10 - 20% of max health
                        ship_damage = random.randint(int(player_spaceship.max_health / 10),int(player_spaceship.max_health / 5))
                        print("original dmg: "+str(ship_damage))
                        multiplier = 1
                        if (game_roll - (player_roll + (2 * helmsmen))) > 5:
                            multiplier = 1.5
                        else:
                            multiplier = (1 + ((game_roll - (player_roll + (2 * helmsmen))) * 0.1))
                        ship_damage = math.ceil(ship_damage * multiplier)
                        print("mult dmg: "+str(ship_damage)+"   mult: "+str((game_roll - (player_roll + (2 * helmsmen)))))
                        for crewmate in player_spaceship.crewmates_alive:
                            # CHANCE FOR INJURY = 25%
                            if random.choice([0,1,2,3]) == 0:
                                # CREWMATE DMG = 25 - 50% of max health * multiplier
                                crewmate_damage = math.ceil((random.randint(int(crewmate.max_health / 4), int(crewmate.max_health / 2))) * (1 + ((game_roll - (player_roll + (2 * helmsmen))) * 0.1)))
                                crewmate.health -= crewmate_damage
                                if crewmate.health <= 0:
                                    crewmates_dead += 1
                                else:
                                    crewmates_injured += 1
                        player_spaceship.health -= ship_damage
                        if player_spaceship.health <= 0:
                            explosion_audio_pack[random.randint(1,3)].play()
                            player_spaceship.game_over = True
                            instr_str += "&RED FAILED NL "
                            instr_str += "&RED YER SHIP %*$#@! EXPLODED NL "
                            instr_str += f"&RED { len(player_spaceship.crewmates_alive) } DEAD NL "
                            instr_str += "&ORANGE 0 INJURED NL "
                        else:
                            crash_audio_pack[random.randint(1,2)].play()
                            instr_str += "&RED FAILED NL "
                            instr_str += f"&ORANGE { int(ship_damage/player_spaceship.max_health*100) }% DAMAGE TO SHIP NL "
                            instr_str += f"&RED { crewmates_dead } DEAD NL "
                            instr_str += f"&ORANGE { crewmates_injured } INJURED NL "
                    continue_button.enabled = True

                if (no_roll_button.hovering_check(mouse_pos) and no_roll_button.clicked and no_roll_button.enabled):
                    # SAIL AROUND
                    warp_fail_audio.play()
                    player_decided = True
                    roll_button.enabled = False
                    no_roll_button.enabled = False
                    player_spaceship.days_left += 1
                    player_spaceship.fuel -= 1
                    instr_str = "&RED - 1 FUEL NL "
                    instr_str += "&RED + 1 DAYS LEFT NL "
                    continue_button.enabled = True
                
                continue_button.clicked = False
                roll_button.clicked = False
                no_roll_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)