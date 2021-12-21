import pygame


def line_up_text(button):
    x = button.position[0] + button.font_size / 4
    y = button.position[1] + button.font_size / 12
    return x, y


def reset(button, deck, board):
    if button.name == 'meun':
        deck.reset_deck()
        board.reset_board()


class Button:
    is_pushed = False
    on_mouse = False
    size_change = 5

    def __init__(self, name, position, font_size, text, background_color=(0, 0, 0), text_color=(255, 255, 255), copy=True):
        position_copy = []
        for x in position:
            position_copy.append(x)
        self.name = name
        self.position = position
        self.font_size = font_size
        self.text = text
        self.background_color = background_color
        self.button_color = background_color
        self.text_color = text_color

        self.font_obj = pygame.font.Font('freesansbold.ttf', font_size)
        self.text_obj = self.font_obj.render(self.text, True, self.text_color)

        self.position[0] = position[0] - self.font_obj.size(text)[0] / 2

        self.width = self.font_obj.size(text)[0] + font_size / 2
        self.height = self.font_obj.size(text)[1]

        self.shape = pygame.Rect(position[0], position[1], self.width, self.height)
        if copy:
            self.second_button = Button(name, position_copy, font_size+5, text, background_color, text_color, copy=False)



    def print_button(self, screen):
        if self.on_mouse:
            pygame.draw.rect(screen, self.second_button.button_color, self.second_button.shape, 0, 5)
            screen.blit(self.second_button.text_obj, line_up_text(self.second_button))
        else:
            pygame.draw.rect(screen, self.button_color, self.shape, 0, 5)
            screen.blit(self.text_obj, line_up_text(self))


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
            self.on_mouse = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.name != 'no switch':
                        display = self.name
                        reset(self, deck, board)
        else:
            self.on_mouse = False
        return display


class DifficultyButton(Button):

    def __init__(self, name, position, font_size, text, background_color=(255, 255, 255), text_color=(0, 0, 0),
                 background_color_two=(255, 221, 85)):
        Button.__init__(self, name, position, font_size, text, background_color, text_color)
        self.background_color_two = background_color_two

    def check_if_button_is_pushed_difficulty(self, events, computer):
        output = False
        collide = self.shape.collidepoint(pygame.mouse.get_pos())
        if collide:
            self.on_mouse = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    computer.difficulty = self.name
                    output = True
        else:
            self.on_mouse = False

        if self.name == computer.difficulty:
            self.button_color = self.background_color_two
        else:
            self.button_color = self.background_color
        self.highlight_correct_button(computer)
        return output

    def highlight_correct_button(self, computer):
        if self.name == computer.difficulty:
            self.button_color = self.background_color_two
            self.second_button.button_color = self.background_color_two
        else:
            self.button_color = self.background_color
            self.second_button.button_color = self.background_color


