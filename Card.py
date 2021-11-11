import pygame
import math
import random


class Card:
    white = (250, 250, 250)
    blue = (102, 0, 204)
    red = (255, 50, 50)
    green = (50, 210, 50)
    highlight_color = (255, 255, 204)
    default_color = white
    is_highlighted = False
    position_dict = {
        0: (7 + 80, 7 + 80),
        1: (7 + 460, 7 + 80),
        2: (7 + 840, 7 + 80),
        3: (7 + 80, 7 + 295),
        4: (7 + 460, 7 + 295),
        5: (7 + 840, 7 + 295),
        6: (7 + 80, 7 + 510),
        7: (7 + 460, 7 + 510),
        8: (7 + 840, 7 + 510),
        9: (7 + 80, 7 + 725),
        10: (7 + 460, 7 + 725),
        11: (7 + 840, 7 + 725)
    }

    def __init__(self, slot, deck):
        self.slot = slot
        self.width = 300 - 14
        self.height = 175 - 14
        self.position = self.position_dict[slot]
        self.color = self.default_color
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        print(len(deck.cards_in_deck) - 1)
        x = random.randint(0, len(deck.cards_in_deck) - 1)
        self.card_num = deck.cards_in_deck[x]
        while deck.num_of_sets_in_play() == 0 and len(deck.slots_open) < 2:
            x = random.randint(0, len(deck.cards_in_deck) - 1)
            self.card_num = deck.cards_in_deck[x]
        deck.add_card_play(self)
        deck.remove_card_deck(self)

    def select_Card(self, events, deck):
        collide = self.rect.collidepoint(pygame.mouse.get_pos())
        if collide:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_highlighted:
                        deck.remove_card_highlight(self)
                    else:
                        deck.add_card_highlight(self)
                    # self.is_highlighted = not self.is_highlighted

    def print_Card(self, screen):
        if self.is_highlighted:
            self.color = self.highlight_color
        else:
            self.color = self.default_color
        pygame.draw.rect(screen, self.color, self.rect, 1000, 15)

    def print_shapes(self, screen):
        outline = 1
        lines = False
        if self.card_num[1] == 0:
            outline = 0
        if self.card_num[1] == 1:
            outline = 5
            lines = True
        if self.card_num[1] == 2:
            outline = 5
        if self.card_num[3] == 2:
            if outline != 0:
                outline += 2


        shape_color = (0, 0, 0)
        if self.card_num[2] == 0:
            shape_color = self.blue
        if self.card_num[2] == 1:
            shape_color = self.red
        if self.card_num[2] == 2:
            shape_color = self.green

        positions = []
        if self.card_num[0] == 0:
            positions = [(self.position[0] + 143, self.position[1] + 87.5 - 65)]
        if self.card_num[0] == 1:
            positions = [(self.position[0] + 143 + 40, self.position[1] + 87 - 65),
                         (self.position[0] + 143 - 40, self.position[1] + 87 - 65)]
        if self.card_num[0] == 2:
            positions = [(self.position[0] + 143, self.position[1] + 87 - 65),
                         (self.position[0] + 143 + 80, self.position[1] + 87 - 65),
                         (self.position[0] + 143 - 80, self.position[1] + 87 - 65)]

        for position in positions:
            step = 7
            thickness = 2
            if self.card_num[3] == 0:
                circle = pygame.Rect(position[0] - 30, position[1], 60, 120)
                pygame.draw.rect(screen, shape_color, circle, outline, 10000)
                if lines:
                    pygame.draw.line(screen, shape_color, (position[0] - 12, int(position[1]+7)), (position[0] + 12, int(position[1]+7)), thickness)
                    for y in range(int(position[1]+14), int(position[1]+120-14), step):
                        pygame.draw.line(screen, shape_color, (position[0] - 25, int(y)), (position[0] + 25, int(y)), thickness)
                    pygame.draw.line(screen, shape_color, (position[0] - 12, int(position[1])+120-9), (position[0] + 12, int(position[1])+120-9), thickness)
            if self.card_num[3] == 1:
                x = position[0]
                y = position[1] - 5
                pygame.draw.polygon(screen, shape_color, ((x, y), (x + 30, y + 60), (x, y + 120), (x - 30, y + 60)),
                                    outline)
                if lines:
                    for y in range(int(position[1]), int(position[1] + 60), step):
                        length = (y-position[1]+5) / 2
                        pygame.draw.line(screen, shape_color, (position[0] - length, int(y)), (position[0] + length, int(y)),
                                         thickness)
                    for y in range(int(position[1]+56), int(position[1] + 112), step):
                        length = (60 - ((y-position[1]+5) / 2))
                        pygame.draw.line(screen, shape_color, (position[0] - length, int(y)), (position[0] + length, int(y)),
                                         thickness)
            if self.card_num[3] == 2:

                x = position[0] - 10
                y = position[1] - 5
                change = 25
                pygame.draw.polygon(screen, shape_color,
                                    (
                                        (x, y), (x - change, y + change), (x, y + 2 * change),
                                        (x - change, y + 3 * change),
                                        (x + change, y + 5 * change), (x + 2 * change, y + 4 * change),
                                        (x + change, y + 3 * change), (x + 2 * change, y + 2 * change)
                                    ),
                                    outline)
                if lines:
                    # for y in range(int(position[1]), int(position[1] + 120), step):
                    #     pygame.draw.line(screen, shape_color, (position[0] - 30, int(y)), (position[0] + 30, int(y)),
                    #                      thickness)
                    for y in range(int(position[1]), int(position[1] + change), step):
                        length = (y-position[1]+5)-1
                        pygame.draw.line(screen, shape_color, (position[0]-10 - length, int(y)), (position[0] -10 + length, int(y)),
                                         thickness)
                    for y in range(int(position[1]+21), int(position[1] + 48), step):
                        pygame.draw.line(screen, shape_color, (position[0]-50+(y-(position[1]+5)), int(y)), (position[0]-50+(y-(position[1]+5))+2*change, int(y)),
                                     thickness)
                    for y in range(int(position[1] + 49), int(position[1] + 71), step):
                        pygame.draw.line(screen, shape_color, (position[0] - (y - position[1]-35), int(y)),
                                         (position[0] - (y - position[1]-35) + 2 * change, int(y)),
                                         thickness)
                    for y in range(int(position[1]+70), int(position[1] + 98), step):
                        pygame.draw.line(screen, shape_color, (position[0]-50+(y-(position[1]+5))-50, int(y)), (position[0]-50+(y-(position[1]+5))+2*change-50, int(y)),
                                     thickness)
                    print()
                    for y in range(int(position[1])+99, int(position[1])+120, step):
                        length = (y - position[1]-106)
                        pygame.draw.line(screen, shape_color, (position[0]+ length, int(y)), (position[0] + 27 - length, int(y)),
                                         thickness)

# pygame.draw.polygon(screen, shape_color,
#                     ((x, y), (x - 20, y + 20), (x, y + 40), (x, y + 100), (x + 20, y + 120),
#                      (x + 40, y + 100), (x + 20, y + 80), (x + 20, y + 20)),
#                     outline)


#  card_0 = pygame.Rect(80, 80, 300, 175)
#  card_1 = pygame.Rect(460, 80, 300, 175)
#  card_2 = pygame.Rect(840, 80, 300, 175)
#  card_3 = pygame.Rect(80, 295, 300, 175)
#  card_4 = pygame.Rect(460, 295, 300, 175)
#  card_5 = pygame.Rect(840, 295, 300, 175)
#  card_6 = pygame.Rect(80, 510, 300, 175)
#  card_7 = pygame.Rect(460, 510, 300, 175)
#  card_8 = pygame.Rect(840, 510, 300, 175)
#  card_9 = pygame.Rect(80, 725, 300, 175)
# card_10 = pygame.Rect(460, 725, 300, 175)
# card_11 = pygame.Rect(840, 725, 300, 175)
#  rect_outlines = [card_0, card_1, card_2, card_3, card_4,
#                   card_5, card_6, card_7, card_8, card_9,
#                   card_10, card_11]
