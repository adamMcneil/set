import time

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



class Computer:

    start_time = 0

    def __init__(self, difficulty):
        self.difficulty = 9 - difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty


    def get_calculated_time(self):
        return self.difficulty

    def find_a_set(self, deck):
        for x in range(0, len(deck.cards_in_play)-2):
            for y in range(x+1, len(deck.cards_in_play)-1):
                for z in range(y+1, len(deck.cards_in_play)):
                    set = [deck.cards_in_play[x], deck.cards_in_play[y], deck.cards_in_play[z]]
                    if SET(set):
                        for card in set:
                            deck.add_card_second_highlight(card)
                        self.start_time = 0
                        return

    def claim_set(self, deck):
        if self.start_time == 0:
            self.start_time = time.time()
            # print(self.start_time)
        current_time = time.time()
        print(current_time-self.start_time)
        if current_time - self.start_time > self.get_calculated_time():
            self.find_a_set(deck)
