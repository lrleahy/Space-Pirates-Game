from configs import *
from button import BUTTON


def roll(low, high) -> int:
    return random.randint(low, high)

# MAIN FUNCTION #
def screen_offcourse(player_spaceship):
    print("LOGS:    now in screen_offcourse function")
    power_down_audio.play()
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
    title_surface = TEXT_MEDIUM.render("MAPPING SYSTEM FAILURE", True, title_color)
    # BUTTONS #
    roll_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.8, str="ROLL TO NAVIGATE")
    continue_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.9, ypos=SCREEN_HEIGHT*0.9, str="CONTINUE")
    # SCREENS #
    player_str = "YOUR ROLL NL [ X ]"
    game_str = "MANUAL NAVIGATION DIFFICULTY NL [ X ]"
    roll_button.str = "ROLL TO NAVIGATE"
    roll_button.enabled = True

    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        rolling_current = time.time()
        SCREEN.fill(BLACK)
        SCREEN.blit(sun_image, (0,SCREEN_HEIGHT-sun_image.get_height()))

        stats_ship_str = f"{player_spaceship.name} NL "
        stats_ship_str += f"AVAILABLE HELMSMEN:  {player_spaceship.get_helmsmen()} NL "
        blit_paragraph(string=stats_ship_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)

        title_surface = TEXT_MEDIUM.render("MAPPING SYSTEM FAILURE", True, title_color)

        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.2))
        continue_button.draw(SCREEN)

        roll_button.draw(SCREEN)

        blit_paragraph(string=game_str,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        blit_paragraph(string=player_str,xpos=SCREEN_WIDTH*0.7,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
        if abs(time_start - time_current) < 3:
            if abs(rolling_start - rolling_current) < 0.1:
                game_roll = random.choice(game_roll_choice)
                game_str = f"MANUAL NAVIGATION DIFFICULTY NL [ { game_roll } ]"
                rolling_start = rolling_current
        else:
            if player_decided == True:
                roll_button.enabled = False

        
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.hovering_check(mouse_pos):
                    continue_button.clicked = True
                if roll_button.hovering_check(mouse_pos):
                    roll_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if continue_button.hovering_check(mouse_pos) and continue_button.clicked == True and continue_button.enabled:
                    running = False
                # NAVIGATION EVENT
                if (roll_button.hovering_check(mouse_pos) and roll_button.clicked and roll_button.enabled):
                    # ROLL TO NAVIGATE
                    roll_audio = diceroll_audio_pack[random.randint(1,3)]
                    roll_audio.play()
                    pygame.time.wait(int(roll_audio.get_length() * 1000))
                    player_decided = True
                    roll_button.enabled = False
                    player_roll = random.choice(player_roll_choice)
                    helmsmen = player_spaceship.get_helmsmen()
                    player_str = f"YOUR ROLL NL [ { player_roll } ] NL { player_roll } + (2 x { helmsmen }) NL [ { (player_roll + (2 * helmsmen)) } ] NL "
                    if (player_roll + (2 * helmsmen)) >= game_roll:
                        #warp_travel_audio_pack[random.randint(1,4)].play()
                        title_color = GREEN
                        instr_str = "&GREEN PASSED NL "
                        instr_str += "&GREEN SHIP ON-COURSE NL "
                        instr_str += "&GREEN + 0 DAYS LEFT NL "
                    else:
                        warp_fail_audio.play()
                        title_color = RED
                        days_added = 0
                        if (game_roll - (player_roll + (2 * helmsmen))) < 4:
                            days_added = 1
                        else:
                            days_added = math.floor((game_roll - (player_roll + (2 * helmsmen)))/4)
                        instr_str = "&RED FAILED NL "
                        instr_str += "&RED SHIP OFF-COURSE NL "
                        instr_str += f"&RED + { days_added } DAYS LEFT NL "
                        player_spaceship.days_left += days_added
                    continue_button.enabled = True
                
                continue_button.clicked = False
                roll_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)