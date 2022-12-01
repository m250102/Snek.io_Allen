import sys
from background import background
import pygame
import time


class Snek:

    def __init__(self):
        pygame.init()
        self.bg_color = (250,255,255)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        pygame.display.set_caption('Snek')
        self.back = background(self)
        #>=

    def run_game(self):
        while True:
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.blit(self.back.image, (0,0))
            pygame.display.flip()




    # surface = pygame.display.set_mode((900, 500))
    # surface.fill((255, 100, 209))
    # pygame.display.flip()

    # time.sleep(5)

if __name__ == '__main__':
    ai = Snek()
    ai.run_game()
