import pygame

def print_logo(screen):
    font_obj = pygame.font.Font('freesansbold.ttf', 150)
    text_obj = font_obj.render('SET', True, (0,0,0))
    screen.blit(text_obj, (600-font_obj.size('SET')[0]/2, 100))

class Meun:

    button_list = []
    gray = (100, 100, 100)

    def __init__(self):
        pass

    def print_meun(self, screen):
        screen.fill(self.gray)
        for button in self.button_list:
            button.print_button(screen)
        print_logo(screen)

    def add_button(self, button):
        self.button_list.append(button)

