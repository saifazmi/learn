# Creating an environment for the object

'''
' Just setting up the pygame environment for the purposes of OOPs demo
' this is not a PyGame tutorial
'''

import pygame
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255) # rgb values
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT)) # window size
pygame.display.set_caption("Blob World") # title
clock = pygame.time.Clock() # for managing FPS


class Blob:
    
    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8) # radius
        self.color = color

    def move(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH

        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT


def draw_environment(blob):
    game_display.fill(WHITE) # draw in the background
    pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
    pygame.display.update() # sends everything to the screen
    blob.move()

def main():
    red_blob = Blob(RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(red_blob)
        clock.tick(60) # capping @ 60 FPS
        print(red_blob.x, red_blob.y)

if __name__ == "__main__":
    main()
