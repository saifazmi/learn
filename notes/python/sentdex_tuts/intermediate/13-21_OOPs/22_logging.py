# Loggin in python

import pygame
import random
from blob import Blob
import numpy as np

'''
' Logging is important for debugging and making sure that program is working as
' expected, we can either print to console or saved a log file.
' Python offers level of logging
'
' DEBUG: Detailed information, typically of interest only when diagnosing problems.
' INFO:	 Confirmation that things are working as expected.
' WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
' ERROR: Due to a more serious problem, the software has not been able to perform some function.
' CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
'
' Loggin is most useful on things like web-server which running headless and we
' are not continously watching the output stream, like this we can periodically check
' to see if things are running as expected and in case of a crash figure out what
' went wrong
'''

import logging

#logging.basicConfig(level=logging.INFO) # setting logging lvl
# No output to a console, append to a log file
logging.basicConfig(filename="logfile.log", level=logging.INFO) # defining a log file

STARTING_BLUE_BLOBS = 30
STARTING_RED_BLOBS = 30
STARTING_GREEN_BLOBS = 30

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        # INFO level logging
        logging.info("Blob add op {} + {}".format(str(self.color), str(other_blob.color)))
        if other_blob.color == (255, 0, 0): 
            self.size -= other_blob.size 
            other_blob.size -= self.size 
            
        elif other_blob.color == (0, 255, 0): 
            self.size += other_blob.size 
            other_blob.size = 0

        elif other_blob.color == (0, 0, 255): 
            pass

        else:
            raise Exception("Tried to combine or multiple blobs of unsupported colors.")


class RedBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)


class GreenBlob(Blob):
    
    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)
        

def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)

def handle_collisions(blob_list):
    blues, reds, greens = blob_list # unpacking the list of blob dictionaries
    for blue_id, blue_blob in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                # DEBUG level logging
                logging.debug("Checking if blobs are touching {} + {}".format(str(blue_blob.color), str(other_blob.color)))
                if blue_blob == other_blob: # if we are checking the same set of blobs
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens
                        
        
def draw_environment(blob_list):
    blues, reds, greens = handle_collisions(blob_list)
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    return blues, reds, greens
    

def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            blues, reds, greens = draw_environment([blue_blobs,red_blobs,green_blobs])
            clock.tick(60)
        except Exception as e:
            # CRITICAL level logging
            logging.critical(str(e))
            pygame.quit()
            quit()
            break

if __name__ == '__main__':
    main()
