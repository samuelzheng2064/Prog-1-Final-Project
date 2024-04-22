import pygame
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.create_board()
        self.selected_cell = None
        self.sketched_value = None

    def create_board(self):
        # Create a 2D list to represent the Sudoku board
        board = [[Cell(row, col, self.screen) for col in range(9)] for row in range(9)]
        return board

    def draw(self):
        # Draw the Sudoku grid and all cells on the board
        for row in range(9):
            for col in range(9):
                self.board[row][col].draw()
        self.draw_grid()

    def draw_grid(self):
        # Draw the grid lines and boxes
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (i * self.width // 10, 0),
                                 (i * self.width // 10, 9 * self.height // 10), 4)
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height // 10),
                                 (9 * self.width // 10, i * self.height // 10), 4)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), (i * self.width // 10, 0),
                                 (i * self.width // 10, 9 * self.height // 10))
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height // 10),
                                 (9 * self.width // 10, i * self.height // 10))

    def select(self, row, col):
        # Select a cell on the board
        self.selected_cell = (row, col)

    def click(self, x, y):
        # Check if a cell was clicked and return its coordinates
        for row in range(9):
            for col in range(9):
                if self.board[row][col].is_clicked(x, y):
                    return (row, col)
        return None

    def clear(self):
        # Clear the selected cell's value and sketched value
        if self.selected_cell is not None:
            self.board[self.selected_cell[0]][self.selected_cell[1]].clear()
            self.sketched_value = None

    def sketch(self, value):
        # Sketch a value in the selected cell
        if self.selected_cell is not None:
            self.board[self.selected_cell[0]][self.selected_cell[1]].sketch(value)
            self.sketched_value = value

    def place_number(self, value):
        # Place a number in the selected cell
        if self.selected_cell is not None:
            self.board[self.selected_cell[0]][self.selected_cell[1]].place_number(value)
            self.sketched_value = None

    def reset_to_original(self):
        # Reset all cells to their original values
        for row in range(9):
            for col in range(9):
                self.board[row][col].reset_to_original()

    def is_full(self):
        # Check if all cells have a value
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        # Update the underlying 2D board with the values in all cells
        self.board = [[self.board[row][col].value for col in range(9)] for row in range(9)]

