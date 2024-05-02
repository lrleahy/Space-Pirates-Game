from configs import *

# TEMPLATE FUNCTION #
def template_function():
    # TIME #
    time_start = time.time()
    # VARIABLES #
    VARIABLES_HERE = 0
    # SURFACES #
    template_surface = pygame.font.Font(None, 20).render("SURFACE", True, (255,255,255))
    # BUTTONS #
    BUTTONS_HERE = 0
    # SCREENS #
    screen_template = True
    # SCREEN VARIABLES #
    can_continue = False
    # GAME LOOP #
    running = True
    while running:
        # TIME & BACKGROUND #
        time_current = time.time()
        SCREEN.fill(BLACK)

        # TEMPLATE SCREEN #
        if screen_template:
            pass
            if can_continue:
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
                    running = False
                    pygame.quit()
                    sys.exit()
            # MOUSE EVENTS #
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == pygame.MOUSEMOTION:
                pass
        # UPDATE DISPLAY #
        pygame.display.update()
        clock.tick(40)


'''

class BUTTON:
    def __init__(self, width, height, xpos, ypos, str=''):
        self.button_color = BLACK
        self.outline_color = WHITE
        self.width = width
        self.height = height
        self.xpos = xpos - width/2
        self.ypos = ypos
        self.str = str
        self.str_color = WHITE
    
    def draw_VOID(self, SCREEN):
        # Call this method to draw the button on the screen

        pygame.draw.rect(SCREEN, self.outline_color, (self.xpos-2, self.ypos-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(SCREEN, self.button_color, (self.xpos, self.ypos, self.width, self.height), 0)
        
        if self.str != '':
            font = pygame.font.SysFont('yugothic', 15, bold=True)
            surface = font.render(self.str, 1, self.str_color)
            SCREEN.blit(surface, (self.xpos + (self.width/2 - surface.get_width()/2), self.ypos + (self.height/2 - surface.get_height()/2)))

    def hovering_BOOL(self, mouse_pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        return True if ((mouse_pos[0] > self.xpos and mouse_pos[0] < self.xpos + self.width) and (mouse_pos[1] > self.ypos and mouse_pos[1] < self.ypos + self.height)) else False


'''