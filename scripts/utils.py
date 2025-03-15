import pygame
import os

BASE_IMG_PATH = 'assets/images/'

def load_image(path,alpha=False):
    if alpha:
        img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
        return img
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path,alpha=False):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        if img_name == '.DS_Store':
            continue
        images.append(load_image(path + '/' + img_name, alpha))
    return images


class Text:
    def __init__(self,text,size,color,pos):
        self.texts = text.split('\n')
        self.color = color
        self.pos = pos
        self.size = size
        self.font = pygame.font.Font('assets/fonts/RusticRoadway.otf',self.size)
        self.images = [self.font.render(text,True,color) for text in self.texts]

    def render(self,surf,offset=(0,0)):
        for i in range(len(self.images)):
            surf.blit(self.images[i],(self.pos[0]-offset[0],int(self.size*i*1.2) + (self.pos[1]-offset[1])))
