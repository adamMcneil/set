import pygame
import Deck
import Board
import Button
import Meun
import Computer
import time

screenHeight = 1000
# 1000
screenWidth = 1200
# 1200
white = (255, 255, 255)
blue = (50, 50, 255)
display = 'meun'
set_getter_start_time = 0

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
difficulty = 0

deck = Deck.Deck()
board = Board.Board()
com = Computer.Computer(difficulty)
meun = Meun.Meun()

freeplay_button = Button.DisplayButton('freeplay', [600, 400], 50, 'Free Play')
verse_button = Button.DisplayButton('versus', [600, 475], 50, 'Versus')
computer_button = Button.DisplayButton('computer', [600, 550], 50, 'Computer')

meun.add_button(computer_button)
meun.add_button(freeplay_button)
meun.add_button(verse_button)

for x in range(0, 10):
    difficulty_button = Button.DifficultyButton(x, [377 + x * 50, 625], 30, str(x))
    meun.add_button(difficulty_button)

for x in range(0, 12):
    deck.add_card_to_board()

meun.print_meun(screen)
pygame.display.update()
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    if display == 'meun':
        meun.print_meun(screen)
        for button in meun.button_list_change_display:
            display = button.check_if_button_is_pushed(events, display, deck, board)
            board.board_start_time = time.time()
        for button in meun.button_list_difficulty:
            if button.check_if_button_is_pushed_difficulty(events, com):
                for second_button in meun.button_list_difficulty:
                    second_button.highlight_correct_button(com)
                meun.print_meun(screen)
                pygame.display.update()
    elif display == 'freeplay':
        board.print_board(screen, deck)
        for card in deck.cards_in_play:
            card.select_Card(events, deck)
            card.print_Card(screen)
            card.print_shapes(screen)
        if deck.check_for_set(board, screen):
            deck.add_card_to_board()
            deck.add_card_to_board()
            deck.add_card_to_board()
            set_getter_start_time = time.time()
        deck.print_cards_left(screen)

        if time.time() - set_getter_start_time < .5:
            image = pygame.image.load('set_getter.svg')
            screen.blit(image, (0, 0))

        deck.print_num_of_sets(screen)
        board.print_player_one_score(screen)
        for button in board.button_list:
            display = button.check_if_button_is_pushed(events, display, deck, board)
    elif display == 'versus':
        board.print_board(screen, deck)
        for card in deck.cards_in_play:
            card.select_Card(events, deck)
            card.select_Card_with_keys(events, deck)
            card.print_Card(screen)
            card.print_shapes(screen)
        if deck.check_for_set(board, screen):
            deck.add_card_to_board()
            deck.add_card_to_board()
            deck.add_card_to_board()
            set_getter_start_time = time.time()

        if deck.check_for_set_second(board, screen):
            deck.add_card_to_board()
            deck.add_card_to_board()
            deck.add_card_to_board()
            set_getter_start_time = time.time()

        if time.time() - set_getter_start_time < .5:
            image = pygame.image.load('set_getter.svg')
            screen.blit(image, (0, 0))
        deck.print_cards_left(screen)
        deck.print_num_of_sets(screen)
        board.print_player_one_score(screen)
        board.print_player_two_score(screen)
        for button in board.button_list:
            display = button.check_if_button_is_pushed(events, display, deck, board)
    elif display == 'computer':
        board.print_board(screen, deck)
        for card in deck.cards_in_play:
            card.select_Card(events, deck)
            card.print_Card(screen)
            card.print_shapes(screen)
        com.claim_set(deck)
        deck.check_slots()
        if deck.check_for_set(board, screen):
            deck.add_card_to_board()
            deck.add_card_to_board()
            deck.add_card_to_board()
            set_getter_start_time = time.time()


        if deck.check_for_set_second(board, screen):
            deck.add_card_to_board()
            deck.add_card_to_board()
            deck.add_card_to_board()
            set_getter_start_time = time.time()

        if time.time() - set_getter_start_time < .5:
            image = pygame.image.load('set_getter.svg')
            screen.blit(image, (0, 0))
        deck.print_cards_left(screen)
        deck.print_num_of_sets(screen)
        board.print_player_one_score(screen)
        board.print_computer_score(screen)
        for button in board.button_list:
            display = button.check_if_button_is_pushed(events, display, deck, board)
    # print(display)
    pygame.display.update()
