from configs import *
from new_game_function import *
from game_function import *
from spaceship import SPACESHIP
from button import BUTTON

# GAME VARIABLES #
global player_spaceship
player_spaceship = SPACESHIP()

# MAIN FUNCTION #
def screen_main():
    print("LOGS:    now in screen_main function")
    # TIME #
    time_start = time.time()
    # GAME VARIABLES #
    global player_spaceship
    background_str = "Ahoy, ye've just been enlisted as a skipper under the flag of Artisan Rum & Gold Handling, or ARGH, to ye and me. "
    background_str += "Yer duty be to steer a hearty crew 'cross the celestial seas, ferryin' cargo on behalf o' ARGH. "
    background_str += "The company'll be grantin' ye a vessel and capital to invest in a handful o' mates and supplies fer yer journey. 'Tis on yer shoulders to round up yer sea dogs and plan the trip. NL "
    background_str += "ARGH finds itself in stormy waters, havin' parted ways with a goodly number o' captains, amid a squall o' scorn from the landlubbers, followin' the disappearance of previous crews into the void, blamed on 'leaky vessels' and 'grueling voyages' and such drivel... Poppycock, I say! "
    background_str += "Yer mission, should ye choose to accept, be to chart a course for ARGH back to glory and to win back the favor o' the masses with a voyage marked by success. "
    background_str += "Fair winds and following seas to ye, matey. Good fortune be yours."
    instr_str = "How to Win or Lose: NL "
    instr_str += "Ye must make port at yer destination to claim victory. NL Should yer vessel be sent to Davy Jones' locker or yer whole crew be taken by the sea, ye be defeated. NL "
    instr_str += "Ye'll have the chance to pressgang various sorts of sea dogs, each with their own duties, to aid in yer voyage. NL Yer ship will also be stocked with provisions of grub, fresh water, fuel, and the breath of life itself. NL "
    instr_str += "Ye'll be granted a sum of gold doubloons to conscript diverse mates. NL How ye choose to invest yer treasure be entirely in yer hands, matey. NL "
    instr_str += "Crewmate Responsibilities: NL "
    instr_str += "Helmsmen are tasked with manuevering the vessel to stay on schedule and avoid danger. NL "
    instr_str += "Carpenters are tasked with repairing the ship, the oxygen generator, and the fuel tank in the event of damages or leaks. NL "
    instr_str += "Surgeons are tasked with healing injured crewmates. NL "
    instr_str += "Scientists are tasked with analyzing passing planets and ships for danger or resources. NL "
    instr_str += "Buccaneers are tasked with protecting the crew on planetary expeditions. NL "
    instr_str += "Deckhands are tasked with resource acquisition on planetary expeditions and cannon-firin' in firefights. NL "
    # SURFACES #
    title_surface = TEXT_LARGE.render("COSMIC VOYAGER", True, WHITE)
    exit_surface = TEXT_XSMALL.render("PRESS 'ESC' ANYTIME TO EXIT GAME", True, WHITE)
    # BUTTONS #
    new_game_button = BUTTON(width=150, height=50, xpos=SCREEN_WIDTH*0.5-150/2, ypos=SCREEN_HEIGHT*0.9, str="START NEW GAME")
    instructions_button = BUTTON(width=150, height=50, xpos=SCREEN_WIDTH*0.5-150/2, ypos=SCREEN_HEIGHT*0.2, str="HOW TO PLAY")
    # SCREENS #
    main_menu_toggle = True
    instructions_toggle = False
    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        SCREEN.fill(BLACK)

        if main_menu_toggle:
            SCREEN.blit(title_surface, (SCREEN_WIDTH/2 - title_surface.get_width()/2, SCREEN_HEIGHT*0.05))
            SCREEN.blit(exit_surface, (SCREEN_WIDTH/2 - exit_surface.get_width()/2, SCREEN_HEIGHT*0.1))
            blit_paragraph(string=background_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="SMALL",SCREEN=SCREEN)
            instructions_button.str = "HOW TO PLAY"
            new_game_button.enabled = True
            instructions_button.enabled = True
            new_game_button.draw(SCREEN)
            instructions_button.draw(SCREEN)
        elif instructions_toggle:
            SCREEN.blit(title_surface, (SCREEN_WIDTH/2 - title_surface.get_width()/2, SCREEN_HEIGHT*0.05))
            SCREEN.blit(exit_surface, (SCREEN_WIDTH/2 - exit_surface.get_width()/2, SCREEN_HEIGHT*0.1))
            blit_paragraph(string=instr_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.3,line_length=150,text_size="SMALL",SCREEN=SCREEN)
            instructions_button.str = "GO BACK"
            instructions_button.draw(SCREEN)
        else:
            pass
        
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
                new_game_button.hovering_color(mouse_pos)
                instructions_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.hovering_check(mouse_pos):
                    new_game_button.clicked = True
                if instructions_button.hovering_check(mouse_pos):
                    instructions_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if new_game_button.hovering_check(mouse_pos) and new_game_button.clicked and new_game_button.enabled:
                    running = False
                    play_again = screen_new_game(player_spaceship)
                    if play_again:
                        player_spaceship = SPACESHIP()
                        screen_main()
                if instructions_button.hovering_check(mouse_pos) and instructions_button.clicked and instructions_button.enabled:
                    if main_menu_toggle:
                        main_menu_toggle = False
                        instructions_toggle = True
                    else:
                        main_menu_toggle = True
                        instructions_toggle = False
                new_game_button.clicked = False
                instructions_button.clicked = False
                    
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)

# RUN MAIN GAME LOOP #
print("LOGS:    running program")
screen_main()