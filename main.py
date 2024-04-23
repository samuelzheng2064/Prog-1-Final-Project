import sys
import pygame
from board_class import Board
import SudokuGenerator_class

def menu_screen(surface):

    #font for buttons
    default_font = pygame.font.Font(None, 40)

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
    pygame.draw.rect(surface, "white", title_background)
    pygame.draw.rect(surface, "black", title_background, 3)
    surface.blit(title_text, (97, 50))

    #INSTRUCTIONS
    ###############################################################################################
    instruction_text = default_font.render("Choose Your Difficulty:", 0, "black")
    surface.blit(instruction_text, (143, 340))

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
        pygame.draw.rect(surface, "white", button, 0, int(button.height / 2))
        pygame.draw.rect(surface, "black", button, 1, int(button.height / 2))

    #shows text on each button
    easy_text = default_font.render("EASY", 0, "black")
    surface.blit(easy_text, (83, 413))

    medium_text = default_font.render("MEDIUM", 0, "black")
    surface.blit(medium_text, (246, 413))

    hard_text = default_font.render("HARD", 0, "black")
    surface.blit(hard_text, (440, 413))

    exit_text = default_font.render("EXIT", 0, "black")
    surface.blit(exit_text, (267, 488))

def main():
    # setup for pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")

    # sets the background
    screen.fill("white")
    screen.blit(pygame.image.load("background.webp"), [0, 0])

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
                if menu:
                    x, y = event.pos
                    if 400 <= y <= 450:
                        if 50 <= x <= 190:
                            screen.fill("white")
                            screen.blit(pygame.image.load("background.webp"), [0, 0])
                            current_board = Board(500, 500, screen, "easy")
                            current_board.draw()
                            menu = False
                            board = True
                        elif 230 <= x <= 370:
                            screen.fill("white")
                            screen.blit(pygame.image.load("background.webp"), [0, 0])
                            current_board = Board(450, 450, screen, "medium")
                            menu = False
                            board = True
                        elif 410 <= x <= 550:
                            screen.fill("white")
                            screen.blit(pygame.image.load("background.webp"), [0, 0])
                            current_board = Board(450, 450, screen, "hard")
                            menu = False
                            board = True
                    if 475 <= y <= 525 and 230 <= x <= 370:
                        pygame.quit()
                        sys.exit()

                elif board:
                    print()
                else:
                    print()


        #updates screen
        pygame.display.flip()

if __name__ == "__main__":
    main()