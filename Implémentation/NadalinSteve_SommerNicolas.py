import pygame
import sys
import math
import random
from pygame.locals import KEYDOWN, MOUSEBUTTONDOWN


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addName(self, name):
        self.name = name

    def distanceBetweenPoints(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)


class IndividualManager:
    pointCircuit = []

    def addPoint(self, point):
        self.pointCircuit.append(point)

    def getPoint(self, index):
        return self.pointCircuit[index]

    def pointCount(self):
        return len(self.pointCircuit)


class Individual:
    def __init__(self, manager, individual=None):
        self.im = manager
        self.individual = []
        self.fitness = 0.0
        self.totalLength = 0

        if individual is not None:
            self.individual = individual
        else:
            for i in range(0, self.im.pointCount()):
                self.individual.append(None)

    def __len__(self):
        return len(self.individual)

    def generateIndividual(self):
        for i in range(0, self.im.pointCount()):
            self.setPoint(i, self.im.getPoint(i))
        random.shuffle(self.individual)

    def getPoint(self, pointIndex):
        return self.individual[pointIndex]

    def setPoint(self, pointIndex, point):
        self.individual[pointIndex] = point
        # self.fitness = 0.0
        # self.totalLength = 0

    def getFitness(self):
        # Astuce: On ne calcul la fitness qu'une seul fois pour economiser du temps de calcul
        if self.fitness == 0:
            self.fitness = 1/float(self.getTotalLength())
        return self.fitness

    def getTotalLength(self):
        if self.totalLength == 0:
            for i in range(0, self.getIndividualSize()):
                origin = self.getPoint(i)
                destination = None
                if i+1 < self.getIndividualSize():
                    destination = self.getPoint(i+1)
                else:
                    destination = self.getPoint(0)
                self.totalLength += origin.distanceBetweenPoints(destination)
        return self.totalLength

    def getIndividualSize(self):
        return len(self.individual)

    def contentPoint(self, point):
        return point in self.individual


class Population:
    def __init__(self, manager, populationSize, init):
        self.individuals = []
        for i in range(0, populationSize):
            self.individuals.append(None)

        if init:
            for i in range(0, populationSize):
                newIndividual = Individual(manager)
                newIndividual.generateIndividual()
                self.saveIndividual(i, newIndividual)

    def saveIndividual(self, index, individual):
        self.individuals[index] = individual

    def getIndividual(self, index):
        return self.individuals[index]

    def getFittest(self):
        fittest = self.individuals[0]
        for i in range(0, self.getPopulationSize()):
            if fittest.getFitness() <= self.getIndividual(i).getFitness():
                fittest = self.getIndividual(i)
            return fittest

    def getPopulationSize(self):
        return len(self.individuals)


class GeneticAlgorithm:
    def __init__(self, manager):
        self.manager = manager
        self.mutationRate = 0.2
        self.tournamentSize = 5
        self.elit = True

    def evolution(self, population):
        newPopulation = Population(self.manager, population.getPopulationSize(), False)
        elitOffset = 0
        if self.elit:
            newPopulation.saveIndividual(0, population.getFittest())
            elitOffset = 1

        for i in range(elitOffset, newPopulation.getPopulationSize()):
            mom = self.selection(population)
            dad = self.selection(population)
            child = self.crossover(mom, dad)
            newPopulation.saveIndividual(i, child)

        for i in range(elitOffset, newPopulation.getPopulationSize()):
            self.mutation(newPopulation.getIndividual(i))

        return newPopulation

    def selection(self, population):
        tournament = Population(self.manager, self.tournamentSize, False)
        for i in range(0, self.tournamentSize):
            randomIndex = int(random.random() * population.getPopulationSize())
            tournament.saveIndividual(i, population.getIndividual(randomIndex))
        fittest = tournament.getFittest()
        return fittest

    def crossover(self, mom, dad):
        child = Individual(self.manager)
        start = int(random.random() * mom.getIndividualSize())
        end = int(random.random() * mom.getIndividualSize())

        for i in range(0, child.getIndividualSize()):
            if start < end and i > start and i < end:
                child.setPoint(i, mom.getPoint(i))
            elif start > end:
                if not (i < start and i > end):
                    child.setPoint(i, mom.getPoint(i))

        for i in range(0, dad.getIndividualSize()):
            if not child.contentPoint(dad.getPoint(i)):
                for j in range(0, child.getIndividualSize()):
                    if child.getPoint(j) is None:
                        child.setPoint(j, dad.getPoint(i))
                        break
        return child

    def mutation(self, individual):
        for i in range(0, individual.getIndividualSize()):
            if random.random() < self.mutationRate:
                j = int(individual.getIndividualSize() * random.random())
                individual.setPoint(j, individual.getPoint(i))
                individual.setPoint(i, individual.getPoint(j))


