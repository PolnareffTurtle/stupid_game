import pygame
import math
import json

NEIGHBOR_OFFSETS = [
    (-1,-1), (0,-1), (1,-1), (2,-1),
    (-1,0),  (0,0),  (1,0),  (2,0),
    (-1,1),  (0,1),  (1,1),  (2,1)
]

class Tile:
    def __init__(self, tile_index, pos, type):
        self.index = tile_index
        self.pos = pos
        self.type = type

class Tilemap:
    def __init__(self,game,level,tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.open_json(level)

    def open_json(self,level):
        with open('assets/levels/'+str(level)+'.json') as f:
            rawjson = f.read()
            jsondata = json.loads(rawjson)
            self.game.player.pos = [16 * jsondata['properties'][4]['value'],  # player_x
                                    16 * jsondata['properties'][5]['value']]  # player_y
            self.height = jsondata['height']
            for i in jsondata['layers']:
                for j, val in enumerate(i['data']):
                    x = j % jsondata['width']
                    y = j // jsondata['width']
                    if val != 0:
                        self.tilemap[(x, y)] = Tile(val - 1, (x, y),jsondata['properties'][val-1]['value'])

    def tiles_around(self,pos):
        tiles=[]
        tile_loc = (int(pos[0] // self.tile_size),int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = (tile_loc[0]+offset[0], tile_loc[1]+offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self,pos):
        rects = {'physics':[],'win':[],'lose':[],'jump':[]}
        for tile in self.tiles_around(pos):
            print(tile.type)
            rects[tile.type].append(pygame.rect.Rect(tile.pos[0]*self.tile_size,tile.pos[1]*self.tile_size,self.tile_size,self.tile_size))
        return rects

    def render(self, surf, offset=(0,0)):
        for x in range(math.floor(offset[0] / self.tile_size), math.ceil((offset[0] + surf.get_width()) / self.tile_size)):
            for y in range(math.floor(offset[1] / self.tile_size), math.ceil((offset[1] + surf.get_height()) / self.tile_size)):
                if (x,y) in self.tilemap:
                    tile = self.tilemap[(x,y)]
                    surf.blit(
                        self.game.assets['tiles'][tile.index],
                        (tile.pos[0]*self.tile_size - offset[0], tile.pos[1]*self.tile_size - offset[1]))
