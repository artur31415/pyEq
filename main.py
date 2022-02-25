import pygame

from equation import Equation
from slot import Slot


pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode([width, height])

running = True

squareSize = 50
offsetX = 50
offsetY = 50
offset_position = (offsetX, offsetY)

myEquation = Equation((3, 3))

boardSlots = []


for i in range(8):
    rowSlots = []
    for j in range(8):
        colorIndex = (i + j) % 2
        squareColor = (0, 0, 0)

        if colorIndex != 0:
            squareColor = (255, 0, 255)

        rowSlots.append(Slot((i, j), squareColor))
    boardSlots.append(rowSlots)


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

            if myEquation.get_rect_with_pos(squareSize, offset_position).collidepoint(pos):
                myEquation.is_selected = True
                print("myEquation selected!")
            else:
                slot_grid_pos = None
                for i in range(len(boardSlots)):
                    for j in range(len(boardSlots[0])):
                        if boardSlots[i][j].get_rect_with_pos(squareSize, offset_position).collidepoint(pos):
                            slot_grid_pos = (i, j)
                            print("grid (", str(i), ", ", str(j), ") selected!")
                            break
                    if slot_grid_pos != None:
                        break
                if slot_grid_pos != None and myEquation.is_selected:
                    if myEquation.can_move_to(slot_grid_pos):
                        myEquation.grid_position = slot_grid_pos
                    else:
                        print("Cannot move to ", str(slot_grid_pos))
                myEquation.is_selected = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for i in range(len(boardSlots)):
        for j in range(len(boardSlots[0])):
            boardSlots[i][j].draw(screen, (offsetX, offsetY), squareSize)

    myEquation.draw(screen, (offsetX, offsetY), squareSize)

    if myEquation.is_selected:
        myEquation.draw_walk_pattern(screen, (offsetX, offsetY), squareSize)

    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()