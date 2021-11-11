import pygame
import Deck
import Board

screenHeight = 1000
screenWidth = 1200
white = (255, 255, 255)
blue = (50, 50, 255)

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

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((screenWidth, screenHeight))

deck = Deck.Deck()
board = Board.Board()

running = True
while running:
    screen.fill(blue)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    board.print_board(screen)
    for card in deck.cards_in_play:
        card.select_Card(events, deck)
        card.print_Card(screen)
        card.print_shapes(screen)
    deck.check_slots()
    deck.add_card_to_board()
    deck.check_for_set()
    deck.print_cards_left(screen)
    deck.print_num_of_sets(screen)
    # print(deck.num_of_sets_in_play())

    pygame.display.update()
