import pygame, sys, time, math, random
from configs import *

class CREWMATE:
    def __init__(self, job):
        self.name = "? [ CREWMATE NAME ] ?"
        self.alive = True
        self.job = job
        self.busy = False
        self.busy_wait = 0
        self.busy_status = "[ AVAILABLE ]"
        self.repair = ""
        self.healer = ""
        self.healing = ""
        self.gender = "X"
        self.max_health = 20
        self.health = self.max_health
        self.max_hunger = 20
        self.hunger = self.max_hunger
        self.max_thirst = 20
        self.thirst = self.max_thirst
        self.distressed = False
        self.expedition = False
        self.speech = "'Yargh.'"

        self.choose_gender()

        self.ONE_SYMBOL = "|"
        self.ZERO_SYMBOL = "-"

    # RETURN STAT STRINGS #
    def health_string(self) -> str:

        health = math.ceil(self.health)

        health_str = "HEALTH NL {"
        for _ in range(self.health):
            health_str += self.ONE_SYMBOL
        for _ in range(self.max_health - health):
            health_str += self.ZERO_SYMBOL
        health_str += "}"

        return health_str

    def hunger_string(self) -> str:

        hunger = math.ceil(self.hunger)

        hunger_str = "HUNGER NL {"
        for _ in range(self.hunger):
            hunger_str += self.ONE_SYMBOL
        for _ in range(self.max_hunger - hunger):
            hunger_str += self.ZERO_SYMBOL
        hunger_str += "}"

        return hunger_str

    def thirst_string(self) -> str:

        thirst = math.ceil(self.thirst)

        thirst_str = "THIRST NL {"
        for _ in range(self.thirst):
            thirst_str += self.ONE_SYMBOL
        for _ in range(self.max_thirst - thirst):
            thirst_str += self.ZERO_SYMBOL
        thirst_str += "}"

        return thirst_str
    
    def check_distressed(self) -> None:
        if self.health < self.max_health or self.hunger <= 3 or self.thirst <= 9:
            self.distressed = True
        else:
            self.distressed = False
            

    # SET NAME, GENDER, AND JOB #
    def choose_gender(self) -> None:
        
        self.gender = "M" if random.randint(0,1) == 1 else "F"

    def choose_speech(self) -> None:

        injured_speech_options = [
            "\"Yargh! I be needin' a %$*#@ doctor matey!\"",
            "\"Ye best sail on without me. I be one foot in the locker.\"",
            "\"Don't ye be worrin' 'bout me. I been worse.\""
        ]
        hungry_speech_options = {
            "",
        }
        thirsty_speech_options = {
            "",
        }