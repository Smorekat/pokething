import pygame as pg

class button():
    def __init__(self, x, y, w, h, color, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.dimensions = [x, y, w, h]
        # self.rect = [self.color, self.dimensions]
        
attack_button = button(180, 300, 160, 100, (255, 50, 100), 'ATK')
bag_button = button(340, 300, 160, 100, (100, 50, 255), 'BAG')
char_button = button(180, 400, 160, 100, (50, 100, 255), 'GUY')
run_button = button(340, 400, 160, 100, (5, 255, 100), 'RUN')


button_list = [attack_button, bag_button, char_button, run_button]
#         if (p.user[0][0]+p.user[2][0]+p.velocity[0] > sector[1][0] and p.user[0][1]+p.user[2][1]+p.velocity[1] > sector[1][1]) and (p.user[0][0]+p.velocity[0] < sector[1][0]+sector[1][2] and p.user[0][1]+p.velocity[1] < sector[1][1] + sector[1][3]):
# (mx() > primaryActions.attack[0][0] and my() > primaryActions.attack[0][1]) and (mx() < primaryActions.attack[1][0] and my() < primaryActions.attack[1][1])
def check_click(mx, my):
    #for event in pg.MOUSE_DOWN:
        for button in button_list:
            # if #((pg.mouse.get_pos()[0] > button.x and pg.mouse.get_pos()[1] > button.y) and (pg.mouse.get_pos()[0] < button.x+button.w and pg.mouse.get_pos()[1] < button.y + button.w)):
            if ((mx > button.x and my > button.y) and (mx < button.x+button.w and my < button.y + button.w)):
                return button.text