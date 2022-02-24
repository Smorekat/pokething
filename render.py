# from matplotlib.pyplot import draw
import pygame as pg
from pygame.locals import NOFRAME
import gui
# from gui import attackbutton as a

size = width, height = (500, 500)   # set window/screen dimensions
screen = pg.display.set_mode(size, NOFRAME, 32)  # make screen
# icon = pg.image.load("./img/icon.jpg")  # import icon 
# pg.display.set_icon(icon)   # set icon
running = True  # set game to run

pg.font.init()
button_font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 50)

def loop():
    screen.fill((0,0,0))
    render()
    

    display()
    #particle_logic()

mainClock = pg.time.Clock()
def display():
    pg.display.update()
    pg.display.flip()
    
    mainClock.tick(60)

def check_quit():
    global running
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            running = False  
        if event.type == pg.MOUSEBUTTONDOWN:
            gui.check_click(pg.mouse.get_pos()[0], pg.mouse.get_pos()[1])


# Rendering functions --------------------------
def draw_characters():
    character = pg.image.load("./img/charles.png")
    character=character.convert_alpha()
    screen.blit(character, (100, 100))

def draw_buttons():
    for button in gui.button_list:
        pg.draw.rect(screen, button.color, button.dimensions)
        label = button_font.render(button.text, True, (255,255,255))
        screen.blit(label, (button.x+35, button.y+25))
        del label

def render(): 
    draw_characters()
    draw_buttons()



def particle_logic():
    pass