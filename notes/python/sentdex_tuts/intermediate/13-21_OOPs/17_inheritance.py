# Inheritance in OOP python

'''
' More modularity
'
' The class being inherited from is called super/base/parent class
' and the class inheriting it is the child or sub class
'
' Inheriting takes all the methods from the parent class
'
' We can overwrite parent class methods in the child class and super() lets
' us dynamically refer to the base class. Here is a great talk on super() by
' Raymond Hettinger: https://www.youtube.com/watch?v=EiOglTERPEo
'''

import pygame
import random
from blob import Blob # import class Blob


STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255) 
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World") 
clock = pygame.time.Clock()


# Inheriting from Blocb class
class BlueBlob(Blob):

    # Overwriting the __init__ method
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        
        # We can also do this, will need to pass "self" now
        # not good when doing multiple inheritance
        # Blob.__init__(self, color, x_boundary, y_boundary)

        self.color = BLUE

    def move_fast(self):
        self.x += random.randrange(-7,7)
        self.y += random.randrange(-7,7)


def draw_environment(blob_list):
    game_display.fill(WHITE)
    
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move_fast()
            blob.check_bounds()

    pygame.display.update() 


def main():
    blue_blobs = dict(enumerate([BlueBlob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([BlueBlob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs])
        clock.tick(60) 

if __name__ == "__main__":
    main()
