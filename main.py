import sys
import pygame
from board_class import Board

def menu_screen(screen):
    #font for buttons
    default_font = pygame.font.Font(None, 40)

    #Sets background
    screen.fill("white")
    screen.blit(pygame.image.load("background.webp"), [0, 0])

    #TITLE
    ###############################################################################################
    #title text
    title_font = pygame.font.Font("minecraft-font/MinecraftRegular-Bmg3.otf", 120)
    title_text = title_font.render("Sudoku", 0, "black")

    #title background
    title_background = pygame.Rect.copy(title_text.get_rect())
    title_background.width = 460
    title_background.center = (300, 100)

    #draws title
    pygame.draw.rect(screen, "white", title_background)
    pygame.draw.rect(screen, "black", title_background, 3)
    screen.blit(title_text, (97, 50))

    #INSTRUCTIONS
    ###############################################################################################
    instruction_text = default_font.render("Choose Your Difficulty:", 0, "black")
    screen.blit(instruction_text, (143, 340))

    #BUTTONS
    ###############################################################################################
    #menu buttons' position and size
    easy_button = pygame.Rect(50, 400, 140, 50)
    medium_button = pygame.Rect.copy(easy_button)
    medium_button.centerx = 300
    hard_button = pygame.Rect.copy(easy_button)
    hard_button.centerx = 480
    exit_button = pygame.Rect.copy(easy_button)
    exit_button.center = (300, 500)

    buttons = [easy_button, medium_button, hard_button, exit_button]

    #draws border and fill based on button data above
    for button in buttons:
        pygame.draw.rect(screen, "white", button, 0, int(button.height / 2))
        pygame.draw.rect(screen, "black", button, 1, int(button.height / 2))

    #shows text on each button
    easy_text = default_font.render("EASY", 0, "black")
    screen.blit(easy_text, (83, 413))

    medium_text = default_font.render("MEDIUM", 0, "black")
    screen.blit(medium_text, (246, 413))

    hard_text = default_font.render("HARD", 0, "black")
    screen.blit(hard_text, (440, 413))

    exit_text = default_font.render("EXIT", 0, "black")
    screen.blit(exit_text, (267, 488))

def board_screen(screen, difficulty):
    #resets screen
    screen.fill("white")
    screen.blit(pygame.image.load("background.webp"), [0, 0])

    #draw board
    current_board = Board(500, 500, screen, difficulty)
    current_board.draw()

    #button data
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
    default_font = pygame.font.Font(None, 40)

    #button text
    reset_text = default_font.render("RESET", 0, "black")
    screen.blit(reset_text, (75, 513))

    restart_text = default_font.render("RESTART", 0, "black")
    screen.blit(restart_text, (236, 513))

    exit_text = default_font.render("EXIT", 0, "black")
    screen.blit(exit_text, (448, 513))

    #Making text and background rectangle for difficulty at top
    difficulty_text = default_font.render(difficulty, 0, "black")
    difficulty_rect = pygame.Rect.copy(difficulty_text.get_rect())
    difficulty_rect.width += 4
    difficulty_rect.height += 4
    difficulty_rect.top = screen.get_height() / 30 - 2
    difficulty_rect.left = screen.get_width() / 2 - difficulty_text.get_rect().width / 2 - 2

    #printing difficulty text and background rectangle
    pygame.draw.rect(screen, "white", difficulty_rect)
    pygame.draw.rect(screen, "black", difficulty_rect, 1)
    screen.blit(difficulty_text, (screen.get_width() / 2 - difficulty_text.get_rect().width / 2, screen.get_height() / 30))

def main():
    # setup for pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")

    # menu buttons + title
    menu_screen(screen)
    menu = True
    board = False
    running = True

    # main game loop
    while running:
        #checks for exit
        for event in pygame.event.get():
            #shuts program down if user exits the game
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            #checks for click on menu, game, and win/lose screen respectively
            if event.type == pygame.MOUSEBUTTONDOWN and running:
                x, y = event.pos
                if menu:
                    #Checks top row of buttons click
                    if 400 <= y <= 450:
                        #easy button
                        if 50 <= x <= 190:
                            board_screen(screen, "Easy")
                            menu = False
                            board = True
                        #medium button
                        elif 230 <= x <= 370:
                            board_screen(screen, "Medium")
                            menu = False
                            board = True
                        #hard button
                        elif 410 <= x <= 550:
                            board_screen(screen, "Hard")
                            menu = False
                            board = True
                    #Checks for exit button click
                    if 475 <= y <= 525 and 230 <= x <= 370:
                        pygame.quit()
                        sys.exit()
                elif board:
                    if 500 < y < 550:
                        #reset button
                        if 50 <= x <= 190:
                            print()
                        #restart button
                        elif 230 <= x <= 370:
                            menu_screen(screen)
                            menu = True
                            board = False
                        #exit button
                        elif 410 <= x <= 550:
                            pygame.quit()
                            sys.exit()
                else:
                    print()


        #updates screen
        pygame.display.flip()

if __name__ == "__main__":
    main()