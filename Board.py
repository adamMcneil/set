import pygame


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

    def __init__(self):
        pass

    def print_board(self, screen):
        screen.fill(self.gray)
        for rect in self.rect_outlines:
            pygame.draw.rect(screen, self.black, rect, 7, 20)
