"""
Create-task
"""

import pygame as pg
from pygame.locals import NOFRAME

# DUE: APRIL 15

# TODO: a lot lol
# TODO: add user input in mouse
# TODO: add user input in keyboard username
name = ""
pg.font.init()
font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 50)
nameplate = nameplate = font.render(name, True, (255,255,255))


# main --------------------------------------------------------------------------------

def get_name():
    global name, font, nameplate
    # font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 50)
    
    finished = False
    while(finished != True):
        screen.fill((100,100,100))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    finished = True
                    break
                elif event.key == pg.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) > 10:
                        continue
                    else:
                        name += event.unicode
        pg.draw.line(screen, (0, 255, 0), [80, 250], [400, 250])
        nameplate = font.render(name, True, (255,255,255))
        screen.blit(nameplate, (80, 195))
        display()
        # wprint(name)
    del finished, font

def start():
    pg.init()

    while (running):
        # input
        # loop function
        screen.fill((0,0,0))
        render()
        # display
        display()


# gui -----------------------------------------------------------------------

class button():
    def __init__(self, x, y, w, h, color, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.dimensions = [x, y, w, h]

attack_button = button(180, 400, 160, 100, (255, 50, 100), 'ATK')
run_button = button(340, 400, 160, 100, (5, 255, 100), 'RUN')
button_list = [attack_button, run_button]
#         if (p.user[0][0]+p.user[2][0]+p.velocity[0] > sector[1][0] and p.user[0][1]+p.user[2][1]+p.velocity[1] > sector[1][1]) and (p.user[0][0]+p.velocity[0] < sector[1][0]+sector[1][2] and p.user[0][1]+p.velocity[1] < sector[1][1] + sector[1][3]):
# (mx() > primaryActions.attack[0][0] and my() > primaryActions.attack[0][1]) and (mx() < primaryActions.attack[1][0] and my() < primaryActions.attack[1][1])
def check_click(mx, my):
    #for event in pg.MOUSE_DOWN:
        for button in button_list:
            # if #((pg.mouse.get_pos()[0] > button.x and pg.mouse.get_pos()[1] > button.y) and (pg.mouse.get_pos()[0] < button.x+button.w and pg.mouse.get_pos()[1] < button.y + button.w)):
            if ((mx > button.x and my > button.y) and (mx < button.x+button.w and my < button.y + button.w)):
                return button.text






# render ------------------------------------------------------------------------------------------------

# from gui import attackbutton as a

size = width, height = (500, 500)   # set window/screen dimensions
screen = pg.display.set_mode(size, NOFRAME, 32)  # make screen
# icon = pg.image.load("./img/icon.jpg")  # import icon 
# pg.display.set_icon(icon)   # set icon
running = True  # set game to run
# name = name


# pg.font.init()
# font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 50)
    # display()
    #particle_logic()

mainClock = pg.time.Clock()
def display():
    global running
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            running = False  
        if event.type == pg.MOUSEBUTTONDOWN:
            check_click(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])
    pg.display.update()
    pg.display.flip()
    
    mainClock.tick(60)


# rendering functions ----------------------------------------------------------------
def draw_characters():
    character = pg.image.load("./img/charles.png")
    character=character.convert_alpha()
    screen.blit(character, (100, 100))

def draw_buttons():
    global label, font
    font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 50)
    for button in button_list:
        pg.draw.rect(screen, button.color, button.dimensions)
        label = font.render(button.text, True, (255,255,255))
        screen.blit(label, (button.x+35, button.y+25))
        # del label

def render(): 
    global name
    draw_characters()
    draw_buttons()

    small_font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 20)
    uname = small_font.render(name, True, (255,255,255))
    screen.blit(uname, (80, 0))

if __name__ == '__main__':
    get_name()
    start()