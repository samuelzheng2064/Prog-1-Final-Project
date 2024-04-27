import random
import math


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    def get_board(self):
        return self.board

    def valid_in_row(self, row, num):
        if num not in self.board[row]:
            return True
        else:
            return False

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        for row in range(3):  # creates a length of 3 rows
            for col in range(3):  # creates three columns in each one of those rows
                if self.board[row_start + row][
                    col_start + col] == num:  # checks if the number is equal for each part of the 3x3 array
                    return False
        return True  # returns true if it does not exist in the array

    def is_valid(self, row, col, num):
        row_starty = row - row % 3
        col_starty = col - col % 3
        return self.valid_in_row(row, num) & self.valid_in_col(col, num) & self.valid_in_box(row_starty, col_starty,
                                                                                             num)

    def fill_box(self, row_start, col_start):
        nums_to_fill = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Creates the list of numbers that need to fill a box
        random.shuffle(nums_to_fill)  # randomizes the list to be put into a box
        for row in range(3):
            for col in range(3):
                self.board[row_start + row][col_start + col] = nums_to_fill[-1]  # fills the box
                nums_to_fill = nums_to_fill[:-1]  # removes the number from the list

    def fill_diagonal(self):
        for i in range(0, 9,
                       3):  # iterates through 0, 3, and 6 (Note: The board goes to index (8,8) since 0 is included)
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # Given on github
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        removed = []  # List to store already removed cells
        for i in range(self.removed_cells):
            while True:  # keeps generating numbers until a new cell has been reached
                row = random.randint(0, 8)  # selects a row to change
                col = random.randint(0, 8)  # selects a column to change

                if (row, col) not in removed:
                    removed.append((row, col))
                    break  # stops the generation of cells
            self.board[row][col] = 0


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board