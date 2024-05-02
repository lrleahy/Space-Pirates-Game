from configs import *
from asteroid_field_function import *
from off_course_function import *
from ship_function import *
from planet_function import *
from game_over_function import *
from win_function import *
from button import BUTTON


def roll_event(player_spaceship) -> None:

    odds = random.random()

    # 20% chance for nothing
    if 0 < odds < 0.20:
        pass
        #return True
    
    # 15% chance for getting lost
    elif 0.20 < odds < 0.35:
        screen_offcourse(player_spaceship)
        #return True
    
    # 15% chance for asteroid field
    elif 0.35 < odds < 0.50:
        screen_asteroids(player_spaceship)
        #return True
    
    # 25% chance for foreign ship
    elif 0.50 < odds < 0.75:
        screen_ship(player_spaceship)
        #return True
    
    # 25% chance for foreign planet
    else:
        screen_planet(player_spaceship)
        #return True

def random_fuel_leak(player_spaceship):
    
    odds = random.random()

    if odds < 0.05 and player_spaceship.fuel != 0:
        player_spaceship.fuel_leak = True

def random_oxygen_leak(player_spaceship):
    
    odds = random.random()

    if odds < 0.05:
        player_spaceship.oxygen_leak = True

# MAIN FUNCTION #
def screen_game(player_spaceship):
    print("LOGS:    now in screen_game function")
    # TIME #
    time_start = time.time()
    loading_time_start = time.time()
    time_start_sun = time.time()
    # SURFACES #
    loading_string = ""
    loading_surface = TEXT_LARGE.render(loading_string, True, WHITE)
    title_surface = TEXT_LARGE.render("", True, WHITE)
    subtitle_surface = TEXT_MEDIUM.render("", True, WHITE)
    curr_crewmate_surface = TEXT_MEDIUM.render("", True, WHITE)
    notice_surface = TEXT_SMALL.render("! ... !", True, WHITE)
    # BUTTONS #
    daily_report_button = BUTTON(width=150, height=50, xpos=SCREEN_WIDTH*0.4-150/2, ypos=SCREEN_HEIGHT*0.15, str="DAILY REPORT")
    crew_button = BUTTON(width=150, height=50, xpos=SCREEN_WIDTH*0.6-150/2, ypos=SCREEN_HEIGHT*0.15, str="CREW")
    continue_button = BUTTON(width=150, height=50, xpos=SCREEN_WIDTH/2-150/2, ypos=SCREEN_HEIGHT*0.3, str="CONTINUE")

    crewmate_next_button = BUTTON(width=50, height=50, xpos=SCREEN_WIDTH*0.6-50/2, ypos=SCREEN_HEIGHT*0.85, str=" > ")
    crewmate_prev_button = BUTTON(width=50, height=50, xpos=SCREEN_WIDTH*0.4-50/2, ypos=SCREEN_HEIGHT*0.85, str=" < ")

    crewmate_food_button = BUTTON(width=250, height=50, xpos=SCREEN_WIDTH-250-25, ypos=SCREEN_HEIGHT*0.3, str="GIVE FOOD RATION")
    crewmate_water_button = BUTTON(width=250, height=50, xpos=SCREEN_WIDTH-250-25, ypos=SCREEN_HEIGHT*0.4, str="GIVE WATER RATION")
    crewmate_heal_button =  BUTTON(width=250, height=50, xpos=SCREEN_WIDTH-250-25, ypos=SCREEN_HEIGHT*0.5, str="CALL SURGEON")

    crewmate_repair_ship_button =  BUTTON(width=250, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.3, str="REPAIR SHIP")
    crewmate_repair_o2_button =  BUTTON(width=250, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.4, str="REPAIR OXYGEN GENERATOR")
    crewmate_repair_fuel_button =  BUTTON(width=250, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.5, str="REPAIR FUEL TANK")

    crewmate_expedition_button = BUTTON(width=250, height=50, xpos=0+25, ypos=SCREEN_HEIGHT*0.3, str="EXPEDITION TEAM")

    crewmate_food_all_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.1-200/2, ypos=SCREEN_HEIGHT*0.7, str="GIVE ALL FOOD RATION")
    crewmate_water_all_button = BUTTON(width=200, height=50, xpos=SCREEN_WIDTH*0.1-200/2, ypos=SCREEN_HEIGHT*0.8, str="GIVE ALL WATER RATION")
    # SCREENS #
    traveling_toggle = True
    eod_toggle = False
    daily_report_toggle = False
    crew_toggle = False
    # VARIABLES #
    curr_crewmate = 0
    crew_busy_str = ""


    crew_busy_str = ""

    for crewmate in player_spaceship.crewmates_alive:
        expedition_str = "[ E ]"
        non_expedition_str = "[ - ]"
        busy_str = "[ B ]"
        available_str = "[ A ]"

        if crewmate.distressed:
            if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                crew_busy_str += f"&RED {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} | {expedition_str if crewmate.expedition else non_expedition_str} NL "
            else:
                crew_busy_str += f"&RED {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} NL "
        else:
            if crewmate.busy:
                if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                    crew_busy_str += f"&ORANGE {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} | {expedition_str if crewmate.expedition else non_expedition_str} NL "
                else:
                    crew_busy_str += f"&ORANGE {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} NL "
            else:
                if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                    crew_busy_str += f"&GREEN {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} | {expedition_str if crewmate.expedition else non_expedition_str} NL "
                else:
                    crew_busy_str += f"&GREEN {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} NL "
    
    travel_sound_played = False
    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        loading_time_current = time.time()
        time_current_sun = time.time()
        SCREEN.fill(BLACK)

        loading_surface = TEXT_LARGE.render(loading_string, True, WHITE)
        SCREEN.blit(loading_surface, ((SCREEN_WIDTH/2 - loading_surface.get_width()/2), (SCREEN_HEIGHT/2 - loading_surface.get_height()/2)))
        SCREEN.blit(title_surface, ((SCREEN_WIDTH/2 - title_surface.get_width()/2), SCREEN_HEIGHT*0.05))
        SCREEN.blit(subtitle_surface, ((SCREEN_WIDTH/2 - subtitle_surface.get_width()/2), SCREEN_HEIGHT*0.1))

        
        blit_paragraph(string=player_spaceship.progress_string(),xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.95,line_length=300,text_size="SMALL",SCREEN=SCREEN,centered=True)


        if traveling_toggle:

            SCREEN.blit(sun_image, (0,SCREEN_HEIGHT-sun_image.get_height()))
            title_surface = TEXT_LARGE.render("TRAVELING", True, WHITE)

            if travel_sound_played != True:
                warp_travel_audio_pack[random.randint(1,4)].play()
                travel_sound_played = True
            if abs(time_start - time_current) < 4:
                if abs(loading_time_start - loading_time_current) >= 0.25:
                    if loading_string != "....":
                        loading_string += "."
                    else:
                        loading_string = "."
                    loading_time_start = loading_time_current
            else:
                travel_sound_played = False
                for crewmate in player_spaceship.crewmates_alive:
                    crewmate.check_distressed()
                    if crewmate.distressed:
                        player_spaceship.total_in_distress += 1
                curr_crewmate = 0
                random_fuel_leak(player_spaceship)
                random_oxygen_leak(player_spaceship)
                #if eventful_day:
                #    eventful_day = False
                #Eelse:
                #    eventful_day = roll_event(player_spaceship)
                roll_event(player_spaceship)
                # CHECK LOSE CONDITIONS
                player_spaceship.check_game_over()
                if player_spaceship.game_over:
                    return screen_game_over(player_spaceship)
                # TRAVEL UPDATE
                if player_spaceship.fuel > 0:
                    player_spaceship.days_traveled += 1
                    player_spaceship.days_left -= 1
                    player_spaceship.fuel -= 1
                else:
                    player_spaceship.days_traveled += 1
                # CHECK WIN CONDITIONS
                player_spaceship.check_win()
                if player_spaceship.win:
                    return screen_win(player_spaceship)
                # SHIP AND CREW UPDATE
                player_spaceship.update()
                # CHECK LOSE CONDITIONS
                player_spaceship.check_game_over()
                if player_spaceship.game_over:
                    return screen_game_over(player_spaceship)
                notice_surface = TEXT_SMALL.render("! ... !", True, WHITE)
                loading_string = ""
                daily_report_button.enabled = True
                crew_button.enabled = True
                continue_button.enabled = True
                eod_toggle = True
                traveling_toggle = False

        elif eod_toggle:

            SCREEN.blit(moon_image, (0,SCREEN_HEIGHT-moon_image.get_height()))

            stats_ship_str = f"{player_spaceship.name} NL "
            stats_ship_str += (f"{player_spaceship.health_string()} NL ") #if player_spaceship.health >= int(player_spaceship.max_health/2) else (f"&ORANGE {player_spaceship.health_string()} NL ")
            stats_ship_str += (f"{player_spaceship.oxygen_string()} NL ") #if not player_spaceship.oxygen_leak else (f"&ORANGE {player_spaceship.oxygen_string()} NL ")
            stats_ship_str += (f"{player_spaceship.fuel_string()} NL ") #if not player_spaceship.fuel_leak else (f"&ORANGE {player_spaceship.fuel_string()} NL ")
            stats_ship_str += (f"{player_spaceship.food_string()} NL ") #if player_spaceship.food >= int(player_spaceship.max_food/2) else (f"&ORANGE {player_spaceship.food_string()} NL ")
            stats_ship_str += (f"{player_spaceship.water_string()} NL ") #if player_spaceship.water >= int(player_spaceship.max_water/2) else (f"&ORANGE {player_spaceship.water_string()} NL ")
            stats_ship_str += (f"{player_spaceship.rum_string()} NL ")
            #distress_str = "CREWMATES IN DISTRESS: " + str(player_spaceship.total_in_distress)
            blit_paragraph(string=stats_ship_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.025,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)
            #blit_paragraph(string=distress_str,xpos=SCREEN_WIDTH*0.025,ypos=SCREEN_HEIGHT*0.2,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False, color=RED if player_spaceship.total_in_distress > 0 else WHITE)
            title_surface = TEXT_LARGE.render("END OF DAY "+str(player_spaceship.days_traveled), True, WHITE)

            if daily_report_toggle:

                daily_report_button.draw(SCREEN)
                subtitle_surface = TEXT_MEDIUM.render("DAILY REPORT", True, WHITE)
                daily_report_string1 = "SCHEDULE & CREW NL -------------------- NL "
                daily_report_string1 += f"DAY(S) TRAVELED NL { str(player_spaceship.days_traveled) } NL NL "
                daily_report_string1 += f"DAY(S) LEFT NL { str(player_spaceship.days_left) } NL NL "
                daily_report_string1 += f"CREWMATE(S) ALIVE NL &GREEN { str(player_spaceship.total_alive) } NL NL "
                daily_report_string1 += f"CREWMATE(S) DEAD NL &RED { str(player_spaceship.total_dead) } NL NL "
                daily_report_string1 += "-------------------- NL "

                daily_report_string2 = "SHIP & SUPPLIES NL -------------------- NL "
                daily_report_string2 += "SHIP HEALTH NL " + (("&GREEN " + str((player_spaceship.health/player_spaceship.max_health)*100) + "%" if player_spaceship.health > int(player_spaceship.max_health/2) else "&RED " + (str((player_spaceship.health/player_spaceship.max_health)*100) + "%")) if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "

                daily_report_string2 += "OXYGEN GENERATOR NL " + (("&RED DISABLED" if player_spaceship.oxygen_leak else "&GREEN ENABLED") if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "
                daily_report_string2 += "FUEL TANK NL " + (("&RED LEAKING" if player_spaceship.fuel_leak else "&GREEN STABLE") if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "
                daily_report_string2 += "OXYGEN SUPPLY NL " + (("&GREEN " + str((player_spaceship.oxygen/player_spaceship.max_oxygen)*100) + "%" if player_spaceship.oxygen > int(player_spaceship.max_oxygen/2) else "&RED " + (str((player_spaceship.oxygen/player_spaceship.max_oxygen)*100) + "%")) if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "
                daily_report_string2 += "FUEL SUPPLY NL " + (("&GREEN " + str(round((player_spaceship.fuel/player_spaceship.max_fuel)*100, 2)) + "%" if player_spaceship.fuel > int(player_spaceship.max_fuel/4) else "&RED " + (str(round((player_spaceship.fuel/player_spaceship.max_fuel)*100, 2)) + "%")) if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "
                daily_report_string2 += "FOOD SUPPLY NL " + (("&GREEN " + str(round((player_spaceship.food/player_spaceship.max_food)*100, 2)) + "%" if player_spaceship.food > int(player_spaceship.max_food/2) else "&RED " + (str(round((player_spaceship.food/player_spaceship.max_food)*100, 2)) + "%")) if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "
                daily_report_string2 += "WATER SUPPLY NL " + (("&GREEN " + str(round((player_spaceship.water/player_spaceship.max_water)*100, 2)) + "%" if player_spaceship.water > int(player_spaceship.max_water/2) else "&RED " + (str(round((player_spaceship.water/player_spaceship.max_water)*100, 2)) + "%")) if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL "
                daily_report_string2 += "-------------------- NL "

                daily_report_string3 = "+/- NL -------------------- NL "
                daily_report_string3 += (((("&GREEN + "+str(abs(player_spaceship.sod_health - player_spaceship.health))) if player_spaceship.sod_health <= player_spaceship.health else ("&RED - "+str(abs(player_spaceship.sod_health - player_spaceship.health)))) + " SHIP HEALTH" if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL ") if player_spaceship.sod_health != player_spaceship.health else ""
                daily_report_string3 += (((("&GREEN + "+str(abs(player_spaceship.sod_oxygen - player_spaceship.oxygen))) if player_spaceship.sod_oxygen <= player_spaceship.oxygen else ("&RED - "+str(player_spaceship.sod_oxygen - player_spaceship.oxygen))) + " OXYGEN" if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL ") if player_spaceship.sod_oxygen != player_spaceship.oxygen else ""
                daily_report_string3 += (((("&GREEN + "+str(abs(player_spaceship.sod_fuel - player_spaceship.fuel))) if player_spaceship.sod_fuel <= player_spaceship.fuel else ("&RED - "+str(abs(player_spaceship.sod_fuel - player_spaceship.fuel)))) + " FUEL" if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL ") if player_spaceship.sod_fuel != player_spaceship.fuel else ""
                daily_report_string3 += (((("&GREEN + "+str(round(abs(player_spaceship.sod_food - player_spaceship.food), 2))) if player_spaceship.sod_food <= player_spaceship.food else ("&RED - "+str(round(abs(player_spaceship.sod_food - player_spaceship.food), 2)))) + " FOOD" if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL ") if player_spaceship.sod_food != player_spaceship.food else  ""
                daily_report_string3 += (((("&GREEN + "+str(round(abs(player_spaceship.sod_water - player_spaceship.water), 2))) if player_spaceship.sod_water <= player_spaceship.water else ("&RED - "+str(round(abs(player_spaceship.sod_water - player_spaceship.water), 2)))) + " WATER" if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL ") if player_spaceship.sod_water != player_spaceship.water else ""
                daily_report_string3 += (((("&RED + "+str(abs(player_spaceship.sod_days_left - player_spaceship.days_left))) if player_spaceship.sod_days_left < player_spaceship.days_left else ("&GREEN - "+str(abs(player_spaceship.sod_days_left - player_spaceship.days_left)))) + " DAYS LEFT" if player_spaceship.get_scientists() > 0 else " &RED UNAVAILABLE") + " NL ") if player_spaceship.sod_days_left != player_spaceship.days_left else ""
                daily_report_string3 += "-------------------- NL "
                
                daily_report_string4 = "&RED SHIP DATA UNAVAILABLE, NO SCIENTIST(S) AVAILABLE NL "
                blit_paragraph(string=daily_report_string1,xpos=SCREEN_WIDTH*0.1,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN, centered=False)
                blit_paragraph(string=daily_report_string2,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN, centered=False)
                blit_paragraph(string=daily_report_string3,xpos=SCREEN_WIDTH*0.5,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN, centered=False)
                if player_spaceship.get_scientists() == 0:
                    blit_paragraph(string=daily_report_string4,xpos=SCREEN_WIDTH*0.1,ypos=SCREEN_HEIGHT*0.75,line_length=100,text_size="XSMALL",SCREEN=SCREEN, centered=False)

            elif crew_toggle:

                crewmate =  player_spaceship.crewmates_alive[curr_crewmate]
                curr_crewmate_surface = TEXT_MEDIUM.render(str(curr_crewmate+1) + " / " + str(player_spaceship.total_alive), True, WHITE)
                SCREEN.blit(curr_crewmate_surface, (SCREEN_WIDTH*0.5-curr_crewmate_surface.get_width()/2,SCREEN_HEIGHT*0.9))
                SCREEN.blit(notice_surface, (SCREEN_WIDTH*0.5-notice_surface.get_width()/2,SCREEN_HEIGHT*0.8))
                crew_button.draw(SCREEN)
                crewmate_str = crewmate.name + " NL "
                crewmate_str += crewmate.job + " NL "
                crewmate_str += "\"I love the sea.\" NL "
                crewmate_str += "EXPEDITION TEAM NL " if crewmate.expedition == True else ""
                #crewmate_distress_str = "! IN DISTRESS !"
                blit_paragraph(string=crewmate_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.3,line_length=100,text_size="XSMALL",SCREEN=SCREEN)
                #if crewmate.distressed:
                #    blit_paragraph(string=crewmate_distress_str,xpos=SCREEN_WIDTH/2,ypos=SCREEN_HEIGHT*0.4,line_length=100,text_size="XSMALL",SCREEN=SCREEN,color=RED)
                crewmate_stats_str = (("&GREEN " + crewmate.busy_status) if crewmate.busy == False else ("&ORANGE " + crewmate.busy_status)) + " NL "
                crewmate_stats_str += (f"{ crewmate.health_string() } NL ") if crewmate.health == crewmate.max_health else (f"&RED  { crewmate.health_string() } NL ")
                crewmate_stats_str += (f"{ crewmate.hunger_string() } NL ") if crewmate.hunger > 3 else (f"&RED  { crewmate.hunger_string() } NL ")
                crewmate_stats_str += (f"{ crewmate.thirst_string() } NL ") if crewmate.thirst > 9 else (f"&RED  { crewmate.thirst_string() } NL ")
                blit_paragraph(string=crewmate_stats_str,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.5,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)
                crewmate_next_button.draw(SCREEN)
                crewmate_prev_button.draw(SCREEN)
                crewmate_food_all_button.draw(SCREEN)
                crewmate_water_all_button.draw(SCREEN)
                crewmate_food_button.draw(SCREEN)
                crewmate_water_button.draw(SCREEN)
                crewmate_heal_button.draw(SCREEN)
                if crewmate.job == "CARPENTER":
                    crewmate_repair_ship_button.enabled = True
                    crewmate_repair_o2_button.enabled = True
                    crewmate_repair_fuel_button.enabled = True
                    crewmate_repair_ship_button.draw(SCREEN)
                    crewmate_repair_o2_button.draw(SCREEN)
                    crewmate_repair_fuel_button.draw(SCREEN)
                else:
                    crewmate_repair_ship_button.enabled = False
                    crewmate_repair_o2_button.enabled = False
                    crewmate_repair_fuel_button.enabled = False
                if crewmate.job == "BUCCANEER" or crewmate.job == "DECKHAND":
                    crewmate_expedition_button.enabled = True
                    crewmate_expedition_button.draw(SCREEN)
                else:
                    crewmate_expedition_button.enabled = False
                subtitle_surface = TEXT_MEDIUM.render("CREW", True, WHITE)
            else:
                blit_paragraph(string=crew_busy_str,xpos=SCREEN_WIDTH*0.3,ypos=SCREEN_HEIGHT*0.4,line_length=100,text_size="XSMALL",SCREEN=SCREEN,centered=False)
                daily_report_button.draw(SCREEN)
                crew_button.draw(SCREEN)
                continue_button.draw(SCREEN)
                subtitle_surface = TEXT_MEDIUM.render("", True, WHITE)
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
                daily_report_button.hovering_color(mouse_pos)
                crew_button.hovering_color(mouse_pos)
                continue_button.hovering_color(mouse_pos)
                crewmate_next_button.hovering_color(mouse_pos)
                crewmate_prev_button.hovering_color(mouse_pos)
                crewmate_food_all_button.hovering_color(mouse_pos)
                crewmate_water_all_button.hovering_color(mouse_pos)
                crewmate_food_button.hovering_color(mouse_pos)
                crewmate_water_button.hovering_color(mouse_pos)
                crewmate_heal_button.hovering_color(mouse_pos)
                crewmate_repair_ship_button.hovering_color(mouse_pos)
                crewmate_repair_o2_button.hovering_color(mouse_pos)
                crewmate_repair_fuel_button.hovering_color(mouse_pos)
                crewmate_expedition_button.hovering_color(mouse_pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if daily_report_button.hovering_check(mouse_pos):
                    daily_report_button.clicked = True
                if crew_button.hovering_check(mouse_pos):
                    crew_button.clicked = True
                if continue_button.hovering_check(mouse_pos):
                    continue_button.clicked = True
                if crewmate_next_button.hovering_check(mouse_pos):
                    crewmate_next_button.clicked = True
                if crewmate_prev_button.hovering_check(mouse_pos):
                    crewmate_prev_button.clicked = True
                if crewmate_food_all_button.hovering_check(mouse_pos):
                    crewmate_food_all_button.clicked = True
                if crewmate_water_all_button.hovering_check(mouse_pos):
                    crewmate_water_all_button.clicked = True
                if crewmate_food_button.hovering_check(mouse_pos):
                    crewmate_food_button.clicked = True
                if crewmate_water_button.hovering_check(mouse_pos):
                    crewmate_water_button.clicked = True
                if crewmate_heal_button.hovering_check(mouse_pos):
                    crewmate_heal_button.clicked = True
                if crewmate_repair_ship_button.hovering_check(mouse_pos):
                    crewmate_repair_ship_button.clicked = True
                if crewmate_repair_o2_button.hovering_check(mouse_pos):
                    crewmate_repair_o2_button.clicked = True
                if crewmate_repair_fuel_button.hovering_check(mouse_pos):
                    crewmate_repair_fuel_button.clicked = True
                if crewmate_expedition_button.hovering_check(mouse_pos):
                    crewmate_expedition_button.clicked = True
            if event.type == pygame.MOUSEBUTTONUP:
                # CLICK DAILY REPORT BUTTON #
                if daily_report_button.hovering_check(mouse_pos) and daily_report_button.clicked and daily_report_button.enabled:
                    if daily_report_toggle == False:
                        crew_button.enabled = False
                        continue_button.enabled = False
                        daily_report_toggle = True
                        daily_report_button.str = "GO BACK"
                    else:
                        crew_button.enabled = True
                        continue_button.enabled = True
                        daily_report_toggle = False
                        daily_report_button.str = "DAILY REPORT"
                # CLICK CREW BUTTON #
                if crew_button.hovering_check(mouse_pos) and crew_button.clicked and crew_button.enabled:
                    if crew_toggle == False:
                        daily_report_button.enabled = False
                        continue_button.enabled = False
                        crewmate_next_button.enabled = True
                        crewmate_prev_button.enabled = True
                        crewmate_food_all_button.enabled = True
                        crewmate_water_all_button.enabled = True
                        crewmate_food_button.enabled = True
                        crewmate_water_button.enabled = True
                        crewmate_heal_button.enabled = True
                        crewmate_repair_ship_button.enabled = True
                        crewmate_repair_o2_button.enabled = True
                        crewmate_repair_fuel_button.enabled = True
                        crewmate_expedition_button.enabled = True
                        crew_toggle = True
                        crew_button.str = "GO BACK"
                    else:
                        daily_report_button.enabled = True
                        continue_button.enabled = True
                        crewmate_next_button.enabled = False
                        crewmate_prev_button.enabled = False
                        crewmate_food_all_button.enabled = False
                        crewmate_water_all_button.enabled = False
                        crewmate_food_button.enabled = False
                        crewmate_water_button.enabled = False
                        crewmate_heal_button.enabled = False
                        crewmate_repair_ship_button.enabled = False
                        crewmate_repair_o2_button.enabled = False
                        crewmate_repair_fuel_button.enabled = False
                        crewmate_expedition_button.enabled = False
                        crew_toggle = False
                        crew_button.str = "CREW"
                # CLICK CONTINUE BUTTON #
                if continue_button.hovering_check(mouse_pos) and continue_button.clicked and continue_button.enabled:
                    player_spaceship.sod_health = player_spaceship.health
                    player_spaceship.sod_oxygen = player_spaceship.oxygen
                    player_spaceship.sod_fuel = player_spaceship.fuel
                    player_spaceship.sod_food = player_spaceship.food
                    player_spaceship.sod_water = player_spaceship.water
                    player_spaceship.sod_days_left = player_spaceship.days_left
                    crew_button.enabled = False
                    daily_report_button.enabled = False
                    continue_button.enabled = False
                    eod_toggle = False
                    traveling_toggle = True
                    loading_time_start = loading_time_current
                    time_start = time_current
                # CLICK NEXT BUTTON #
                if crewmate_next_button.hovering_check(mouse_pos) and crewmate_next_button.clicked and crewmate_next_button.enabled:
                    notice_surface = TEXT_SMALL.render("! ... !", True, WHITE)
                    if curr_crewmate == player_spaceship.total_alive - 1:
                        curr_crewmate = 0
                    else:
                        curr_crewmate += 1
                # CLICK PREV BUTTON #
                if crewmate_prev_button.hovering_check(mouse_pos):
                    notice_surface = TEXT_SMALL.render("! ... !", True, WHITE)
                    if curr_crewmate == 0:
                        curr_crewmate = player_spaceship.total_alive - 1
                    else:
                        curr_crewmate -= 1
                # CLICK GIVE ALL FOOD RATION BUTTON #
                if crewmate_food_all_button.hovering_check(mouse_pos) and crewmate_food_all_button.clicked and crewmate_food_all_button.enabled:
                    for crewmate in player_spaceship.crewmates_alive:
                        if player_spaceship.food > 0 and (crewmate.hunger < crewmate.max_hunger):
                            crewmate.hunger += 1
                            player_spaceship.food -= 0.2
                # CLICK GIVE ALL WATER RATION BUTTON #
                if crewmate_water_all_button.hovering_check(mouse_pos):
                    for crewmate in player_spaceship.crewmates_alive:
                        if player_spaceship.water > 0 and crewmate.thirst < crewmate.max_thirst:
                            crewmate.thirst += 2
                            if crewmate.thirst > crewmate.max_thirst:
                                crewmate.thirst = crewmate.max_thirst
                            player_spaceship.water -= 0.2
                # CLICK GIVE FOOD RATION BUTTON #
                if crewmate_food_button.hovering_check(mouse_pos) and crewmate_food_button.clicked and crewmate_food_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    # check if ship has food and crewmate is hungry
                    if player_spaceship.food > 0 and (crewmate.hunger < crewmate.max_hunger):
                        crewmate.hunger += 1
                        player_spaceship.food -= 0.2
                    else:
                        if player_spaceship.food < 0.2:
                            notice_surface = TEXT_SMALL.render("! NOT ENOUGH FOOD !", True, WHITE)
                        else:
                            notice_surface = TEXT_SMALL.render("! THIS CREWMATE IS NOT HUNGRY !", True, WHITE)
                # CLICK GIVE WATER RATION BUTTON #
                if crewmate_water_button.hovering_check(mouse_pos) and crewmate_water_button.clicked and crewmate_water_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    # check if ship has water and crewmate is thirsty
                    if player_spaceship.water > 0 and (crewmate.thirst < crewmate.max_thirst):
                        crewmate.thirst += 2
                        player_spaceship.water -= 0.2
                    else:
                        if player_spaceship.water < 0.2:
                            notice_surface = TEXT_SMALL.render("! NOT ENOUGH WATER !", True, WHITE)
                        else:
                            notice_surface = TEXT_SMALL.render("! THIS CREWMATE IS NOT THIRSTY !", True, WHITE)
                # CLICK CALL SURGEON BUTTON #
                if crewmate_heal_button.hovering_check(mouse_pos) and crewmate_heal_button.clicked and crewmate_heal_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    if crewmate.busy == False:
                        if crewmate.health < crewmate.max_health:
                            # check for available surgeons
                            if player_spaceship.get_surgeons() > 0:
                                for surgeon in player_spaceship.crewmates_alive:
                                    if (surgeon.job == "SURGEON") and (surgeon.busy == False) and (surgeon != crewmate):
                                        surgeon.busy = True
                                        surgeon.busy_wait = math.inf
                                        surgeon.busy_status = "[ BUSY ] TREATING '" + crewmate.name + "'"
                                        surgeon.healing = crewmate.name
                                        crewmate.busy = True
                                        crewmate.busy_wait = math.inf
                                        crewmate.busy_status = "[ BUSY ] BEING TREATED BY '" + surgeon.name + "'"
                                        crewmate.healer = surgeon.name
                                        break
                                    if surgeon == crewmate and player_spaceship.get_surgeons() == 1:
                                        notice_surface = TEXT_SMALL.render("! SURGEONS CAN NOT OPERATE ON THEMSELVES !", True, WHITE)

                            else:
                                notice_surface = TEXT_SMALL.render("! NO SURGEONS AVAILABLE !", True, WHITE)
                        else:
                            notice_surface = TEXT_SMALL.render("! THIS CREWMATE IS NOT INJURED !", True, WHITE)
                    else:
                        notice_surface = TEXT_SMALL.render("! THIS CREWMATE IS BUSY !", True, WHITE)
                # CLICK REPAIR SHIP BUTTON #
                if crewmate_repair_ship_button.hovering_check(mouse_pos) and crewmate_repair_ship_button.clicked and crewmate_repair_ship_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    if crewmate.job == "CARPENTER":
                        if crewmate.busy == False or crewmate.repair != "":
                            if crewmate.repair == "SHIP":
                                crewmate.busy = False
                                crewmate.busy_wait = 0
                                crewmate.busy_status = "[ AVAILABLE ]"
                                crewmate.repair = ""
                                notice_surface = TEXT_SMALL.render("! NO LONGER REPAIRING SHIP !", True, WHITE)
                            else:
                                if player_spaceship.health < player_spaceship.max_health:
                                    crewmate.busy = True
                                    crewmate.busy_wait = math.inf
                                    crewmate.busy_status = "[ BUSY ] REPAIRING SHIP"
                                    crewmate.repair = "SHIP"
                                    notice_surface = TEXT_SMALL.render("! NOW REPAIRING SHIP !", True, WHITE)
                                else:
                                    notice_surface = TEXT_SMALL.render("! SHIP DOES NOT NEED REPAIRING !", True, WHITE)
                        else:
                            notice_surface = TEXT_SMALL.render("! THIS CARPENTER IS BUSY !", True, WHITE)
                    else:
                        notice_surface = TEXT_SMALL.render("! CREWMATE MUST BE A CARPENTER !", True, WHITE)
                # CLICK REPAIR OXYGEN GENERATOR BUTTON #
                if crewmate_repair_o2_button.hovering_check(mouse_pos) and crewmate_repair_o2_button.clicked and crewmate_repair_o2_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    if crewmate.job == "CARPENTER":
                        if crewmate.busy == False or crewmate.repair != "":
                            if crewmate.repair == "OXYGEN":
                                crewmate.busy = False
                                crewmate.busy_wait = 0
                                crewmate.busy_status = "[ AVAILABLE ]"
                                crewmate.repair = ""
                                notice_surface = TEXT_SMALL.render("! NO LONGER REPAIRING OXYGEN GENERATOR !", True, WHITE)
                            else:
                                if player_spaceship.oxygen_leak:
                                    crewmate.busy = True
                                    crewmate.busy_wait = math.inf
                                    crewmate.busy_status = "[ BUSY ] REPAIRING OXYGEN GENERATOR"
                                    crewmate.repair = "OXYGEN"
                                    notice_surface = TEXT_SMALL.render("! NOW REPAIRING OXYGEN GENERATOR !", True, WHITE)
                                else:
                                    notice_surface = TEXT_SMALL.render("! OXYGEN GENERATOR DOES NOT NEED REPAIRING !", True, WHITE)
                        else:
                            notice_surface = TEXT_SMALL.render("! THIS CARPENTER IS BUSY !", True, WHITE)
                    else:
                        notice_surface = TEXT_SMALL.render("! CREWMATE MUST BE A CARPENTER !", True, WHITE)
                # CLICK REPAIR FUEL TANK BUTTON #
                if crewmate_repair_fuel_button.hovering_check(mouse_pos) and crewmate_repair_fuel_button.clicked and crewmate_repair_fuel_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    if crewmate.job == "CARPENTER":
                        if crewmate.busy == False or crewmate.repair != "": 
                            if crewmate.repair == "FUEL":
                                crewmate.busy = False
                                crewmate.busy_wait = 0
                                crewmate.busy_status = "[ AVAILABLE ]"
                                crewmate.repair = ""
                                notice_surface = TEXT_SMALL.render("! NO LONGER REPAIRING FUEL TANK !", True, WHITE)
                            else:
                                if player_spaceship.fuel_leak:
                                    crewmate.busy = True
                                    crewmate.busy_wait = math.inf
                                    crewmate.busy_status = "[ BUSY ] REPAIRING FUEL TANK"
                                    crewmate.repair = "FUEL"
                                    notice_surface = TEXT_SMALL.render("! NOW REPAIRING FUEL TANK !", True, WHITE)
                                else:
                                    notice_surface = TEXT_SMALL.render("! FUEL TANK DOES NOT NEED REPAIRING !", True, WHITE)
                        else:
                            notice_surface = TEXT_SMALL.render("! THIS CARPENTER IS BUSY !", True, WHITE)
                    else:
                        notice_surface = TEXT_SMALL.render("! CREWMATE MUST BE A CARPENTER !", True, WHITE)
                if crewmate_expedition_button.hovering_check(mouse_pos) and crewmate_expedition_button.clicked and crewmate_expedition_button.enabled:
                    crewmate = player_spaceship.crewmates_alive[curr_crewmate]
                    if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                        if crewmate.expedition == False:
                            crewmate.expedition = True
                            notice_surface = TEXT_SMALL.render("! CREWMATE IS NOW ON EXPEDITION TEAM !", True, WHITE)
                        else:
                            crewmate.expedition = False
                            notice_surface = TEXT_SMALL.render("! CREWMATE IS NO LONGER ON EXPEDITION TEAM !", True, WHITE)
                    else:
                        notice_surface = TEXT_SMALL.render("! CREWMATE MUST BE A DECKHAND OR BUCCANEER !", True, WHITE)
                # reset clicks
                daily_report_button.clicked = False
                crew_button.clicked = False
                continue_button.clicked = False
                crewmate_next_button.clicked = False
                crewmate_prev_button.clicked = False
                crewmate_food_all_button.clicked = False
                crewmate_water_all_button.clicked = False
                crewmate_food_button.clicked = False
                crewmate_water_button.clicked = False
                crewmate_heal_button.clicked = False
                crewmate_repair_ship_button.clicked = False
                crewmate_repair_o2_button.clicked = False
                crewmate_repair_fuel_button.clicked = False
                crewmate_expedition_button.clicked = False

            player_spaceship.total_in_distress = 0
            for crewmate in player_spaceship.crewmates_alive:
                crewmate.check_distressed()
                if crewmate.distressed:
                    player_spaceship.total_in_distress += 1

            crew_busy_str = ""

            for crewmate in player_spaceship.crewmates_alive:
                expedition_str = "[ E ]"
                non_expedition_str = "[ - ]"
                busy_str = "[ B ]"
                available_str = "[ A ]"
                if crewmate.distressed:
                    if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                        crew_busy_str += f"&RED {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} | {expedition_str if crewmate.expedition else non_expedition_str} NL "
                    else:
                        crew_busy_str += f"&RED {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} NL "
                else:
                    if crewmate.busy:
                        if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                            crew_busy_str += f"&ORANGE {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} | {expedition_str if crewmate.expedition else non_expedition_str} NL "
                        else:
                            crew_busy_str += f"&ORANGE {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} NL "
                    else:
                        if crewmate.job == "DECKHAND" or crewmate.job == "BUCCANEER":
                            crew_busy_str += f"&GREEN {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} | {expedition_str if crewmate.expedition else non_expedition_str} NL "
                        else:
                            crew_busy_str += f"&GREEN {crewmate.job} {crewmate.name} | {busy_str if crewmate.busy else available_str} NL "
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)