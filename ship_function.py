from configs import *
from button import BUTTON
from ship_function_ii import *


def roll(low, high) -> int:
    return random.randint(low, high)

# MAIN FUNCTION #
def screen_ship(player_spaceship):
    print("LOGS:    now in screen_ship function")
    # TIME #
    time_start = time.time()
    rolling_start = time.time()
    # GAME VARIABLES #
    friendly = False if random.randint(0,2) == 0 else True
    player_decided = False
    title_color = ORANGE
    # SURFACES #
    title_surface = TEXT_MEDIUM.render("SHIP DETECTED", True, title_color)
    # BUTTONS #
    approach_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.7, str="PARLEY")
    ignore_button = BUTTON(width=200, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.8, str="SAIL ON")
    # SCREENS #
    approach_button.enabled = True
    ignore_button.enabled = True

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
        stats_ship_str += f"{player_spaceship.food_string()} NL "
        stats_ship_str += f"{player_spaceship.water_string()} NL "
        stats_ship_str += f"{player_spaceship.rum_string()} NL "
        stats_ship_str += f"AVAILABLE DECKHANDS:  {player_spaceship.get_deckhands()}"
        blit_paragraph(string=stats_ship_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)

        title_surface = TEXT_MEDIUM.render("SHIP DETECTED", True, title_color)

        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.2))

        approach_button.draw(SCREEN)
        ignore_button.draw(SCREEN)

        #blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH*0.25,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)
        if player_decided == True:
            approach_button.enabled = False
            ignore_button.enabled = False

        
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
                approach_button.hovering_color(mouse_pos)
                ignore_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if approach_button.hovering_check(mouse_pos):
                    approach_button.clicked = True
                if ignore_button.hovering_check(mouse_pos):
                    ignore_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if approach_button.hovering_check(mouse_pos) and approach_button.clicked == True and approach_button.enabled:
                    screen_ship_ii(player_spaceship, friendly)
                    running = False
                # NAVIGATION EVENT
                if (ignore_button.hovering_check(mouse_pos) and ignore_button.clicked and ignore_button.enabled):
                    #warp_travel_audio_pack[random.randint(1,4)].play()
                    running = False
                
                approach_button.clicked = False
                ignore_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)