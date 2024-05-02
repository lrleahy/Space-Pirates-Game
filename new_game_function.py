from configs import *
from game_function import *
from button import BUTTON

# FUNCTION #
def screen_new_game(player_spaceship):
    print("LOGS:    now in screen_new_game function")
    # TIME #
    time_start = time.time()
    # VARIABLES #

    # SURFACES #
    title_surface = TEXT_LARGE.render("", True, WHITE)
    #gold_surface = TEXT_MEDIUM.render("", True, WHITE)

    # BUTTONS #
    continue_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.9, ypos=SCREEN_HEIGHT*0.9, str="CONTINUE")

    helmsman_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.7, ypos=SCREEN_HEIGHT*0.2, str="HIRE HELMSMAN")
    carpenter_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.7, ypos=SCREEN_HEIGHT*0.3, str="HIRE CARPENTER") 
    surgeon_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.7, ypos=SCREEN_HEIGHT*0.4, str="HIRE SURGEON") 
    scientist_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.7, ypos=SCREEN_HEIGHT*0.5, str="HIRE SCIENTIST") 
    buccaneer_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.7, ypos=SCREEN_HEIGHT*0.6, str="HIRE BUCCANEER") 
    deckhand_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.7, ypos=SCREEN_HEIGHT*0.7, str="HIRE DECKHAND") 
    reset_button = BUTTON(width=100, height=50, xpos=SCREEN_WIDTH*0.6, ypos=SCREEN_HEIGHT*0.2, str="RESET") 

    continue_button.enabled = True
    # SCREENS #
    stage1_toggle = True
    stage2_toggle = False
    stage3_toggle = False
    stage4_toggle = False
    # SCREEN VARIABLES #
    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        SCREEN.fill(BLACK)


        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.05))

        #if stage4_toggle == False:
            #SCREEN.blit(gold_surface, (0, SCREEN_HEIGHT*0.05))

        # TEMPLATE SCREEN #
        if stage1_toggle:
            title_surface = TEXT_LARGE.render("STAGE 1: RECEIVIN' YER VESSEL", True, WHITE)
            stage1_str = f"Arrr, ye ship be christened {player_spaceship.name} by yer generous employer! "
            stage1_str += "She be fitted wit' th' finest o' modern contraptions includin' a breath-o-life generator ye best keep ye eye on. "
            stage1_str += "Ye'll be supplied wit' fuel, grub, an' drink as ye embark on yer voyage. "
            stage1_str += "'Tis yer duty to ensure ye deliver yer cargo to its rightful port wi' th' ship an' crew still standin'. "
            blit_paragraph(string=stage1_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.2,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            continue_button.draw(SCREEN)
        elif stage2_toggle:
            title_surface = TEXT_LARGE.render("STAGE 2: ASSESIN' YER JOURNEY ", True, WHITE)
            stage2_str = "Ye've got a treacherous journey ahead o' ye, two moons long! And mark me words, the supplies ye've got won't keep ye afloat for that stretch. "
            stage2_str += "So, ye'll be needin' to parley with other ships, either through fair trade or a bit o' swashbucklin' if need be. "
            stage2_str += "And if the seas be too stingy, ye may even have to set foot on some distant planets to gather the plunder ye need. "
            stage2_str += "Fer all that plunderin' and explorin' ye'll need a crew matey! That be yer next task. "
            blit_paragraph(string=stage2_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.2,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            continue_button.draw(SCREEN)
        elif stage3_toggle:
            title_surface = TEXT_LARGE.render("STAGE 3: PLANNIN' YER JOURNEY", True, WHITE)
            #gold_surface = TEXT_MEDIUM.render("GOLD REMAINING: "+str(player_spaceship.gold), True, WHITE)
            selection_str = "YER CREW NL "
            selection_str += "HELMSMEN: "+str(player_spaceship.helmsmen)+" NL "
            selection_str += "CARPENTERS: "+str(player_spaceship.carpenters)+" NL "
            selection_str += "SURGEONS: "+str(player_spaceship.surgeons)+" NL "
            selection_str += "SCIENTISTS: "+str(player_spaceship.scientists)+" NL "
            selection_str += "BUCCANEERS: "+str(player_spaceship.buccaneers)+" NL "
            selection_str += "DECKHANDS: "+str(player_spaceship.deckhands)+" NL "
            selection_str += str(15-player_spaceship.max_crewmates)+" /15 MAX NL NL "
            stage3_str = "The company's seen fit to bestow upon ye a chest o' gold to gather a crew worthy o' ye vessel! "
            stage3_str += "And heed me words: spare no expense in findin' the finest swashbucklers to join ye ranks. Every doubloon not spent on the recruitment shall find its way back to the company coffers. "
            stage3_str += "But that be between ye and I... "
            blit_paragraph(string=stage2_str,xpos=SCREEN_WIDTH*0.35,ypos=SCREEN_HEIGHT*0.35,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            blit_paragraph(string=selection_str,xpos=0,ypos=SCREEN_HEIGHT*0.1,line_length=150,text_size="XSMALL",SCREEN=SCREEN,centered=False)
            reset_button.draw(SCREEN)
            continue_button.draw(SCREEN)
            helmsman_button.draw(SCREEN)
            deckhand_button.draw(SCREEN)
            buccaneer_button.draw(SCREEN)
            carpenter_button.draw(SCREEN)
            surgeon_button.draw(SCREEN)
            scientist_button.draw(SCREEN)
        elif stage4_toggle:
            title_surface = TEXT_LARGE.render("STAGE 4: SETTIN' SAIL", True, WHITE)
            stage4_str = "A fine crew! "
            stage4_str += "Goodluck matey! "
            blit_paragraph(string=stage4_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.2,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=True)
            continue_button.draw(SCREEN)
            continue_button.str = "SET SAIL"
        else:
            print("LOGS:    ERROR; toggle unknown")

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
                helmsman_button.hovering_color(mouse_pos)
                deckhand_button.hovering_color(mouse_pos)
                buccaneer_button.hovering_color(mouse_pos)
                carpenter_button.hovering_color(mouse_pos)
                surgeon_button.hovering_color(mouse_pos)
                scientist_button.hovering_color(mouse_pos)
                reset_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.hovering_check(mouse_pos):
                    continue_button.clicked = True
                if helmsman_button.hovering_check(mouse_pos):
                    helmsman_button.clicked = True
                if deckhand_button.hovering_check(mouse_pos):
                    deckhand_button.clicked = True
                if buccaneer_button.hovering_check(mouse_pos):
                    buccaneer_button.clicked = True
                if carpenter_button.hovering_check(mouse_pos):
                    carpenter_button.clicked = True
                if surgeon_button.hovering_check(mouse_pos):
                    surgeon_button.clicked = True
                if scientist_button.hovering_check(mouse_pos):
                    scientist_button.clicked = True
                if reset_button.hovering_check(mouse_pos):
                    reset_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                if reset_button.hovering_check(mouse_pos) and reset_button.clicked and reset_button.enabled:
                    reset_button.enabled = False
                    player_spaceship.max_crewmates = 15
                    player_spaceship.helmsmen = 0
                    player_spaceship.carpenters = 0
                    player_spaceship.surgeons = 0
                    player_spaceship.scientists = 0
                    player_spaceship.buccaneers = 0
                    player_spaceship.deckhands = 0
                    #player_spaceship.gold = player_spaceship.max_gold

                if continue_button.hovering_check(mouse_pos) and continue_button.clicked and continue_button.enabled:
                    if stage1_toggle:
                        stage1_toggle = False
                        stage2_toggle = True
                    elif stage2_toggle:
                        continue_button.enabled = False # disable button until at least 1 crewmate selected
                        helmsman_button.enabled = True
                        deckhand_button.enabled = True
                        buccaneer_button.enabled = True
                        carpenter_button.enabled = True
                        surgeon_button.enabled = True
                        scientist_button.enabled = True
                        stage2_toggle = False
                        stage3_toggle = True
                    elif stage3_toggle:
                        continue_button.enabled = True
                        helmsman_button.enabled = False
                        deckhand_button.enabled = False
                        buccaneer_button.enabled = False
                        carpenter_button.enabled = False
                        surgeon_button.enabled = False
                        scientist_button.enabled = False
                        stage3_toggle = False
                        stage4_toggle = True
                    else:
                        yarrr_sound.play()
                        player_spaceship.generate_crew()
                        for x in range(len(player_spaceship.crewmates_alive)):
                            print(player_spaceship.crewmates_alive[x].name)
                        print(str(player_spaceship.total_alive))
                        running = False
                        return screen_game(player_spaceship)
                if helmsman_button.hovering_check(mouse_pos) and helmsman_button.clicked and helmsman_button.enabled:# and player_spaceship.gold >= 5:
                    clink_audio_pack[random.randint(1,3)].play()
                    player_spaceship.helmsmen += 1
                    player_spaceship.max_crewmates -= 1
                    #player_spaceship.gold -= 5
                if deckhand_button.hovering_check(mouse_pos) and deckhand_button.clicked and deckhand_button.enabled:# and player_spaceship.gold >= 5:
                    clink_audio_pack[random.randint(1,3)].play()
                    player_spaceship.deckhands += 1
                    player_spaceship.max_crewmates -= 1
                    #player_spaceship.gold -= 5
                if buccaneer_button.hovering_check(mouse_pos) and buccaneer_button.clicked and buccaneer_button.enabled:# and player_spaceship.gold >= 5:
                    clink_audio_pack[random.randint(1,3)].play()
                    player_spaceship.buccaneers += 1
                    player_spaceship.max_crewmates -= 1
                    #player_spaceship.gold -= 5
                if carpenter_button.hovering_check(mouse_pos) and carpenter_button.clicked and carpenter_button.enabled:# and player_spaceship.gold >= 5:
                    clink_audio_pack[random.randint(1,3)].play()
                    player_spaceship.carpenters += 1
                    player_spaceship.max_crewmates -= 1
                    #player_spaceship.gold -= 5
                if surgeon_button.hovering_check(mouse_pos) and surgeon_button.clicked and surgeon_button.enabled:# and player_spaceship.gold >= 5:
                    clink_audio_pack[random.randint(1,3)].play()
                    player_spaceship.surgeons += 1
                    player_spaceship.max_crewmates -= 1
                    #player_spaceship.gold -= 5
                if scientist_button.hovering_check(mouse_pos) and scientist_button.clicked and scientist_button.enabled:# and player_spaceship.gold >= 5:
                    clink_audio_pack[random.randint(1,3)].play()
                    player_spaceship.scientists += 1
                    player_spaceship.max_crewmates -= 1
                    #player_spaceship.gold -= 5

                #if fuel_button.hovering_check(mouse_pos) and fuel_button.clicked and fuel_button.enabled and player_spaceship.gold >= 15:
                #    player_spaceship.fuel += 20
                #    player_spaceship.gold -= 15
                #if food_button.hovering_check(mouse_pos) and food_button.clicked and food_button.enabled and player_spaceship.gold >= 10:
                #    player_spaceship.food += 20
                #    player_spaceship.gold -= 10
                #if water_button.hovering_check(mouse_pos) and water_button.clicked and water_button.enabled and player_spaceship.gold >= 10:
                #    player_spaceship.water += 20
                #    player_spaceship.gold -= 10

                # enable continue button with crew >= 1
                if (player_spaceship.helmsmen + player_spaceship.carpenters + player_spaceship.surgeons + player_spaceship.buccaneers + player_spaceship.scientists + player_spaceship.deckhands) >= 1:
                    reset_button.enabled = True
                    continue_button.enabled = True

                # disable fuel/food/water buttons if maxed
                #if player_spaceship.fuel == player_spaceship.max_fuel:
                #    fuel_button.enabled = False
                #    fuel_button.str = "FUEL DRUM - MAX"
                #if player_spaceship.food == player_spaceship.max_food:
                #    food_button.enabled = False
                #    food_button.str = "FOOD BARREL - MAX"
                #if player_spaceship.water == player_spaceship.max_water:
                #    water_button.enabled = False
                #    water_button.str = "WATER CASK - MAX"
                
                # disable crewmate buttons if maxed
                if player_spaceship.max_crewmates == 0:
                    helmsman_button.enabled = False
                    deckhand_button.enabled = False
                    buccaneer_button.enabled = False
                    carpenter_button.enabled = False
                    surgeon_button.enabled = False
                    scientist_button.enabled = False
                    helmsman_button.str = "HELMSMEN - MAX"
                    deckhand_button.str = "DECKHAND - MAX"
                    buccaneer_button.str = "BUCCANEER - MAX"
                    carpenter_button.str = "CARPENTER - MAX"
                    surgeon_button.str = "SURGEON - MAX"
                    scientist_button.str = "SCIENTIST - MAX"
                
                # disable buttons if cannot afford
                #if player_spaceship.gold < 2:
                #    deckhand_button.enabled = False
                #if player_spaceship.gold < 3:
                #    buccaneer_button.enabled = False
                #    scientist_button.enabled = False
                #if player_spaceship.gold < 5:
                #    helmsman_button.enabled = False
                #    carpenter_button.enabled = False
                #    surgeon_button.enabled = False
                #    buccaneer_button.enabled = False
                #    scientist_button.enabled = False
                #    deckhand_button.enabled = False
                #if player_spaceship.gold < 10:
                #    if player_spaceship.food != player_spaceship.max_food:
                #        food_button.enabled = False
                #    if player_spaceship.water != player_spaceship.max_water:
                #        water_button.enabled = False
                #if player_spaceship.gold < 15:
                #    if player_spaceship.fuel != player_spaceship.max_fuel:
                #        fuel_button.enabled = False

                # reset click 
                reset_button.clicked = False
                continue_button.clicked = False
                #fuel_button.clicked = False
                #food_button.clicked = False
                #water_button.clicked = False
                helmsman_button.clicked = False
                deckhand_button.clicked = False
                buccaneer_button.clicked = False
                carpenter_button.clicked = False
                surgeon_button.clicked = False
                scientist_button.clicked = False
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)