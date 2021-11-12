import pygame
import Card

def SET(cards):
    if len(cards) == 3:
        total1 = 0
        total2 = 0
        total3 = 0
        total4 = 0
        for card in cards:
            total1 += card.card_num[0]
            total2 += card.card_num[1]
            total3 += card.card_num[2]
            total4 += card.card_num[3]
        if total1 % 3 == 0 and total2 % 3 == 0 and total3 % 3 == 0 and total4 % 3 == 0:
            return True
    return False



class Deck:
    black = (0,0,0)
    cards_in_deck = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 2],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 2],
        [0, 0, 2, 0],
        [0, 0, 2, 1],
        [0, 0, 2, 2],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 0, 2],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 2],
        [0, 1, 2, 0],
        [0, 1, 2, 1],
        [0, 1, 2, 2],
        [0, 2, 0, 0],
        [0, 2, 0, 1],
        [0, 2, 0, 2],
        [0, 2, 1, 0],
        [0, 2, 1, 1],
        [0, 2, 1, 2],
        [0, 2, 2, 0],
        [0, 2, 2, 1],
        [0, 2, 2, 2],

        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 2],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 0, 1, 2],
        [1, 0, 2, 0],
        [1, 0, 2, 1],
        [1, 0, 2, 2],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 2],
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 1, 2, 0],
        [1, 1, 2, 1],
        [1, 1, 2, 2],
        [1, 2, 0, 0],
        [1, 2, 0, 1],
        [1, 2, 0, 2],
        [1, 2, 1, 0],
        [1, 2, 1, 1],
        [1, 2, 1, 2],
        [1, 2, 2, 0],
        [1, 2, 2, 1],
        [1, 2, 2, 2],

        [2, 0, 0, 0],
        [2, 0, 0, 1],
        [2, 0, 0, 2],
        [2, 0, 1, 0],
        [2, 0, 1, 1],
        [2, 0, 1, 2],
        [2, 0, 2, 0],
        [2, 0, 2, 1],
        [2, 0, 2, 2],
        [2, 1, 0, 0],
        [2, 1, 0, 1],
        [2, 1, 0, 2],
        [2, 1, 1, 0],
        [2, 1, 1, 1],
        [2, 1, 1, 2],
        [2, 1, 2, 0],
        [2, 1, 2, 1],
        [2, 1, 2, 2],
        [2, 2, 0, 0],
        [2, 2, 0, 1],
        [2, 2, 0, 2],
        [2, 2, 1, 0],
        [2, 2, 1, 1],
        [2, 2, 1, 2],
        [2, 2, 2, 0],
        [2, 2, 2, 1],
        [2, 2, 2, 2]

    ]
    cards_in_play = []
    cards_highlighted = []
    card_second_highlighted = []
    slots_open = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def __init__(self):
        pass

    def add_card_deck(self, card):
        self.cards_in_deck.append(card.card_num)

    def remove_card_deck(self, card):
        self.cards_in_deck.remove(card.card_num)

    def add_card_play(self, card):
        self.cards_in_play.append(card)

    def remove_card_play(self, card):
        self.cards_in_play.remove(card)

    def add_card_highlight(self, card):
        self.cards_highlighted.append(card)
        card.is_highlighted = True

    def remove_card_highlight(self, card):
        self.cards_highlighted.remove(card)
        card.is_highlighted = False

    def add_card_second_highlight(self, card):
        self.card_second_highlighted.append(card)
        card.is_second_highlighted = True

    def remove_card_second_highlight(self, card):
        self.card_second_highlighted.remove(card)
        card.is_second_highlighted = False

    def add_card_to_board(self):
        self.check_slots()
        if len(self.slots_open) > 0:
            x = self.slots_open[0]
            if len(self.cards_in_deck) > 0:
                card = Card.Card(x, self)
                while self.num_of_sets_in_play() == 0 and len(self.slots_open) < 2:
                    self.add_card_deck(card)
                    self.remove_card_play(card)
                    card = Card.Card(x, self)
        print('len of slots:', len(self.slots_open))
        print('len of deck:', len(self.cards_in_deck))
        print(self.cards_in_deck)
        if len(self.slots_open) > len(self.cards_in_deck) > 0:
            card = Card.Card(x, self)
            print('here')

        # x = random.randint(0, len(deck.cards_in_deck) - 1)
        #         self.card_num = deck.cards_in_deck[x]

    def check_slots(self):
        print()
        self.slots_open = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        if len(self.cards_in_play) > 0:
            for card in self.cards_in_play:
                if card.slot in self.slots_open:
                    self.slots_open.remove(card.slot)

    def check_for_set(self, board):
        if len(self.cards_highlighted) == 3:
            if SET(self.cards_highlighted):
                board.player_one_score += '←'
                for cardH in self.cards_highlighted:
                    for cardP in self.cards_in_play:
                        if cardH == cardP:
                            self.cards_in_play.remove(cardP)
                            break
            for card in self.cards_highlighted[:]:
                self.remove_card_highlight(card)

    def check_for_set_second(self, board):
        if len(self.card_second_highlighted) == 3:
            if SET(self.card_second_highlighted):
                board.player_two_score += '←'
                for cardH in self.card_second_highlighted:
                    for cardP in self.cards_in_play:
                        if cardH == cardP:
                            self.cards_in_play.remove(cardP)
                            break
            for card in self.card_second_highlighted[:]:
                self.remove_card_second_highlight(card)

    def num_of_sets_in_play(self):
        total = 0
        for x in range(0, len(self.cards_in_play)-2):
            for y in range(x+1, len(self.cards_in_play)-1):
                for z in range(y+1, len(self.cards_in_play)):
                    cards = [self.cards_in_play[x], self.cards_in_play[y], self.cards_in_play[z]]
                    if SET(cards):
                        total += 1
        return total

    def print_cards_left(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render(str(len(self.cards_in_deck + self.cards_in_play)) + ' / 81', True, self.black)
        screen.blit(text_obj, (1100, 950))

    def print_num_of_sets(self, screen):
        font_obj = pygame.font.Font('freesansbold.ttf', 30)
        text_obj = font_obj.render(str(self.num_of_sets_in_play()), True, self.black)
        screen.blit(text_obj, (1050, 950))

    def reset_deck(self):
        self.cards_in_deck = [
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 2],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 2],
            [0, 0, 2, 0],
            [0, 0, 2, 1],
            [0, 0, 2, 2],
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 0, 2],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 1, 1, 2],
            [0, 1, 2, 0],
            [0, 1, 2, 1],
            [0, 1, 2, 2],
            [0, 2, 0, 0],
            [0, 2, 0, 1],
            [0, 2, 0, 2],
            [0, 2, 1, 0],
            [0, 2, 1, 1],
            [0, 2, 1, 2],
            [0, 2, 2, 0],
            [0, 2, 2, 1],
            [0, 2, 2, 2],
            [1, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 2],
            [1, 0, 1, 0],
            [1, 0, 1, 1],
            [1, 0, 1, 2],
            [1, 0, 2, 0],
            [1, 0, 2, 1],
            [1, 0, 2, 2],
            [1, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 2],
            [1, 1, 1, 0],
            [1, 1, 1, 1],
            [1, 1, 1, 2],
            [1, 1, 2, 0],
            [1, 1, 2, 1],
            [1, 1, 2, 2],
            [1, 2, 0, 0],
            [1, 2, 0, 1],
            [1, 2, 0, 2],
            [1, 2, 1, 0],
            [1, 2, 1, 1],
            [1, 2, 1, 2],
            [1, 2, 2, 0],
            [1, 2, 2, 1],
            [1, 2, 2, 2],
            [2, 0, 0, 0],
            [2, 0, 0, 1],
            [2, 0, 0, 2],
            [2, 0, 1, 0],
            [2, 0, 1, 1],
            [2, 0, 1, 2],
            [2, 0, 2, 0],
            [2, 0, 2, 1],
            [2, 0, 2, 2],
            [2, 1, 0, 0],
            [2, 1, 0, 1],
            [2, 1, 0, 2],
            [2, 1, 1, 0],
            [2, 1, 1, 1],
            [2, 1, 1, 2],
            [2, 1, 2, 0],
            [2, 1, 2, 1],
            [2, 1, 2, 2],
            [2, 2, 0, 0],
            [2, 2, 0, 1],
            [2, 2, 0, 2],
            [2, 2, 1, 0],
            [2, 2, 1, 1],
            [2, 2, 1, 2],
            [2, 2, 2, 0],
            [2, 2, 2, 1],
            [2, 2, 2, 2]

        ]
        self.cards_in_play = []
        self.cards_highlighted = []
        self.slots_open = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def SET_tester(self, board):
        for x in range(0, len(self.cards_in_play) - 2):
            for y in range(x + 1, len(self.cards_in_play) - 1):
                for z in range(y + 1, len(self.cards_in_play)):
                    cards = [self.cards_in_play[x], self.cards_in_play[y], self.cards_in_play[z]]
                    if SET(cards):
                        for card in cards:
                            self.add_card_second_highlight(card)
                        board.computer_score += '←'
                        return


