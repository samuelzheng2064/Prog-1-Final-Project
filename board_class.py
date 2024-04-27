import pygame
from cell_class import Cell
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
    CELL_SIZE = 40
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.selected = False
        if difficulty == 'Easy':
            self.og_board, self.sol_board = generate_sudoku(9, 30)  # gathers both solved board and user interative board
        elif difficulty == 'Medium':
            self.og_board, self.sol_board = generate_sudoku(9, 40)
        elif difficulty == 'Hard':
            self.og_board, self.sol_board = generate_sudoku(9, 50)
        self.cells = [[Cell(self.og_board[row][col], row, col, screen, self.CELL_SIZE) for col in range(9)] for row in range(9)]

        self.left_of_board = self.screen.get_width() / 2 - ((len(self.cells) / 2) * self.CELL_SIZE)
        self.right_of_board = self.screen.get_width() / 2 + ((len(self.cells) / 2) * self.CELL_SIZE)
        self.top_of_board = self.screen.get_width() / 2 - ((len(self.cells) / 2) * self.CELL_SIZE) - self.CELL_SIZE
        self.bottom_of_board = self.screen.get_width() / 2 + ((len(self.cells) / 2) * self.CELL_SIZE) - self.CELL_SIZE

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

            # i'm sorry for the confusing stuff here, but it sets the screen to the center with a little bit at the top - Matt
            pygame.draw.line(self.screen, (0, 0, 0), (self.screen.get_width() / 2 - ((len(self.cells) / 2) * 40), i * 40 + (len(self.cells) / 3 * 40) - 40), (self.screen.get_width() / 2 + ((len(self.cells) / 2) * 40), i * 40 + (len(self.cells) / 3 * 40) - 40), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * 40 + (len(self.cells) / 3 * 40), self.screen.get_width() / 2 - ((len(self.cells) / 2) * 40) - 40), (i * 40 + (len(self.cells) / 3 * 40), self.screen.get_width() / 2 + ((len(self.cells) / 2) * 40) - 40), thick)

    def select(self, row, col):
        # Select a cell on the board
        self.selected = (row, col)

    def click(self, x, y):
        if self.left_of_board <= x < self.right_of_board and self.top_of_board <= y < self.bottom_of_board:
            col = x // self.CELL_SIZE - 2
            row = y // self.CELL_SIZE - 1
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

    def sketch(self, value):  # sets and displays sketched value
        if self.selected:
            row, col = self.selected
            row -= 1
            col -= 1
            if self.og_board[row][col] == 0:
                self.cells[row][col].set_sketched_value(value)

    def place_number(self, value=0):  # sets number
        if self.selected:
            row, col = self.selected
            row -= 1
            col -= 1
            if self.og_board[row][col] == 0:
                value = self.cells[row][col].sketched_value
                self.cells[row][col].set_cell_value(value)

    def reset_to_original(self):  # resets to original board
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].set_sketched_value(0)
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
        for row in range(9):
            for col in range(9):
                if self.sol_board[row][col] != self.cells[row][col].value:
                    return False
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

