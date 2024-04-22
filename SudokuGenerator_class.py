import random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.fill_values()

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return True
        return False

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return True
        return False

    def valid_in_box(self, row_start, col_start, num):
        for row in range(3):
            for col in range(3):
                if self.board[row + row_start][col + col_start] == num:
                    return True
        return False

    def is_valid(self, row, col, num):
        return not (self.valid_in_row(row, num) or self.valid_in_col(col, num)
                    or self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        unused_numbers = [x for x in range(1, self.row_length + 1)]
        for row in range(3):
            for col in range(3):
                while True:
                    random_num = random.choice(unused_numbers)
                    if self.is_valid(row + row_start, col + col_start, random_num):
                        self.board[row + row_start][col + col_start] = random_num
                        unused_numbers.remove(random_num)
                        break

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if row == self.row_length - 1 and col == self.row_length:
            return True
        if col == self.row_length:
            row += 1
            col = 0
        if self.board[row][col] > 0:
            return self.fill_remaining(row, col + 1)
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
        self.board[row][col] = 0
        return False

    def fill_values(self):
        self.board = [[0 for _ in range(self.row_length)] for _ in range(self.row_length)]
        self.fill_diagonal()
        self.fill_remaining(0, 0)
        return self.board

    def remove_cells(self):
        for _ in range(self.removed_cells):
            row, col = random.randint(0, self.row_length - 1), random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0


def generate_sudoku(size, removed):
    if size != 9 or removed < 0 or removed > 50:
        raise ValueError("Invalid input")
    generator = SudokuGenerator(size, removed)
    generator.remove_cells()
    return generator.get_board()
