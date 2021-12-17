import pygame
import Button


class Board:
    black = (0, 0, 0)
    gray = (150, 150, 150)
    rect_outlines_0 = pygame.Rect(80, 80, 300, 175)
    rect_outlines_1 = pygame.Rect(460, 80, 300, 175)
    rect_outlines_2 = pygame.Rect(840, 80, 300, 175)
    rect_outlines_3 = pygame.Rect(80, 295, 300, 175)
    rect_outlines_4 = pygame.Rect(460, 295, 300, 175)
    rect_outlines_5 = pygame.Rect(840, 295, 300, 175)
    rect_outlines_6 = pygame.Rect(80, 510, 300, 175)
    rect_outlines_7 = pygame.Rect(460, 510, 300, 175)
    rect_outlines_8 = pygame.Rect(840, 510, 300, 175)
    rect_outlines_9 = pygame.Rect(80, 725, 300, 175)
    rect_outlines_10 = pygame.Rect(460, 725, 300, 175)
    rect_outlines_11 = pygame.Rect(840, 725, 300, 175)
    rect_outlines = [rect_outlines_0, rect_outlines_1, rect_outlines_2, rect_outlines_3, rect_outlines_4,
                     rect_outlines_5, rect_outlines_6, rect_outlines_7, rect_outlines_8, rect_outlines_9,
                     rect_outlines_10, rect_outlines_11]
    button_list = []
    player_one_score = ''
    player_two_score = ''
    computer_score = ''

    def __init__(self):
        self.back_button = Button.DisplayButton('meun', [40, 20], 30, '<-')
        self.button_list.append(self.back_button)

    def print_board(self, screen):
        screen.fill(self.gray)
        for rect in self.rect_outlines:
            pygame.draw.rect(screen, self.black, rect, 7, 20)
        self.back_button.print_button(screen)
        image = pygame.image.load('set_back_arrow.svg')
        screen.blit(image, (0, 0))

    def print_player_one_score(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render('Player 1: ' + str(self.player_one_score), True, self.black)
        screen.blit(text_obj, (40, 915))

    def print_player_two_score(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render('Player 2: ' + str(self.player_two_score), True, self.black)
        screen.blit(text_obj, (40, 960))

    def print_computer_score(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render('Computer: ' + str(self.player_two_score), True, self.black)
        screen.blit(text_obj, (12, 960))

    def reset_board(self):
        self.player_one_score = ''
        self.player_two_score = ''
        self.computer_score = ''



