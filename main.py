import pygame
#from board_class import Board

def menu_buttons(surface):
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

    default_font = pygame.font.Font(None, 40)

    easy_text = default_font.render("EASY", 0, "black")
    surface.blit(easy_text, (83, 413))

    medium_text = default_font.render("MEDIUM", 0, "black")
    surface.blit(medium_text, (246, 413))

    hard_text = default_font.render("HARD", 0, "black")
    surface.blit(hard_text, (440, 413))

    exit_text = default_font.render("EXIT", 0, "black")
    surface.blit(exit_text, (267, 488))



#setup for pygame and screen
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
running = True

#main game loop
while running:
    #checks for exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #sets the background
    screen.fill("white")
    screen.blit(pygame.image.load("background.webp"), [0, 0])

    menu_buttons(screen)







    # flip() the display to put your work on screen
    pygame.display.flip()