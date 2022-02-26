import pygame
from random import *


from equation import Equation
from ore import Ore
from slot import Slot


pygame.init()
pygame.font.init()

# seed random number generator
seed(1)
################################################################################################
#                                           VARIABLES
################################################################################################
width = 500
height = 500

screen = pygame.display.set_mode([width, height])

myfont = pygame.font.SysFont('Comic Sans MS', 20)

running = True

squareSize = 50
offsetX = 50
offsetY = 50
offset_position = (offsetX, offsetY)

my_init_position = (3, 3)

myEquation = Equation(my_init_position)

boardSlots = []

ores = []

myGold = 0

################################################################################################
#                                           FUNCTIONS
################################################################################################
def get_ore_index_by_grid(grid_position):
    for x in range(len(ores)):
        if ores[x].grid_position == grid_position:
            return x
    return -1

def init_board():
    for i in range(8):
        rowSlots = []
        for j in range(8):
            colorIndex = (i + j) % 2
            squareColor = (0, 0, 0)

            if colorIndex != 0:
                squareColor = (255, 0, 255)

            rowSlots.append(Slot((i, j), squareColor))
        boardSlots.append(rowSlots)

def generate_ores(num_of_ores):
    ores.clear()
    for j in range(num_of_ores):
        new_grid_pos = (randint(0, 7), randint(0, 7))
        while (True):
            is_valid = True
            for ore in ores:
                if ore.grid_position == new_grid_pos:
                    is_valid = False
                    break
            
            if is_valid:
                if myEquation.grid_position != new_grid_pos:
                    break
            new_grid_pos = (randint(0, 7), randint(0, 7))

        ores.append(Ore(new_grid_pos, randint(1, 5)))

def reset_game(num_of_ores):
    myEquation.grid_position = my_init_position
    generate_ores(num_of_ores)
################################################################################################
#                                           MAIN LOOP
################################################################################################

init_board()
reset_game(randint(5, 10))

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
                        #CHECK IF THERE IS AN ORE HERE!
                        slot_ore_index = get_ore_index_by_grid(slot_grid_pos)
                        if slot_ore_index != -1:
                            myGold += ores[slot_ore_index].to_gold()
                            ores.pop(slot_ore_index)
                            
                        myEquation.grid_position = slot_grid_pos
                    else:
                        print("Cannot move to ", str(slot_grid_pos))
                myEquation.is_selected = False


    if len(ores) == 0:
        reset_game(randint(5, 10))

    ##################################################################
    # DRAW CODE
    ##################################################################
    # Fill the background with white
    screen.fill((255, 255, 255))

    for i in range(len(boardSlots)):
        for j in range(len(boardSlots[0])):
            boardSlots[i][j].draw(screen, (offsetX, offsetY), squareSize)

    myEquation.draw(screen, (offsetX, offsetY), squareSize)

    if myEquation.is_selected:
        myEquation.draw_walk_pattern(screen, (offsetX, offsetY), squareSize)

    for ore in ores:
        ore.draw(screen, (offsetX, offsetY), squareSize)


    textsurface = myfont.render('Gold = ' + str(myGold), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    ##################################################################
    # Flip the display
    ##################################################################
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()