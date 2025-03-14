import pygame
from sys import exit
from utils import load_image,load_images
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 720))
        pygame.display.set_caption('stupid fucking game')
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        self.assets = {
            'player':load_images('player')
        }
        self.player = Player(self, [0, 0])

    def game_running(self):
        self.movement[0] = False
        self.movement[1] = False

        while True:
            self.screen.fill((123,24,25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in {pygame.K_LEFT,pygame.K_a}:
                        self.movement[0] = True
                    if event.key in {pygame.K_RIGHT,pygame.K_d}:
                        print('hi')
                        self.movement[1] = True
                    if event.key in {pygame.K_UP,pygame.K_w}:
                        #self.player.jump()
                        pass

                elif event.type == pygame.KEYUP:
                    if event.key in {pygame.K_LEFT,pygame.K_a}:
                        self.movement[0] = False
                    if event.key in {pygame.K_RIGHT,pygame.K_d}:
                        print('bye')
                        self.movement[1] = False

            print(self.movement)
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            self.clock.tick(60)
            pygame.display.update()

    def run(self):
        self.game_running()

if __name__ == '__main__':
    game = Game()
    game.run()