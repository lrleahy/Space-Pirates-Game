from configs import *
from button import BUTTON


def roll(low, high) -> int:
    return random.randint(low, high)

# MAIN FUNCTION #
def screen_win(player_spaceship):
    print("LOGS:    now in screen_win function")
    # TIME #
    time_start = time.time()
    rolling_start = time.time()
    # GAME VARIABLES #
    instr_str = f"DAYS TRAVELED: {player_spaceship.days_traveled} NL CARGO LEFT: {player_spaceship.rum_crates} / 15"

    # SURFACES #
    title_surface = TEXT_LARGE.render("YOU WIN", True, GREEN)
    # BUTTONS #
    play_again_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.9, ypos=SCREEN_HEIGHT*0.9, str="PLAY AGAIN")
    play_again_button.enabled = True
    # SCREENS #

    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        SCREEN.fill(BLACK)

        title_surface = TEXT_LARGE.render("YOU WIN", True, GREEN)

        blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT/2,line_length=100,text_size="SMALL",SCREEN=SCREEN,centered=True)

        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.2))
        play_again_button.draw(SCREEN)


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
                play_again_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.hovering_check(mouse_pos):
                    play_again_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if play_again_button.hovering_check(mouse_pos) and play_again_button.clicked == True and play_again_button.enabled:
                    running = False
                    return True
                
                play_again_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)