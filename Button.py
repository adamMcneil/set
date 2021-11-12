import pygame


def line_up_text(button):
    x = button.position[0] + button.font_size / 8
    y = button.position[1] + button.font_size / 16
    return x, y


class Button:
    is_pushed = False

    def __init__(self, name, position, font_size, text, background_color=(0, 0, 0), text_color=(255, 255, 255)):
        self.name = name
        self.font_obj = pygame.font.Font('freesansbold.ttf', font_size)
        self.position = position
        self.position[0] = position[0] - self.font_obj.size(text)[0] / 2
        self.width = self.font_obj.size(text)[0] + font_size / 4 + 20
        self.height = font_size
        if name == 'meun':
            self.height += 8
        self.font_size = font_size
        self.text = text
        self.background_color = background_color
        self.text_color = text_color
        self.shape = pygame.Rect(position[0]-10, position[1], self.width, self.height)

    def print_button(self, screen):
        pygame.draw.rect(screen, self.background_color, self.shape, 0, 5)
        text_obj = self.font_obj.render(self.text, True, self.text_color)
        screen.blit(text_obj, line_up_text(self))

    def check_if_button_is_pushed(self, events, display, deck, board):
        collide = self.shape.collidepoint(pygame.mouse.get_pos())
        if collide:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    display = self.name
                    self.reset(deck, board)
        return display

    def reset(self, deck, board):
        if self.name == 'meun':
            deck.reset_deck()
            board.reset_board()
