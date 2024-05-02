import pygame, sys, time, math, random
from configs import *
from crewmate import CREWMATE

class SPACESHIP:
    def __init__(self):

        # SHIP VARIABLES #
        self.name = "? [ SPACESHIP NAME ] ?"
        self.max_health = 50
        self.health = self.max_health
        self.max_oxygen = 50
        self.oxygen = self.max_oxygen
        self.max_fuel = 50
        self.fuel = self.max_fuel
        self.max_food = 50
        self.food = self.max_food
        self.max_water = 50
        self.water = self.max_water
        self.max_morale = 10
        self.morale = self.max_morale
        self.max_gold = 85
        self.gold = self.max_gold
        self.max_rum_crates = 15
        self.rum_crates = self.max_rum_crates
        self.days_left = 60
        self.total_days = self.days_left
        self.days_traveled = 0

        self.sod_health = self.health
        self.sod_oxygen = self.oxygen
        self.sod_fuel = self.fuel
        self.sod_food = self.food
        self.sod_water = self.water
        self.sod_days_left = self.days_left

        # SHIP CONDITIONS #
        self.oxygen_leak = False
        self.fuel_leak = False

        # CREW VARIABLES #
        self.crewmates_alive = []
        self.crewmates_dead = []
        self.max_crewmates = 15
        self.total_alive = 0
        self.total_dead = 0
        self.total_in_distress = 0
        self.helmsmen = 0
        self.deckhands = 0
        self.buccaneers = 0
        self.carpenters = 0
        self.surgeons = 0
        self.scientists = 0

        self.firstname_female = ["Vega", "Polaris", "Mirabelle", "Persephone", "Calypso",
                    "Thalassa", "Selene", "Iris", "Rhea", "Ophelia",
                    "Callisto", "Leda", "Phoebe", "Theia", "Sally",
                    "Conchella", "Luna", "Aurora", "Galaxia", "Astra"] 
        self.firstname_male = ["Titan", "Orion", "Helios", "Atlas", "Zephyrus",
                    "Aether", "Prometheus", "Hyperion", "Icarus", "Castor",
                    "Pollux", "Vulcan", "Apollo", "Perseus", "Eros",
                    "Mars", "Frank", "Cassius", "Galileo", "Sirius"]

        # EVENT VARIABLES #
        self.crewmates_expedition = []
        self.expedition_food = 0
        self.expedition_water = 0

        # STAT LEVEL SYMBOLS #
        self.ONE_SYMBOL = "|"
        self.ZERO_SYMBOL = "-"

        # GAME VARIABLES #
        self.game_over = False
        self.win = False

        self.pick_random_name()

    # RETURN NUMBER (INT) OF LIVING AND AVAILABLE CREWMATES BASED ON ROLE #
    def get_surgeons(self) -> int:
        return sum(1 for crewmate in self.crewmates_alive if crewmate.job == "SURGEON" and not crewmate.busy)

    def get_scientists(self) -> int:
        return sum(1 for crewmate in self.crewmates_alive if crewmate.job == "SCIENTIST" and not crewmate.busy)

    def get_helmsmen(self) -> int:
        return sum(1 for crewmate in self.crewmates_alive if crewmate.job == "HELMSMAN" and not crewmate.busy)

    def get_deckhands(self) -> int:
        return sum(1 for crewmate in self.crewmates_alive if crewmate.job == "DECKHAND" and not crewmate.busy)

    def get_buccaneers(self) -> int:
        return sum(1 for crewmate in self.crewmates_alive if crewmate.job == "BUCCANEER" and not crewmate.busy)

    def add_crewmate(self, job) -> None:
        new_crewmate = CREWMATE(job)
        if job == "DECKHAND" or job == "BUCCANEER":
            new_crewmate.expedition = True
        if new_crewmate.gender == "M":
            new_crewmate.name = random.choice(self.firstname_male)
            self.firstname_male.remove(new_crewmate.name)
        else:
            new_crewmate.name = random.choice(self.firstname_female)
            self.firstname_female.remove(new_crewmate.name)
        self.total_alive += 1
        self.crewmates_alive.append(new_crewmate)

    def generate_crew(self) -> None:
        for _ in range(self.helmsmen):
            self.add_crewmate("HELMSMAN")
        for _ in range(self.carpenters):
            self.add_crewmate("CARPENTER")
        for _ in range(self.surgeons):
            self.add_crewmate("SURGEON")
        for _ in range(self.scientists):
            self.add_crewmate("SCIENTIST")
        for _ in range(self.buccaneers):
            self.add_crewmate("BUCCANEER")
        for _ in range(self.deckhands):
            self.add_crewmate("DECKHAND")

    # RANDOMLY SELECT A SHIP NAME #
    def pick_random_name(self) -> None:
        name1 = ["STAR", "COSMIC", "NEBULA", "VOID", "COMET'S",
                 "STELLAR", "SPACE", "LUNAR", "ASTRO", "INTERSTELLAR",
                 "SOLAR", "CELESTIAL","METERO", "BLACK HOLE", "GALACTIC",
                 "ETHER", "PLANETARY", "COSMOS", "STARBOARD", "SUPERNOVA",
                 "ORBIT", "MOONBEAM", "QUANTUM", "DREAD"]
        name2 = ["MARAUDER", "CORSAIR", "RAIDER", "BUCCANEER","PLUNDERER",
                 "SCOURGE", "KRAKEN", "LOOTER", "AVENGER", "INVADER",
                 "SABRE", "OUTLAW", "BANDIT", "GHOUL", "SCALLYWAG",
                 "EXPLORER", "ADVENTURER","PIRATE", "VOYAGER", "ARGONAUT",
                 "SCAVENGER", "DESPERADO", "SCOUNDREL", "ZEPHYR", "STORMER",
                 "ASSASSIN", "CUTTHROAT", "MUTINEER", "NAVIGATOR","SHARK",
                 "OMEN", "STARSHIP", "ECLIPSE", "NEW MOON"]
        self.name = "THE "+random.choice(name1)+" "+random.choice(name2)

    # RETURN STAT STRINGS #
    def rum_string(self) -> str:
        rum_str = "CARGO {"
        for _ in range(self.rum_crates):
            rum_str += "[R]"
        for _ in range(self.max_rum_crates - self.rum_crates):
            rum_str += "[_]"
        rum_str += "}"

        return rum_str

    def health_string(self) -> str:
        health_str = "HLTH {"

        for _ in range(self.health):
            health_str += self.ONE_SYMBOL
        for _ in range(self.max_health - self.health):
            health_str += self.ZERO_SYMBOL

        health_str += "}"
        return health_str
    
    def oxygen_string(self) -> str:
        oxygen_str = "OXYG {"

        for _ in range(self.oxygen):
            oxygen_str += self.ONE_SYMBOL
        for _ in range(self.max_oxygen - self.oxygen):
            oxygen_str += self.ZERO_SYMBOL

        oxygen_str += "}"
        return oxygen_str


    def fuel_string(self) -> str:
        fuel_str = "FUEL {"

        for _ in range(self.fuel):
            fuel_str += self.ONE_SYMBOL
        for _ in range(self.max_fuel - self.fuel):
            fuel_str += self.ZERO_SYMBOL

        fuel_str += "}"
        return fuel_str
    
    def food_string(self) -> str:
        food_str = "FOOD {"

        for _ in range(math.ceil(self.food)):
            food_str += self.ONE_SYMBOL
        for _ in range(self.max_food - math.ceil(self.food)):
            food_str += self.ZERO_SYMBOL

        food_str += "}"
        return food_str
    
    def water_string(self) -> str:
        water_str = "WTER {"

        for _ in range(math.ceil(self.water)):
            water_str += self.ONE_SYMBOL
        for _ in range(self.max_water - math.ceil(self.water)):
            water_str += self.ZERO_SYMBOL

        water_str += "}"
        return water_str

    def progress_string(self) -> str:
        progress_str = ""
        if self.days_left <= self.total_days:
            for _ in range(self.total_days - self.days_left):
                progress_str += ". "
            progress_str += "> "
            for _ in range(self.days_left):
                progress_str += ". "
        else:
            progress_str += "> "
            for _ in range(self.total_days):
                progress_str += ". "

        progress_str += "X"

        return progress_str

    def update(self) -> None:
        
        #update crew
        for crewmate in self.crewmates_alive:
            if crewmate.repair == "SHIP":
                if self.health == self.max_health:
                    crewmate.busy = False
                    crewmate.busy_wait = 0
                    crewmate.busy_status = "[ AVAILABLE ]"
                    crewmate.repair = ""
                else:
                    self.health += 4
                    if self.health > self.max_health:
                        self.health = self.max_health
            if crewmate.repair == "OXYGEN":
                if self.oxygen_leak == False:
                    crewmate.busy = False
                    crewmate.busy_wait = 0
                    crewmate.busy_status = "[ AVAILABLE ]"
                    crewmate.repair = ""
                else:
                    self.oxygen_leak = False
                    crewmate.busy = False
                    crewmate.busy_wait = 0
                    crewmate.busy_status = "[ AVAILABLE ]"
                    crewmate.repair = ""
            if crewmate.repair == "FUEL":
                if self.fuel_leak == False:
                    crewmate.busy = False
                    crewmate.busy_wait = 0
                    crewmate.busy_status = "[ AVAILABLE ]"
                    crewmate.repair = ""
                else:
                    self.fuel_leak = False
                    crewmate.busy = False
                    crewmate.busy_wait = 0
                    crewmate.busy_status = "[ AVAILABLE ]"
                    crewmate.repair = ""
            # decrement busy waiting if busy
            if crewmate.busy == True:
                crewmate.busy_wait -= 1
            # make available if finished busy wait
            if crewmate.busy_wait == 0:
                crewmate.busy = False
                crewmate.busy_status = "[ AVAILABLE ]"
            # decrement hunger and thirst
            crewmate.hunger -= 1
            crewmate.thirst -= 3
            # check if died from hunger or thirst
            if crewmate.hunger <= 0 or crewmate.thirst <= 0:
                crewmate.health = 0
            # check and update dead
            if crewmate.health <= 0:
                self.total_alive -= 1
                self.total_dead += 1
                self.crewmates_dead.append(crewmate)
                crewmate.alive = False
                crewmate.busy = True
                crewmate.busy_wait = math.inf
                crewmate.busy_status = "[ DEAD ]"
                crewmate.repair = ""
                if crewmate.healing != "":
                    for patient in self.crewmates_alive:
                        if patient.name == crewmate.healing:
                            patient.busy = False
                            patient.busy_wait = 0
                            patient.busy_status = "[ AVAILABLE ]"
                            crewmate.healing = ""
                if crewmate.healer != "":
                    for surgeon in self.crewmates_alive:
                        if surgeon.name == crewmate.healer:
                            surgeon.busy = False
                            surgeon.busy_wait = 0
                            surgeon.busy_status = "[ AVAILABLE ]"
                            surgeon.healing = ""
                            crewmate.healer = ""
            # do any healing
            if crewmate.job == "SURGEON":
                if crewmate.healing != "":
                    for patient in self.crewmates_alive:
                        if patient.name == crewmate.healing:
                            patient.health = patient.max_health
                            if patient.health >= patient.max_health:
                                patient.health = patient.max_health
                                patient.healer = ""
                                patient.busy = False
                                patient.busy_wait = 0
                                patient.busy_status = "[ AVAILABLE ]"
                                crewmate.healing = ""
                                crewmate.busy = False
                                crewmate.busy_wait = 0
                                crewmate.busy_status = "[ AVAILABLE ]"


        # remove dead crewmates after
        for crewmate in self.crewmates_dead:
            if crewmate in self.crewmates_alive:
                self.crewmates_alive.remove(crewmate)
        
        # check for oxygen leak
        if self.oxygen_leak == True:
            self.oxygen -= 5
        else:
            if self.oxygen < self.max_oxygen:
                self.oxygen += 3
            if self.oxygen > self.max_oxygen:
                self.oxygen = self.max_oxygen
        # check for fuel leak
        if self.fuel_leak == True:
            self.fuel -= 1

        if self.oxygen < 0:
            self.oxygen = 0
        if self.fuel < 0:
            self.fuel = 0

    def check_win(self):
        # check for win condition
        if self.days_left == 0 and self.rum_crates > 0:
            self.win = True 

    def check_game_over(self):
        # check for lose conditions
        if self.total_alive <= 0:
            self.game_over = True
        if self.oxygen <= 0:
            self.game_over = True
        if self.health <= 0:
            self.game_over = True
        if self.rum_crates <= 0:
            self.game_over = True