# def initScreen():
#         (width, height) = (1800, 900)
#         pygame.init()
#         screen = pygame.display.set_mode((width, height))
#         pygame.display.set_caption('Probleme du voyageur de commerce')
#         font = pygame.font.Font(None, 30)
#         return screen
#
#
# def drawWindow(screen):
#     listeCity = set()
#     RED = (255, 0, 0)
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == MOUSEBUTTONDOWN:
#                 pygame.draw.circle(screen, RED, pygame.mouse.get_pos(), 5)
#                 x, y = pygame.mouse.get_pos()
#                 point = Point(x, y)
#                 listeCity.add(point)      #add city
#                 pygame.display.flip()
#             elif event.type == KEYDOWN:
#                 return listeCity
#     pygame.display.flip()
#
#
# def drawCity(positions, screen):
#     for position in positions:
#         pygame.draw.circle(screen, (255, 0, 0), (int(position.x), int(position.y)), 5)
#         pygame.display.flip()
#
#
# def drawPath(point1, point2, screen):
#     print("Affichage chemin")
#     pygame.display.flip()
#
#
# def readFile(File):
#     liste = set()
#     name = 0
#     with open(File) as f:
#         for line in f:
#             tab = line.split()
#             point = Point(int(tab[1]), int(tab[2]))
#             point.addName(name)
#             name += 1
#             liste.add(point)
#     return liste
#
#
# def ga_solve(File=None, gui=True, maxTime=0):
#     screen = initScreen()
#     liste = set()
#     if(gui is True):
#         liste = drawWindow(screen)
#     else:
#         liste = readFile(File)
#         # drawCity(liste, screen)
#     startSolve(liste)
#
#
# def startSolve(liste):
#     im = IndividualManager()
#     for element in liste:
#         im.addPoint(element)
#
#     population = Population(im, 100, True)
#     print("Distance initiale: " + str(population.getFittest().getTotalLength()))
#
#     ga = GeneticAlgorithm(im)
#     population = ga.evolution(population)
#     for i in range(0, 100):
#         population = ga.evolution(population)
#
#     print("Distance finale: " + str(population.getFittest().getTotalLength()))
#     bestPop = pop.getFittest()
#
#     for ville in bestPop.individual:
#         print(ville.name)






if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     ga_solve(File=sys.argv[1], gui=False, maxTime=0)
    # else:
    #     ga_solve(maxTime=0)

    im = IndividualManager()

    point1 = Point(3, 4)
    point1.addName("truc")
    point2 = Point(1, 9)
    point2.addName("truc1")
    point2 = Point(7, 8)
    point2.addName("truc2")

    pop = Population(im, 50, True)
    print("Distance intiale: " + str(pop.getFittest().getTotalLength()))

    ga = GeneticAlgorithm(im)
    pop = ga.evolution(pop)

    for i in range(0, 100):
        pop = ga.evolution(pop)

    print("Distance finale: " + str(pop.getFittest().getTotalLength()))
