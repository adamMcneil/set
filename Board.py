import pygame
import Button


class Board:
    black = (0, 0, 0)
    gray = (100, 100, 100)
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
    player_one_score = 0
    player_two_score = 0

    def __init__(self):
        self.back_button = Button.Button('meun', [40, 13], 40, '<-')
        self.button_list.append(self.back_button)

    def print_board(self, screen):
        screen.fill(self.gray)
        for rect in self.rect_outlines:
            pygame.draw.rect(screen, self.black, rect, 7, 20)
        self.back_button.print_button(screen)

    def print_player_one_score(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render('Player 1: ' + str(self.player_one_score), True, self.black)
        screen.blit(text_obj, (40, 950))

    def print_player_two_score(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render('Player 2: ' + str(self.player_two_score), True, self.black)
        screen.blit(text_obj, (250, 950))

    def reset_board(self):
        self.player_one_score = 0
        self.player_two_score = 0



