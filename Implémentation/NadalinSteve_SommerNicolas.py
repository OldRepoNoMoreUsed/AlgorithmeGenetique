import pygame
import sys
from pygame.locals import KEYDOWN, MOUSEBUTTONDOWN

def drawWindow():
    listeCity = set()
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
                listeCity.add(pygame.mouse.get_pos())
                pygame.display.flip()
            elif event.type == KEYDOWN:
                return screen, listeCity
    pygame.display.flip()

def drawPath(positions, screen):
    #for position in positions:
    #    pygame.draw.circle(screen, (255, 0, 0), position, 5)
    #    pygame.display.flip()
    print("Affichage chemin")

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
        screen, liste = drawWindow()
    else:
        readFile(File)
    drawPath(liste, screen)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ga_solve(File=sys.argv[1], gui=False, maxTime=0)
    else:
        ga_solve(maxTime=0)
