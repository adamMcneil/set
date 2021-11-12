import pygame
import Deck
import Board
import Button
import Meun

screenHeight = 1000
screenWidth = 1200
white = (255, 255, 255)
blue = (50, 50, 255)
display = 'meun'

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
freeplay_button = Button.Button('freeplay', [600, 250], 50, 'Free Play')
verse_button = Button.Button('verse', [600, 325], 50, 'Verse')
meun = Meun.Meun()
meun.add_button(freeplay_button)
meun.add_button(verse_button)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if display == 'meun':
        meun.print_meun(screen)
        for button in meun.button_list:
            button.print_button(screen)
            display = button.check_if_button_is_pushed(events, display, deck, board)
    if display == 'freeplay':
        board.print_board(screen)
        for card in deck.cards_in_play:
            card.select_Card(events, deck)
            card.print_Card(screen)
            card.print_shapes(screen)
        deck.check_slots()
        deck.add_card_to_board()
        deck.check_for_set(board)
        deck.print_cards_left(screen)
        deck.print_num_of_sets(screen)
        board.print_player_one_score(screen)
        for button in board.button_list:
            button.print_button(screen)
            display = button.check_if_button_is_pushed(events, display, deck, board)
    if display == 'verse':
        board.print_board(screen)
        for card in deck.cards_in_play:
            card.select_Card(events, deck)
            card.select_Card_with_keys(events, deck)
            card.print_Card(screen)
            card.print_shapes(screen)
        deck.check_slots()
        deck.add_card_to_board()
        deck.check_for_set(board)
        deck.check_for_set_second(board)
        deck.print_cards_left(screen)
        deck.print_num_of_sets(screen)
        board.print_player_one_score(screen)
        board.print_player_two_score(screen)

        for button in board.button_list:
            button.print_button(screen)
            display = button.check_if_button_is_pushed(events, display, deck, board)
    # print(display)
    pygame.display.update()
