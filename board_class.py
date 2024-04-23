import pygame
from cell_class import (Cell)
from SudokuGenerator_class import SudokuGenerator
import copy

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sol_board = copy.deepcopy(sudoku.get_board())  # created variable copy needed since this doesn't return solved list
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, sol_board

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        if difficulty == 'easy':  #
            self.og_board, self.sol_board = generate_sudoku(9,
                                                            30)  # gathers both solved board and user interative board    elif difficulty == 'medium':
            self.og_board, self.sol_board = generate_sudoku(9, 40)
        elif difficulty == 'hard':
            self.og_board, self.sol_board = generate_sudoku(9, 50)
        self.cells = [[Cell(self.og_board[row][col], row, col, screen) for col in range(9)] for row in range(9)]
        self.selected = None

    # def create_board(self):
    #     # Create a 2D list to represent the Sudoku board
    #     board = [[Cell(row, col, self.screen) for col in range(9)] for row in range(9)]
    #     return board

    def draw(self):
        # Draw the Sudoku grid and all cells on the board
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()
        for i in range(10):  # draws lines
            if i % 3 == 0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 40), (360, i * 40), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 40, 0), (i * 40, 360), thick)

    # def draw_grid(self):
    #     # Draw the grid lines and boxes
    #     for i in range(10):
    #         if i % 3 == 0:
    #             pygame.draw.line(self.screen, (0, 0, 0), (i * self.width // 10, 0),
    #                              (i * self.width // 10, 9 * self.height // 10), 4)
    #             pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height // 10),
    #                              (9 * self.width // 10, i * self.height // 10), 4)
    #         else:
    #             pygame.draw.line(self.screen, (0, 0, 0), (i * self.width // 10, 0),
    #                              (i * self.width // 10, 9 * self.height // 10))
    #             pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.height // 10),
    #                              (9 * self.width // 10, i * self.height // 10))

    def select(self, row, col):
        # Select a cell on the board
        self.selected_cell = (row, col)

    def click(self, x, y):
        cell_size = self.width // 9
        if 0 <= x < self.width and 0 <= y < self.height:
            col = x // cell_size
            row = y // cell_size
            return row, col
        else:
            return None

    def clear(self):
        # Clear the selected cell's value and sketched value
        if self.selected:
            row, col = self.selected
            if self.og_board[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
            else:
                return False

    def clear(self):  # clears input value
        if self.selected:
            row, col = self.selected
            if self.og_board[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
            else:
                return False

    def sketch(self, value):  # sets and displays sketched value
        if self.selected:
            row, col = self.selected
            if self.og_board[row][col] == 0:
                self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):  # sets number
        if self.selected:
            row, col = self.selected
            if self.og_board[row][col] == 0:
                self.cells[row][col].set_cell_value(value)

    def reset_to_original(self):  # resets to original boardd
        if self.og_board:
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].set_cell_value(self.og_board[i][j])

    def is_full(self):  # finds if board is full
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):  # updates user input board
        for row in range(9):
            for col in range(9):
                self.og_board[row][col] = self.cells[row][col].value

    def find_empty(self):  # finds empty cells
        for row in range(9):
            for col in range(9):
                if self.og_board[row][col] == 0:
                    return row, col
        return None

    def check_board(self):  # checks solved board against user input
        if self.sol_board != self.og_board:  # checks solved board against original board
            return False
        else:
            return True

    def check_valid(self, row, col, num):  # checks valid number
        return self.valid_row(row, num) and self.valid_col(col, num) and self.valid_box(row - row % 3, col - col % 3,
                                                                                        num)

    def valid_row(self, row, num):  # checks valid row
        for col in range(9):
            if self.cells[row][col].value == num:
                return True
        return False

    def valid_col(self, col, num):  # checks valid col
        for row in range(9):
            if self.cells[row][col].value == num:
                return True
        return False

    def valid_box(self, row_start, col_start, num):  # checks valid box
        for row in range(3):
            for col in range(3):
                if self.cells[row + row_start][col + col_start].value == num:
                    return True
        return False

    # def sketch(self, value):
    #     # Sketch a value in the selected cell
    #     if self.selected_cell is not None:
    #         self.board[self.selected_cell[0]][self.selected_cell[1]].sketch(value)
    #         self.sketched_value = value
    #
    # def place_number(self, value):
    #     # Place a number in the selected cell
    #     if self.selected_cell is not None:
    #         self.board[self.selected_cell[0]][self.selected_cell[1]].place_number(value)
    #         self.sketched_value = None
    #
    # def reset_to_original(self):
    #     # Reset all cells to their original values
    #     for row in range(9):
    #         for col in range(9):
    #             self.board[row][col].reset_to_original()
    #
    # def is_full(self):
    #     # Check if all cells have a value
    #     for row in range(9):
    #         for col in range(9):
    #             if self.board[row][col].value == 0:
    #                 return False
    #     return True
    #
    # def update_board(self):
    #     # Update the underlying 2D board with the values in all cells
    #     self.board = [[self.board[row][col].value for col in range(9)] for row in range(9)]

