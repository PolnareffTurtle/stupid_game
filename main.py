import pygame
from sys import exit
from scripts.utils import load_image,load_images
from scripts.player import Player
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 768))
        self.display = pygame.Surface((480, 384))
        pygame.display.set_caption('vance adventures')
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        self.level = 1
        self.assets = {
            'player':load_images('player'),
            'background':load_image('america.jpg'),
            'tiles':load_images('tiles')
        }
        self.player = Player(self, [0, 0])

    def game_running(self):
        self.tilemap = Tilemap(self,self.level)
        self.movement[0] = False
        self.movement[1] = False

        while True:
            self.display.blit(pygame.transform.scale(self.assets['background'],self.display.get_size()),(0,0))
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
                        self.player.jump()
                        pass

                elif event.type == pygame.KEYUP:
                    if event.key in {pygame.K_LEFT,pygame.K_a}:
                        self.movement[0] = False
                    if event.key in {pygame.K_RIGHT,pygame.K_d}:
                        print('bye')
                        self.movement[1] = False

            print(self.movement)
            self.tilemap.render(self.display)

            self.player.update(self.tilemap,(self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(60)
            pygame.display.update()

    def run(self):
        self.game_running()

if __name__ == '__main__':
    game = Game()
    game.run()