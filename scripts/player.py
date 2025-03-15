import pygame

class Player:
    def __init__(self,game,pos):
        self.game = game
        self.pos = pos
        self.image = self.game.assets['player'][0]
        self.size = self.image.get_size()
        self.velocity = [0,0]
        self.flip = False
        self.jumps = 1
        self.terminal_velocity = 20
        self.air_time = 0
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        return pygame.rect.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])


    def check_collisions(self,axis: int,rects,frame_movement):
        if not rects:
            return
        self.pos[axis] += frame_movement[axis]
        entity_rect = self.rect()
        for rect in rects['physics']:
            #self.rect_render(rect)    #<--- DEBUGGING
            if entity_rect.colliderect(rect):
                if frame_movement[axis] > 0:
                    if axis == 0:
                        entity_rect.right = rect.left
                        self.collisions['right'] = True
                    else:
                        entity_rect.bottom = rect.top
                        self.collisions['down'] = True
                if frame_movement[axis] < 0:
                    if axis == 0:
                        entity_rect.left = rect.right
                        self.collisions['left'] = True
                    else:
                        entity_rect.top = rect.bottom
                        self.collisions['up'] = True
                self.pos[axis] = entity_rect.x if axis == 0 else entity_rect.y

    def update(self,tilemap,movement):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        frame_movement = (movement[0] * 5 + self.velocity[0], movement[1] + self.velocity[1])

        rects = tilemap.physics_rects_around(self.pos)

        self.check_collisions(1, rects, frame_movement)  # check vertical collisions
        self.check_collisions(0, rects, frame_movement)  # check horizontal collisions

        entity_rect = self.rect()
        for rect in rects['lose']:
            if entity_rect.collidepoint(rect.center):
                self.game.gamestate = self.game.LOSE
        for rect in rects['win']:
            if entity_rect.colliderect(rect):
                self.game.gamestate = self.game.WIN
        for rect in rects['jump']:
            if entity_rect.collidepoint(rect.center):
                self.velocity[1] = -8

        self.air_time += 1
        if self.collisions['up'] or self.collisions['down']:
            self.velocity[1] = 0
            self.air_time = 0
            self.jumps = 1

        self.velocity[1] = min(self.terminal_velocity, self.velocity[1] + 0.5)  # 10 is the terminal velocity

        """if self.pos[1]+self.image.get_height() > 200:
            self.pos[1] = 200 - self.image.get_height()
            self.velocity[1] = 0
            self.jumps = 1"""

        if self.air_time > 4:
            self.jumps = 0

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True




    def render(self, surf,offset=(0,0)):
        surf.blit(pygame.transform.flip(self.image,self.flip,False),(self.pos[0] - offset[0], self.pos[1] - offset[1] ))
        #pygame.draw.rect(self.game.display,(0,0,255),pygame.rect.Rect(self.pos[0]-offset[0],self.pos[1]-offset[1],self.size[0],self.size[1]),width=1)

    def jump(self):
        if self.jumps:
            self.velocity[1] = -10
            self.jumps -= 1
            self.air_time = 5