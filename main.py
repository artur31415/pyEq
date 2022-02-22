import pygame

from equation import Equation


pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode([width, height])

running = True

squareSize = 50
offsetX = 50
offsetY = 50

myEquation = Equation((0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("pressed A")
            elif event.key == pygame.K_d:
                print("pressed D")

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            

        
    # Fill the background with white
    screen.fill((255, 255, 255))

    for i in range(8):
        for j in range(8):
            colorIndex = (i + j) % 2
            squareColor = (0, 0, 0)

            if colorIndex != 0:
                squareColor = (255, 0, 255)

            pygame.draw.rect(screen, squareColor, (offsetX + squareSize * i, offsetY + squareSize * j, squareSize, squareSize))


            


            myEquation.draw(screen, (offsetX, offsetY), squareSize)

    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()