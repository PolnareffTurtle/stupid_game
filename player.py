import pygame

class Player:
    def __init__(self,game,pos):
        self.game = game
        self.pos = pos
        self.image = self.game.assets['player'][0]
        self.size = self.image.get_size()
        self.velocity = [0,0]
        self.flip = False

    def update(self,movement):
        terminal_velocity = 10
        print(movement)

        frame_movement = (movement[0] * 2 + self.velocity[0], movement[1] + self.velocity[1])
        print(frame_movement)

        self.pos[1] += frame_movement[1]
        self.pos[0] += frame_movement[0]

        self.velocity[1] = min(terminal_velocity, self.velocity[1] + 0.25)  # 10 is the terminal velocity

        if self.pos[1] > 600:
            self.pos[1] = 600
            self.velocity[1] = 0

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True


    def render(self, surf,offset=(0,0)):
        surf.blit(pygame.transform.flip(self.image,self.flip,False),(self.pos[0] - offset[0], self.pos[1] - offset[1] ))
        pygame.draw.rect(self.game.screen,(0,0,255),pygame.rect.Rect(self.pos[0]-offset[0],self.pos[1]-offset[1],self.size[0],self.size[1]),width=1)

