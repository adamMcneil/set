import pygame
import Button


def print_logo(screen):
    font_obj = pygame.font.Font('freesansbold.ttf', 150)
    text_obj = font_obj.render('SET', True, (0, 0, 0))
    screen.blit(text_obj, (600 - font_obj.size('SET')[0] / 2, 100))


class Meun:
    button_list = []
    button_list_change_display = []
    button_list_difficulty = []
    gray = (100, 100, 100)

    def __init__(self):
        pass

    def print_meun(self, screen):
        # image = pygame.image.load('~/PycharmProjects/pythonProject4/set_background.svg')
        # screen.blit(image, (0, 0))
        screen.fill(self.gray)
        for button in self.button_list:
            button.print_button(screen)
        print_logo(screen)

    def add_button(self, button):
        self.button_list.append(button)
        if isinstance(button, Button.DisplayButton):
            self.button_list_change_display.append(button)
        elif isinstance(button, Button.DifficultyButton):
            self.button_list_difficulty.append(button)
        else:
            print("Button was not added")
