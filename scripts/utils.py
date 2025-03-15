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