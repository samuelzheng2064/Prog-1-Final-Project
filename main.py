import sys
import pygame
from board_class import Board

def draw_highlight(current_board, selected_cell, screen):
    row, col = selected_cell
    cell_highlight = pygame.Rect((col + 2) * current_board.CELL_SIZE, (row + 1) * current_board.CELL_SIZE,
                                 current_board.CELL_SIZE, current_board.CELL_SIZE)
    current_board.draw()
    pygame.draw.rect(screen, "red", cell_highlight, 5)

def win_screen(screen):
    #font for buttons
    default_font = pygame.font.Font(None, 40)

    #Sets background
    screen.fill("white")
    screen.blit(pygame.image.load("background.webp"), [0, 0])

    #win text
    win_font = pygame.font.Font("minecraft-font/MinecraftRegular-Bmg3.otf", 80)
    win_text = win_font.render("You Win!!! :)", 0, "black")

    #win background
    win_rect = pygame.Rect.copy(win_text.get_rect())
    win_rect.width += 20
    win_rect.height += 20
    win_rect.top = screen.get_height() / 2 - win_text.get_rect().height / 2 - 10
    win_rect.left = screen.get_width() / 2 - win_text.get_rect().width / 2 - 10

    #prints win text
    pygame.draw.rect(screen, "white", win_rect)
    pygame.draw.rect(screen, "black", win_rect, 5)
    screen.blit(win_text, (screen.get_width() / 2 - win_text.get_rect().width / 2, screen.get_height() / 2 - win_text.get_rect().height / 2))

    #exit button
    exit_button = pygame.Rect(230, 475, 140, 50)
    pygame.draw.rect(screen, "white", exit_button, 0, int(exit_button.height / 2))
    pygame.draw.rect(screen, "black", exit_button, 1, int(exit_button.height / 2))
    exit_text = default_font.render("EXIT", 0, "black")
    screen.blit(exit_text, (268, 488))

def lose_screen(screen):
    #font for buttons
    default_font = pygame.font.Font(None, 40)

    #Sets background
    screen.fill("white")
    screen.blit(pygame.image.load("background.webp"), [0, 0])

    #lose text
    lose_font = pygame.font.Font("minecraft-font/MinecraftRegular-Bmg3.otf", 80)
    lose_text = lose_font.render("You Lose :(", 0, "black")

    #lose background
    lose_rect = pygame.Rect.copy(lose_text.get_rect())
    lose_rect.width += 20
    lose_rect.height += 20
    lose_rect.top = screen.get_height() / 2 - lose_text.get_rect().height / 2 - 10
    lose_rect.left = screen.get_width() / 2 - lose_text.get_rect().width / 2 - 10

    #prints lose text and background
    pygame.draw.rect(screen, "white", lose_rect)
    pygame.draw.rect(screen, "black", lose_rect, 5)
    screen.blit(lose_text, (screen.get_width() / 2 - lose_text.get_rect().width / 2, screen.get_height() / 2 - lose_text.get_rect().height / 2))

    #restart button
    restart_button = pygame.Rect(230, 475, 140, 50)
    pygame.draw.rect(screen, "white", restart_button, 0, int(restart_button.height / 2))
    pygame.draw.rect(screen, "black", restart_button, 1, int(restart_button.height / 2))
    restart_text = default_font.render("RESTART", 0, "black")
    screen.blit(restart_text, (237, 488))

