"""
=====================================================================
  Scenes / Dungen Crawl
  Author: 	Rahul Pinnala
  Date: 	26.03.2026
  Contact:	pinnala@uni-bremen.de
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def example_scene():
    
    print(f"\nit is a sunny day and something shiny caught your eye")
    sleep(2.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
    print(f"\n.....**shiny shiny**", end=' ', flush=True)
    sleep(2.0)
    print(f"\nyou realized something is there beyond the very thick high bushes")
    sleep(2.0)
	print(f"\nyou go closer towards it squeezing through the bushes", end=' ', flush=True)
    sleep(2.0)
	print(f"\nafter passing through enough bushes and you open your eyes")
	sleep(2.0)
	print(f"\nyou see a beautiful crystal clear lake infront of you")
	sleep(2.0)
	print(f"\ndo you want to swimm ")

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('Yes, i will definetly pick it', continuation_scene), # If you want option 1 to lead to a continuation_scene
        ('No, its probaly not worth anything', None)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

