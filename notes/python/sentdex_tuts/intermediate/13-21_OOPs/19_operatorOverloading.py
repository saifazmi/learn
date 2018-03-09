# Operator Overloading

'''
' All of the operators can be overloaded from assignment to comparison & calc
'
' Here we are overloading "+" operator
'''

import pygame
import random
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 5

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


'''
' STORY TIME :)
'
' The Blue blobs are the main character in this story and they can be damaged
' by Red blobs :( BUT Green blobs can heal Blue blobs :D
'''


class BlueBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    # Overloading the addition operator
    def __add__(self, other_blob):

        '''
        ' If red blob deals damage first to blue and then the remaining blue
        ' deals damage to red, this can end up adding to the size of red if
        ' blue is too small
        '''
        if other_blob.color == (255, 0, 0):  # RED
            self.size -= other_blob.size # red deals damage to blue blob
            other_blob.size -= self.size # blue deals damage to red blob
            
        elif other_blob.color == (0, 255, 0):  # GREEN
            self.size += other_blob.size # Heals or size++ for blue blobs
            other_blob.size = 0

        elif other_blob.color == (0, 0, 255):  # BLUE
            pass  # do nothing when interacting with other blue blobs

        else:
            raise Exception("Tried to combine or multiple blobs of unsupported colors.")


class RedBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)


class GreenBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)
        

def draw_environment(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    

def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

    # Observe the change in size
    print("Blue blob size: {} red size: {}".format(blue_blobs[0].size, red_blobs[0].size))
    blue_blobs[0] + red_blobs[0]
    print("Blue blob size: {} red size: {}".format(blue_blobs[0].size, red_blobs[0].size))
    
##    while True:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##
##        draw_environment([blue_blobs,red_blobs,green_blobs])
##        clock.tick(60)

if __name__ == '__main__':
    main()
