﻿# window
window = {
    'width': 1280,
    'height': 720,
    'caption': "King of the Dungeon",
    "fullscreen": False,
    'resizable': True
}

window_original = (1920, 1080)

# static positioning
monster_pos = (500, 500)
gold_pos = ((100, 100), (300, 300))

# minions

soldiers = { # ((attack, defense), corpse cost, weapon cost)
	"goblin": 			((1, 1), 1, 0),
	"hobgoblin": 		((2, 2), 1, 1),
	"orc": 				((3, 3), 1, 2), # wait 1 turn to fight (enter stack)
	"madgnome": 		((2,1), 1, 2), # spawn madgnome_count when bought
	"necromancer": 		((0,1), 0, 0) # costs gold
}

farmers = { # (cost, gathred gold, gathered corpses, gathered weapons)
	"miner": 			(1, 5, 0, 0),
	"gatherer": 		(1, 1, 5, 1)
}


madgnome_count = 3

necromancer_gold_cost = 10
necromancer_revival_chance = 0.2

spy_frecuency = 0.05


# treasure hunters

hunters = { # (attack, defense)
	"vagabound":		(1, 1),
	"militia":			(1, 2),
	"looter":			(2, 1),
	"defender":			(1, 5),
	"agressor":			(3, 2),
	"champion":			(5, 5)
}

waves = ( # (vagabound, militia, looter, defender, agressor, champion)
	(5, 1, 0, 0, 0)
)