'''
    # PRINT CREW COUNT TO SCREEN #
    def print_crew(self, SCREEN, xpos, ypos) -> None:
        crew_name_str =         f"{self.name}'S CREW"
        total_helmsmen_str =    f"{self.helmsmen} HELMSMEN"
        total_deckhands_str =   f"{self.deckhands} DECKHANDS"
        total_buccaneers_str =  f"{self.buccaneers} BUCCANEERS"
        total_carpenters_str =  f"{self.carpenters} CARPENTERS"
        total_surgeons_str =    f"{self.surgeons} SURGEONS"
        total_scientists_str =  f"{self.scientists} SCIENTISTS"
        total_alive_dead_str =  f"ALIVE: {self.total_alive} DEAD: {self.total_dead}"

        # CREATE SURFACES #
        crew_name_surface = TEXT_XSMALL.render(crew_name_str, True, WHITE)

        if self.helmsmen > 0:
            total_helmsmen_surface = TEXT_XSMALL.render(total_helmsmen_str, True, WHITE)
        else:
            total_helmsmen_surface = TEXT_XSMALL.render(total_helmsmen_str, True, RED)

        if self.deckhands > 0:
            total_deckhands_surface = TEXT_XSMALL.render(total_deckhands_str, True, WHITE)
        else:
            total_deckhands_surface = TEXT_XSMALL.render(total_deckhands_str, True, RED)

        if self.buccaneers > 0:
            total_buccanees_surface = TEXT_XSMALL.render(total_buccaneers_str, True, WHITE)
        else:
            total_buccanees_surface = TEXT_XSMALL.render(total_buccaneers_str, True, RED)

        if self.carpenters > 0:
            total_carpenters_surface = TEXT_XSMALL.render(total_carpenters_str, True, WHITE)
        else:
            total_carpenters_surface = TEXT_XSMALL.render(total_carpenters_str, True, RED)

        if self.surgeons > 0:
            total_surgeons_surface = TEXT_XSMALL.render(total_surgeons_str, True, WHITE)
        else:
            total_surgeons_surface = TEXT_XSMALL.render(total_surgeons_str, True, RED)

        if self.scientists > 0:
            total_scientists_surface = TEXT_XSMALL.render(total_scientists_str, True, WHITE)
        else:
            total_scientists_surface = TEXT_XSMALL.render(total_scientists_str, True, RED)

        total_alive_dead_surface = TEXT_XSMALL.render(total_alive_dead_str, True, WHITE)
        white_space = crew_name_surface.get_height()

        SCREEN.blit(crew_name_surface,          (xpos,ypos-white_space * 8))
        SCREEN.blit(total_helmsmen_surface,     (xpos,ypos-white_space * 7))
        SCREEN.blit(total_deckhands_surface,    (xpos,ypos-white_space * 6))
        SCREEN.blit(total_buccanees_surface,    (xpos,ypos-white_space * 5))
        SCREEN.blit(total_carpenters_surface,   (xpos,ypos-white_space * 4))
        SCREEN.blit(total_surgeons_surface,     (xpos,ypos-white_space * 3))
        SCREEN.blit(total_scientists_surface,   (xpos,ypos-white_space * 2))
        SCREEN.blit(total_alive_dead_surface,   (xpos,ypos-white_space))


    # PRINT STATS TO SCREEN #
    def print_stats(self, SCREEN, xpos, ypos) -> None:
        name_str =          f"{self.name}'S STATS"
        days_left_str =     f"{self.days_left} DAYS LEFT IN THE JOURNEY!"
        days_in_space_str = f"{self.days_in_space} DAYS IN SPACE!"

        # CREATE SURFACES #
        name_surface = TEXT_XSMALL.render(name_str, True, WHITE)
        if self.health >= 35:
            health_surface = TEXT_XSMALL.render(self.health_string(), True, GREEN)
        elif self.health >= 15:
            health_surface = TEXT_XSMALL.render(self.health_string(), True, YELLOW)
        else:
            health_surface = TEXT_XSMALL.render(self.health_string(), True, RED)

        if self.O2_leak == False:
            oxygen_surface = TEXT_XSMALL.render(self.oxygen_string(), True, GREEN)
        else:
            oxygen_surface = TEXT_XSMALL.render(self.oxygen_string(), True, RED)

        if self.fuel_leak == False:
            fuel_surface = TEXT_XSMALL.render(self.fuel_string(), True, WHITE)
        else:
            fuel_surface = TEXT_XSMALL.render(self.fuel_string(), True, RED)

        if self.food >= 35:
            food_surface = TEXT_XSMALL.render(self.food_string(), True, GREEN)
        elif self.food >= 15:
            food_surface = TEXT_XSMALL.render(self.food_string(), True, YELLOW)
        else:
            food_surface = TEXT_XSMALL.render(self.food_string(), True, RED)

        if self.water >= 35:
            water_surface = TEXT_XSMALL.render(self.water_string(), True, GREEN)
        elif self.water >= 15:
            water_surface = TEXT_XSMALL.render(self.water_string(), True, YELLOW)
        else:
            water_surface = TEXT_XSMALL.render(self.water_string(), True, RED)


        days_left_surface = TEXT_XSMALL.render(days_left_str, True, WHITE)
        days_in_space_surface = TEXT_XSMALL.render(days_in_space_str, True, WHITE)

        white_space = name_surface.get_height()

        SCREEN.blit(name_surface,           (xpos,ypos))
        SCREEN.blit(health_surface,         (xpos,ypos + white_space))
        SCREEN.blit(oxygen_surface,         (xpos,ypos + white_space * 2))
        SCREEN.blit(food_surface,           (xpos,ypos + white_space * 3))
        SCREEN.blit(water_surface,          (xpos,ypos + white_space * 4))
        SCREEN.blit(fuel_surface,           (xpos,ypos + white_space * 5))
        SCREEN.blit(days_left_surface,      (xpos,ypos + white_space * 6))
        SCREEN.blit(days_in_space_surface,  (xpos,ypos + white_space * 7))
'''