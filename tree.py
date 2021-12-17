import pygame
import os
import winsound
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (-1800,50) #sets game window position on screen
pygame.init()  #sets up pygame
pygame.display.set_caption("tree")  # sets the window title
screen = pygame.display.set_mode((1200, 800))  # creates game screen
screen.fill((0,0,0)) #wipe screen black

#tree function definition--------------------------------------------------------------------
def tree(xpos, ypos, width, height, level):
    if level<11:

        pygame.draw.line(screen, (250, 250-level*25, level*25), (xpos, ypos), (int(xpos-width), int(ypos-height)),21-level*2) #left branch
        pygame.draw.line(screen, (level*25, 250-level*25, 250), (xpos, ypos), (int(xpos+width), int(ypos-height)),21-level*2) #right branch
        winsound.Beep(level*100, 50)
        pygame.display.flip()
        level+=1
        #recursive function calls:
        tree(xpos+width, ypos-height, width*.75, height*.75, level)
        tree(xpos-width, ypos-height, width*.75, height*.75, level)

    else:
        return 0

#main function---------------------------------------------------------------------------------
for i in range(9):
    tree(600, 800, 150, 200, 1)
pygame.time.delay(1000)
    
    
print("goodbye")
    
