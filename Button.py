import pygame


def line_up_text(button):
    x = button.position[0] + button.font_size / 8
    y = button.position[1] + button.font_size / 16
    return x, y


def reset(button, deck, board):
    if button.name == 'meun':
        deck.reset_deck()
        board.reset_board()


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
        self.button_color = background_color
        self.text_color = text_color
        self.shape = pygame.Rect(position[0] - 10, position[1], self.width, self.height)

    def print_button(self, screen):
        pygame.draw.rect(screen, self.button_color, self.shape, 0, 5)
        text_obj = self.font_obj.render(self.text, True, self.text_color)
        screen.blit(text_obj, line_up_text(self))


class DisplayButton(Button):

    def __init__(self, name, position, font_size, text, background_color=(0, 0, 0), text_color=(255, 255, 255)):
        Button.__init__(self, name, position, font_size, text, background_color, text_color)

    def check_if_button_is_pushed(self, events, display, deck, board):
        if self.name == "meun":
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        display = self.name
                        reset(self, deck, board)

        collide = self.shape.collidepoint(pygame.mouse.get_pos())
        if collide:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.name != 'no switch':
                        display = self.name
                        reset(self, deck, board)
        return display


class DifficultyButton(Button):

    def __init__(self, name, position, font_size, text, background_color=(255, 255, 255), text_color=(0, 0, 0),
                 background_color_two=(255, 255, 175)):
        Button.__init__(self, name, position, font_size, text, background_color, text_color)
        self.background_color_two = background_color_two

    def check_if_button_is_pushed_difficulty(self, events, difficulty):
        collide = self.shape.collidepoint(pygame.mouse.get_pos())
        if collide:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    difficulty = self.name
        if self.name == difficulty:
            self.button_color = self.background_color_two
        else:
            self.button_color = self.background_color
        return difficulty