def main():
    # setup for pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")

    # variables
    menu = True
    board = False
    running = True
    row = 0
    col = 0
    endwin = False
    endlose = False

    # main game loop
    while running:
        if menu:
            # MENU
            # font for buttons
            font = pygame.font.Font(None, 40)

            # Sets background
            screen.fill("white")
            screen.blit(pygame.image.load("background.webp"), [0, 0])

            # title text
            title_font = pygame.font.Font("minecraft-font/MinecraftRegular-Bmg3.otf", 120)
            title_text = title_font.render("Sudoku", 0, "black")

            # title background
            title_background = pygame.Rect.copy(title_text.get_rect())
            title_background.width = 460
            title_background.center = (300, 100)

            # draws title
            pygame.draw.rect(screen, "white", title_background)
            pygame.draw.rect(screen, "black", title_background, 3)
            screen.blit(title_text, (97, 50))

            # instruction
            instruction_text = font.render("Choose Your Difficulty:", 0, "black")
            screen.blit(instruction_text, (143, 340))

            # menu buttons' position and size
            easy_button = pygame.Rect(50, 400, 140, 50)
            medium_button = pygame.Rect.copy(easy_button)
            medium_button.centerx = 300
            hard_button = pygame.Rect.copy(easy_button)
            hard_button.centerx = 480
            exit_button = pygame.Rect.copy(easy_button)
            exit_button.center = (300, 500)

            buttons = [easy_button, medium_button, hard_button, exit_button]

            # draws border and fill based on button data above
            for button in buttons:
                pygame.draw.rect(screen, "white", button, 0, int(button.height / 2))
                pygame.draw.rect(screen, "black", button, 1, int(button.height / 2))

            # shows text on each button
            easy_text = font.render("EASY", 0, "black")
            screen.blit(easy_text, (83, 413))

            medium_text = font.render("MEDIUM", 0, "black")
            screen.blit(medium_text, (246, 413))

            hard_text = font.render("HARD", 0, "black")
            screen.blit(hard_text, (440, 413))

            exit_text = font.render("EXIT", 0, "black")
            screen.blit(exit_text, (267, 488))

        if board:
            # resets screen
            screen.fill("white")
            screen.blit(pygame.image.load("background.webp"), [0, 0])

            # draw board
            current_board = Board(500, 500, screen, difficulty)
            current_board.draw()

            # button data
            reset_button = pygame.Rect(50, 500, 140, 50)
            restart_button = pygame.Rect.copy(reset_button)
            restart_button.centerx = 300
            exit_button = pygame.Rect.copy(reset_button)
            exit_button.centerx = 480

            buttons = [reset_button, restart_button, exit_button]

            # draws border and fill based on button data above
            for button in buttons:
                pygame.draw.rect(screen, "white", button, 0, int(button.height / 2))
                pygame.draw.rect(screen, "black", button, 1, int(button.height / 2))

            # shows text on each button
            # font for buttons
            font = pygame.font.Font(None, 40)

            # button text
            reset_text = font.render("RESET", 0, "black")
            screen.blit(reset_text, (75, 513))

            restart_text = font.render("RESTART", 0, "black")
            screen.blit(restart_text, (236, 513))

            exit_text = font.render("EXIT", 0, "black")
            screen.blit(exit_text, (448, 513))

            # Making text and background rectangle for difficulty at top
            difficulty_text = font.render(difficulty, 0, "black")
            difficulty_rect = pygame.Rect.copy(difficulty_text.get_rect())
            difficulty_rect.width += 4
            difficulty_rect.height += 4
            difficulty_rect.top = screen.get_height() / 30 - 2
            difficulty_rect.left = screen.get_width() / 2 - difficulty_text.get_rect().width / 2 - 2

            # printing difficulty text and background rectangle
            pygame.draw.rect(screen, "white", difficulty_rect)
            pygame.draw.rect(screen, "black", difficulty_rect, 1)
            screen.blit(difficulty_text,(screen.get_width() / 2 - difficulty_text.get_rect().width / 2, screen.get_height() / 30))
            # stop drawing the board again
            board = False

        for event in pygame.event.get():

            # shuts program down if user exits the game
            if event.type == pygame.QUIT:
                running = False

            # checks for click on menu, game, and win/lose screen respectively
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if menu:
                    # Checks each button
                    if easy_button.collidepoint(event.pos):
                        menu = False
                        board = True
                        difficulty = "Easy"
                    if medium_button.collidepoint(event.pos):
                        menu = False
                        board = True
                        difficulty = "Medium"
                    if hard_button.collidepoint(event.pos):
                        menu = False
                        board = True
                        difficulty = "Hard"
                    if exit_button.collidepoint(event.pos):
                        running = False
                elif endwin:
                    if 475 < y < 525 and 230 <= x <= 370:
                        pygame.quit()
                        sys.exit()
                elif endlose:
                    if restart_button.collidepoint(event.pos):
                        menu = True
                        endlose = False
                elif not menu:
                    if reset_button.collidepoint(event.pos):
                        current_board.reset_to_original()
                        current_board.draw()
                    elif restart_button.collidepoint(event.pos):
                        menu = True
                    elif exit_button.collidepoint(event.pos):
                        running = False
                    elif current_board.click(x,y):
                        row, col = current_board.click(x,y)
                        row, col = int(row), int(col)
                        current_board.select(row, col)
                        draw_highlight(current_board, current_board.selected, screen)

                pygame.display.flip()

            if event.type == pygame.KEYDOWN and current_board and current_board.selected and running:
                if current_board.selected:
                    if event.key in [pygame.K_LEFT, pygame.K_a, pygame.K_RIGHT, pygame.K_d, pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s]:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            if current_board.selected[0] > 1:
                                row, col = current_board.selected
                                current_board.select(row - 1, col)
                                draw_highlight(current_board, current_board.selected, screen)
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if current_board.selected[0] < 9:
                                row, col = current_board.selected
                                current_board.select(row + 1, col)
                                draw_highlight(current_board, current_board.selected, screen)
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if current_board.selected[1] > 1:
                                row, col = current_board.selected
                                current_board.select(row, col - 1)
                                draw_highlight(current_board, current_board.selected, screen)
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if current_board.selected[1] < 9:
                                row, col = current_board.selected
                                current_board.select(row, col + 1)
                                draw_highlight(current_board, current_board.selected, screen)

                    elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                        current_board.sketch(event.unicode)
                        draw_highlight(current_board, current_board.selected, screen)
                    elif event.key == pygame.K_BACKSPACE:
                        current_board.sketch(0)
                        current_board.place_number()
                        draw_highlight(current_board, current_board.selected, screen)
                    elif event.key == pygame.K_RETURN:
                        current_board.place_number()
                        current_board.sketch(0)
                        draw_highlight(current_board, current_board.selected, screen)
                        if current_board.is_full():
                            screen.fill("white")
                            screen.blit(pygame.image.load("background.webp"), [0, 0])
                            if current_board.check_board():
                                win_screen(screen)
                                endwin = True
                            else:
                                lose_screen(screen)
                                endlose = True

        pygame.display.flip()
if __name__ == "__main__":
    main()