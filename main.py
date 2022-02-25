import render as ren
import pygame as pg
import gui as gui

# TODO: a lot lol
# TODO: add user input in mouse
# TODO: add user input in keyboard username
name = ""
def get_name():
    global name
    pg.font.init()
    font = pg.font.Font("./dependencies/VCR_OSD_MONO.ttf", 50)
    
    finished = False
    while(finished != True):
        ren.screen.fill((100,100,100))
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
        ren.check_quit()
        pg.draw.line(ren.screen, (0, 255, 0), [80, 250], [400, 250])
        label = font.render(name, True, (255,255,255))
        ren.screen.blit(label, (80, 195))
        ren.display()
        # wprint(name)
    del finished, font

def start():
    pg.init()


    while (ren.running):

        # input
        ren.check_quit()

        # loop function
        ren.loop()

        # display
        ren.display()



if __name__ == '__main__':
    get_name()
    start()