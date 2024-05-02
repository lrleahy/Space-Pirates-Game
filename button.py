import pygame, sys, time, math, random
from configs import *

class BUTTON:
    def __init__(self, width, height, xpos, ypos, str):
        self.enabled = False
        self.clicked = False
        self.button_color = BLACK
        self.outline_color = WHITE
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.str = str
        self.str_color = WHITE
    
    def draw(self, SCREEN) -> None:
        # Call this method to draw the button on the screen

        pygame.draw.rect(SCREEN, self.outline_color, (self.xpos-2, self.ypos-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(SCREEN, self.button_color, (self.xpos, self.ypos, self.width, self.height), 0)

        if self.enabled == False:
            self.str_color = RED
            self.outline_color = RED
            self.button_color = BLACK

        if self.str != '':
            font = pygame.font.SysFont('yugothic', 15, bold=True)
            surface = font.render(self.str, 1, self.str_color)
            SCREEN.blit(surface, (self.xpos + (self.width/2 - surface.get_width()/2), self.ypos + (self.height/2 - surface.get_height()/2)))

    def hovering_check(self, mouse_pos) -> bool:
        return True if (((mouse_pos[0] > self.xpos and mouse_pos[0] < self.xpos + self.width) and (mouse_pos[1] > self.ypos and mouse_pos[1] < self.ypos + self.height)) and self.enabled) else False
        
    def hovering_color(self, mouse_pos) -> None:
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.enabled:
            if ((mouse_pos[0] > self.xpos and mouse_pos[0] < self.xpos + self.width) and (mouse_pos[1] > self.ypos and mouse_pos[1] < self.ypos + self.height)):
                self.button_color = WHITE
                self.outline_color = BLACK
                self.str_color = BLACK
            else:
                self.button_color = BLACK
                self.outline_color = WHITE
                self.str_color = WHITE