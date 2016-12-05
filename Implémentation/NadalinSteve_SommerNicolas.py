import pygame


def ga_solve(File=None, gui=True, maxTime=0):
    print("ga_Solve")
    if(File is None):
        (width, height) = (1800, 900)
        background_color = (255, 255, 255)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Probleme du voyageur de commerce')
        screen.fill(background_color)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.display.flip()


if __name__ == '__main__':
    ga_solve()
