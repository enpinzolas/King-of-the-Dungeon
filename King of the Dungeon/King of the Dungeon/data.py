﻿# window
window = {
    'width': 1280,
    'height': 720,
    'caption': "King of the Dungeon",
    "fullscreen": False,
    'resizable': True
}

window_original = (1920, 1080)

# misc
start_gold = 7
start_corpses = 9999
start_weapons = 9999
gold_objective = 10000

house_scale= 6
minion_scale=1.5 	

# static positioning
monster_pos = (650, 750)
gold_pos = ((100, 100), (300, 300))

# minions

soldiers = { # ((attack, defense), corpse cost, weapon cost)
	"goblin": 			((1, 1), 1, 0),
	"hobgoblin": 		((2, 2), 1, 1),
	"orc": 				((2, 4), 2, 2), # they have a 50% chance to attack twice, if they kill in the first attack they take no damage
	"madgnome": 		((2,1), 1, 2), # spawn madgnome_count when bought
	"necromancer": 		((0,1), 0, 0) # costs gold
}

farmers = { # (cost, success rate, gathred gold, gathered corpses, gathered weapons)
	"miner": 			(1, 0.01, 5, 0, 0),
	"gatherer": 		(1, 0.08, 1, 5, 1)
}

spawn_place = {
	"goblin": 			(75, 200),
	"hobgoblin": 		(350, 180),
	"orc": 				(200, 350), 
	"madgnome": 		(925, 160),
	"necromancer": 		(1055, 240),
	"gatherer":			(1200, 260),
	"miner":			(1000, 420)
}

minion_move_to = {
	"goblin": 			(0, -213),
	"hobgoblin": 		(0, -180),
	"orc": 				(0, -350), 
	"madgnome": 		(0, -162),
	"necromancer": 		(0, -240),
	"gatherer":			(0, -273),
	"miner":			(270, 0)
}

minion_move_time = 3

orc_berserk_chance = 0.5

madgnome_count = 3

necromancer_gold_cost = 10
necromancer_revival_chance = 0.2

spy_frecuency = 0.05


# treasure hunters

hunters = ( # (attack, defense)
			(1, 1), # vagabound
	        (1, 2), # militia
			(2, 1), # looter
			(1, 5), # defender
			(3, 2), # agressor
			(5, 5)  # champion
)

waves = ( # (vagabound, militia, looter, defender, agressor, champion)
	(5, 1, 0, 0, 0)
)