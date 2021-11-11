import pygame
import main
import Deck


class Computer:

    def __init__(self):
        pass

    def find_a_set(self, cards):
        total = 0
        for x in range(0, len(cards)-2):
            for y in range(x+1, len(cards)-1):
                for z in range(y+1, len(cards)):
                    set = [cards[x], cards[y], cards[z]]
                    if main.SET(set):
                        return set

    def claim_set(self, deck):
        pass