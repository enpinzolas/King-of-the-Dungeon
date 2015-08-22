﻿import random
from cocos.director import director
from cocos.scene import Scene
from cocos.sprite import Sprite
from cocos.layer import Layer
from cocos.text import Label
from cocos.menu import Menu, ImageMenuItem, MenuItem, fixedPositionMenuLayout
from cocos.actions import *

from pyglet.image import load_animation

from data import *

from singletons import Gold, Logic

class HUDLayer(Layer):
    def __init__(self):
        super().__init__()

        self.text = Label("aaaa", x=100, y=280 )
        self.count_goblin = Label("5", x=200, y=300)
        self.count_hobgoblin = Label("0", x=250, y=300)
        self.count_orc = Label("0", x=300, y=300)
        self.count_madgnome = Label("0", x=350, y=300)
        self.count_necro = Label("0", x=400, y=300)
        self.count_miner = Label("0", x=450, y=300)
        self.count_gatherer = Label("0", x=500, y=300)
        self.count_corpses = Label("0", x=550, y=300)

        self.add(self.text)
        self.add(self.count_goblin)
        self.add(self.count_hobgoblin)
        self.add(self.count_orc)
        self.add(self.count_madgnome)
        self.add(self.count_necro)
        self.add(self.count_miner)
        self.add(self.count_gatherer)
        self.add(self.count_corpses)

    def update(self, corpses, weapons, gold, miners, gatherers, orcs):
        pass


class GUILayer(Menu):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic

        positions = []
        houses = []
        
        ############   goblin house    ###################
        house_goblin = ImageMenuItem("resources/goblin_quarters.png",
                                     self.logic.spawn('goblin'))
        houses.append(house_goblin)
        positions.append((100,60))

        ############  hobgoblin house  ###################

        house_hobgoblin = ImageMenuItem("resources/hobgoblin_quarters.png",
                                        self.logic.spawn('hobgoblin'))
        houses.append(house_hobgoblin)
        positions.append((200,60))

        ############     orc  house    ###################

        house_orc = ImageMenuItem("resources/orc_quarters.png",
                                  self.logic.spawn('orc'))
        houses.append(house_orc)
        positions.append((300,60))

        ############  madgnome house   ##################

        house_madgnome = ImageMenuItem("resources/madgnome_quarters.png",
                                       self.logic.spawn('madgnome'))
        houses.append(house_madgnome)
        positions.append((400,60))

        ############ necromancer house ###################

        house_necromancer = ImageMenuItem("resources/necromancer_quarters.png",
                                          self.logic.spawn('necromancer'))
        houses.append(house_necromancer)
        positions.append((500,60))

        ############  gatherer  house  ###################

        house_gatherer = ImageMenuItem("resources/gatherer_quarters.png",
                                       self.logic.spawn('gatherer'))
        houses.append(house_gatherer)
        positions.append((600, 60))

        ############   miner   house   ###################

        house_miner = ImageMenuItem ("resources/miner_quarters.png",
                                     self.logic.spawn('miner'))
        houses.append(house_miner)
        positions.append((700,60))

        ############    create menu    ###################

        self.create_menu(houses,
                         activated_effect=self.shake(),
                         selected_effect=None,
                         unselected_effect=None,
                         layout_strategy=fixedPositionMenuLayout(positions))

    def shake(self):
        """Predefined action that performs a slight rotation and then goes back to the original rotation
        position.
        """
        angle = 30
        duration = 0.01

        rot = Accelerate(RotateBy(angle, duration), 2)
        rot2 = Accelerate(RotateBy(-angle * 2, duration), 2)
        return rot + (rot2 + Reverse(rot2)) * 2 + Reverse(rot)

class DynamicLayer(Layer):
    def __init__(self):
        super().__init__()
        GUILayer.push_handlers(self)

    def invoke(self, minion):
        pass

    def bring(self, minion):
        pass

class StaticLayer(Layer):
    def __init__(self):
        super().__init__()

        # self.monster = Sprite("resource/monster.gif", position = monster_pos)
        self.monster = Sprite(load_animation("resources/monster.gif"), position = monster_pos)
        self.gold = Gold(self)

        self.add(self.monster)

class GroundLayer(Layer):
    def __init__(self):
        super().__init__()

        ws = director.get_window_size()

        self.cave_sprite = Sprite("resources/cave.png")
        self.cave_sprite.position = (ws[0]/2, ws[1]/2)

        self.background_sprite = Sprite("resources/background.png")
        self.background_sprite.position = (ws[0]/2, ws[1]/2)

        self.add(self.background_sprite, z=0)
        self.add(self.cave_sprite, z=1)

class RootLayer(Layer):
    def __init__(self):
        super().__init__()
        
        ws = director.get_window_size()
        self.scale_x = ws[0]/window_original[0]
        self.scale_y = ws[1]/window_original[1]

        dynamic_layer = DynamicLayer()
        hud_layer = HUDLayer()
        self.logic = Logic(dynamic_layer, hud_layer)

        self.add(GroundLayer(),        z=0)
        self.add(StaticLayer(),        z=1)
        self.add(DynamicLayer(),       z=2)
        self.add(GUILayer(self.logic), z=3)
        self.add(HUDLayer(),           z=4)


def main():
    director.init(**window)
    main_scene = Scene(RootLayer())
    director.run(main_scene)

if __name__ == '__main__':
    main()
