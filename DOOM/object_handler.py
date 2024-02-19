from sprite_objects import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.dead_npc_list = []
        self.npc_sprite_path ='Resources/Sprites/npc/'
        self.static_sprite_path = 'Resources/Sprites/static_sprites/'
        self.animated_sprite_path = 'Resources/Sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        ##Sprites
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        add_sprite(AnimatedSprite(game, path=self.animated_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))

        ##NPCs
        add_npc(NPC(game, pos=(6,3)))
        add_npc(SoldierNPC(game, pos=(12,2)))
        add_npc(CacoDemon(game, pos=(10, 6)))
        add_npc(CacoDemon(game, pos=(3, 6)))
        add_npc(CacoDemon(game, pos=(13, 7)))
        add_npc(CyberDemon(game,pos=(13, 3)))
        self.total_number_npcs = len(self.npc_list)
        print(self.npc_list)

    def update(self):
        self.npc_positions = {npc.map_position for npc in self.npc_list if npc.alive}
        for sprite in self.sprite_list:
            sprite.update()
        for npc in self.npc_list:
            npc.update()


    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)