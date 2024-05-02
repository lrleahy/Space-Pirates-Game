import pygame, os, sys, time, math, random

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SPACE PIRATES")

# SCREEN CONFIGS #
SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()

# COLOR CONFIGS #
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,179,44) #GREEN = (0,128,0)
YELLOW = (238,210,2)
RED = (179,0,12) #RED = (139,0,0)
ORANGE = (255,127,0)

# TEXT CONFIGS #
TEXT_XSMALL = pygame.font.SysFont('yugothic',15,True)
TEXT_SMALL =  pygame.font.SysFont('yugothic',20,True)
TEXT_MEDIUM = pygame.font.SysFont('yugothic',25,True)
TEXT_LARGE =  pygame.font.SysFont('yugothic',30,True)
TEXT_XLARGE = pygame.font.SysFont('yugothic',50,True)


# HELPER FUNCTIONS #

# string = text to be wrapped
# xpos, ypos = coordinates to blit (it will auto center text on width)
# line_length = # of characters per line
# SCREEN = surface to blit on


def blit_paragraph(string, xpos, ypos, line_length, text_size, SCREEN, centered=True, color=WHITE) -> None:
    words = string.split(' ')
    lines = []
    current_line = {'text': '', 'color':color}
    for word in words:
        if word.startswith('&'):  # Check if word denotes a color change
            current_line['color'] = globals().get(word[1:], color)  # Get the color value or use white if not found
        elif word == "NL":  # Check for the special word "NL"
            if current_line['text']:  # Only add the current line if it's not empty
                lines.append(current_line)
            current_line = {'text': '', 'color': color}  # Reset current line
        else:
            if len(current_line['text']) + len(word) + 1 > line_length:
                lines.append(current_line)
                current_line = {'text': word, 'color': color}
            else:
                if current_line['text']:
                    # Add a space before the word if it's not the beginning of the line
                    current_line['text'] += ' '
                current_line['text'] += word
    lines.append(current_line)  # Add the last line
    
    y_offset = 0
    for line in lines:
        # Render each line and blit it to the screen
        if text_size == "XSMALL":
            line_surface = TEXT_XSMALL.render(line['text'], True, line['color'])
        elif text_size == "SMALL":
            line_surface = TEXT_SMALL.render(line['text'], True, line['color'])
        elif text_size == "MEDIUM":
            line_surface = TEXT_MEDIUM.render(line['text'], True, line['color'])
        else:
            print("LOGS:    ERROR; unknown text size in 'blit_paragraph' function call")

        if centered:
            SCREEN.blit(line_surface, (xpos - line_surface.get_width()/2, ypos + y_offset))
        else:
            SCREEN.blit(line_surface, (xpos, ypos + y_offset))
        
        y_offset += line_surface.get_height()  # Move y to the next line





# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct the path to the 'sounds' folder
sounds_dir = os.path.join(script_dir, 'sounds')
images_dir = os.path.join(script_dir, 'images')


raw_sun_image = pygame.image.load(os.path.join(images_dir, 'sun.png'))
sun_image = pygame.transform.scale(raw_sun_image, (60, 60))

raw_moon_image = pygame.image.load(os.path.join(images_dir, 'moon.png'))
moon_image = pygame.transform.scale(raw_moon_image, (75, 75))


clink_1_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'clink_1_original_sound.wav'))
clink_2_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'clink_2_original_sound.wav'))
clink_3_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'clink_3_original_sound.wav'))
clink_1_audio.set_volume(0.50)
clink_2_audio.set_volume(0.50)
clink_3_audio.set_volume(0.50)

clink_audio_pack = {
    1 : clink_1_audio,
    2 : clink_2_audio,
    3 : clink_3_audio
}

diceroll_1_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'diceroll_1_epidemic_sound.wav'))
diceroll_2_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'diceroll_2_epidemic_sound.wav'))
diceroll_3_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'diceroll_3_epidemic_sound.wav'))
diceroll_1_audio.set_volume(0.50)
diceroll_2_audio.set_volume(0.50)
diceroll_3_audio.set_volume(0.50)

diceroll_audio_pack = {
    1 : diceroll_1_audio,
    2 : diceroll_2_audio,
    3 : diceroll_3_audio
}

crash_1_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'crash_1_epidemic_sound.wav'))
crash_2_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'crash_2_epidemic_sound.wav'))
crash_1_audio.set_volume(0.50)
crash_2_audio.set_volume(0.50)
crash_audio_pack = {
    1 : crash_1_audio,
    2 : crash_2_audio,
}

explosion_1_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'distant_explosion_1_epidemic_sound.wav'))
explosion_2_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'distant_explosion_2_epidemic_sound.wav'))
explosion_3_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'distant_explosion_3_epidemic_sound.wav'))
explosion_1_audio.set_volume(0.50)
explosion_2_audio.set_volume(0.50)
explosion_3_audio.set_volume(0.50)

explosion_audio_pack = {
    1 : explosion_1_audio,
    2 : explosion_2_audio,
    3 : explosion_3_audio
}

laser_1_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'scifi_weapon_1_epidemic_sound.wav'))
laser_2_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'scifi_weapon_2_epidemic_sound.wav'))
laser_3_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'scifi_weapon_3_epidemic_sound.wav'))
laser_1_audio.set_volume(0.50)
laser_2_audio.set_volume(0.50)
laser_3_audio.set_volume(0.50)

laser_audio_pack = {
    1 : laser_1_audio,
    2 : laser_2_audio,
    3 : laser_3_audio
}

warp_travel_1_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'warp_dimension_1_epidemic_sound.wav'))
warp_travel_2_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'warp_dimension_2_epidemic_sound.wav'))
warp_travel_3_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'warp_dimension_3_epidemic_sound.wav'))
warp_travel_4_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'warp_dimension_4_epidemic_sound.wav'))
warp_travel_1_audio.set_volume(0.50)
warp_travel_2_audio.set_volume(0.50)
warp_travel_3_audio.set_volume(0.50)
warp_travel_4_audio.set_volume(0.50)

warp_travel_audio_pack = {
    1 : warp_travel_1_audio,
    2 : warp_travel_2_audio,
    3 : warp_travel_3_audio,
    4 : warp_travel_4_audio
}

warp_fail_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'warp_echo_epidemic_sound.wav'))
warp_fail_audio.set_volume(0.50)

warp_escape_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'warp_appear_epidemic_sound.wav'))
warp_escape_audio.set_volume(0.50)

laser_battle_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'laser_battle_epidemic_sound.wav'))
laser_battle_audio.set_volume(0.50)

power_down_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'power_down_epidemic_sound.wav'))
power_down_audio.set_volume(0.75)

alarm_audio = pygame.mixer.Sound(os.path.join(sounds_dir, 'spacestation_alarm_epidemic_sound.wav'))
alarm_audio.set_volume(0.50)

yarrr_sound = pygame.mixer.Sound(os.path.join(sounds_dir, 'yarrr.wav'))
yarrr_sound.set_volume(0.50)
