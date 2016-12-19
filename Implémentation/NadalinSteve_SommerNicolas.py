import pygame
import sys
import time
from pygame.locals import KEYDOWN, MOUSEBUTTONDOWN


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addName(self, name):
        self.name = name


def initScreen():
        (width, height) = (1800, 900)
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Probleme du voyageur de commerce')
        font = pygame.font.Font(None, 30)
        return screen

def drawWindow(screen):
    listeCity = set()
    RED = (255, 0, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, RED, pygame.mouse.get_pos(), 5)
                x, y = pygame.mouse.get_pos()
                point = Point(x, y)
                listeCity.add(point)      #add city
                pygame.display.flip()
            elif event.type == KEYDOWN:
                return listeCity
    pygame.display.flip()

def drawCity(positions, screen):
    for position in positions:
        pygame.draw.circle(screen, (255, 0, 0), (int(position.x), int(position.y)), 5)
        pygame.display.flip()
        time.sleep(1)

def drawPath(positions, screen):
    print("Affichage chemin")
    pygame.display.flip()
    time.sleep(2)


def readFile(File):
    liste = set()
    with open(File) as f:
        for line in f:
            tab = line.split()
            point = Point(tab[1], tab[2])
            liste.add(point)
    return liste


def ga_solve(File=None, gui=True, maxTime=0):
    screen = initScreen()
    if(gui is True):
        liste = drawWindow(screen)
    else:
        liste = readFile(File)
        drawCity(liste, screen)
    time.sleep(5)
    drawPath(liste, screen)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ga_solve(File=sys.argv[1], gui=False, maxTime=0)
    else:
        ga_solve(maxTime=0)
