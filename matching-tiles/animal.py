import os
import random
import game_config as gc

from pygame import image, transform

animals_count = dict([(a, 0) for a in gc.ASSET_FILES])

def available_animals():
    res = []
    for a, c in animals_count.items():
        if c < 2:
           res.append(a)     
    return res

class Animal:
    def __init__(self, index):
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.name = random.choice(available_animals())
        animals_count[self.name] += 1

        self.front_path = os.path.join(gc.ASSET_DIR, self.name)
        self.image = image.load(self.front_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))
        self.skip = False