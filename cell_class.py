import pygame


class Cell:
    # constructor
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = int(value)  # uses integer to compare

    def set_sketched_value(self, value):
        self.sketched_value = value

    # function is assuming a screen of 360 x 420
    def draw(self):

        x_pos, y_pos = 40 * self.col, 40 * self.row

        pygame.draw.rect(self.screen, (173, 216, 230), (x_pos, y_pos, 40, 40))

        # draws number in rectangle
        if self.value != 0:
            text_surface = pygame.font.Font(None, 24).render(str(self.value), True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(x_pos + 20, y_pos + 20))
            self.screen.blit(text_surface, text_rect)
        # draws user inputted number in rectangle
        if self.sketched_value != 0:
            text_surface = pygame.font.Font(None, 15).render(str(self.sketched_value), True, (128, 128, 128))
            text_rect = text_surface.get_rect(center=(x_pos + 10, y_pos + 10))
            self.screen.blit(text_surface, text_rect)