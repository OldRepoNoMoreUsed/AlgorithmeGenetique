import pygame
import sys
from pygame.locals import KEYDOWN, MOUSEBUTTONDOWN

def drawWindow():
    RED = (255, 0, 0)
    (width, height) = (1800, 900)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Probleme du voyageur de commerce')
    font = pygame.font.Font(None, 30)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, RED, pygame.mouse.get_pos(), 5)
                print(pygame.mouse.get_pos())
                pygame.display.flip()
    pygame.display.flip()


def onClick(event):
    cx = event.xdata
    cy = event.ydata
    print(cy + " " + cx)

def readFile(File):
    with open(File) as f:
        for line in f:
            print(line)


def ga_solve(File=None, gui=True, maxTime=0):
    if(gui is True):
        drawWindow()
    else:
        readFile(File)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ga_solve(File=sys.argv[1], gui=False, maxTime=0)
    else:
        ga_solve(maxTime=0)
