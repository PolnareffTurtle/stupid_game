import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 720))
        pygame.display.set_caption('stupid fucking game')
        self.clock = pygame.time.Clock()

    def game_running(self):
        while True:
            self.screen.fill((123,24,25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.clock.tick(60)
            pygame.display.update()

    def run(self):
        self.game_running()

if __name__ == '__main__':
    game = Game()
    game.run()