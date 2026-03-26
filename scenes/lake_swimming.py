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

# -----------------------------------------------

def continuation_scene():
    
    print(f"\nyou remove you outer clothes")
    sleep(2.0)
	print(f"\n you fold them nicely and place on a stone")
	sleep(2.0)
	print(f".....*****.......")
	sleep(2.0)
    print(f"\nyou carefully walk into the lake")
    sleep(2.0)
	print(f"\.........********swimming********............")
	sleep(2.0)
	print(f"\nyou find a stick poking above the water a bit far away")
	sleep(2.0)
    print(f"\nit feels like moving")
    sleep(2.0)
    print(f"\nwhat would you do ???")
    sleep(1.0)


    # You can add options for the player to choose from like this:
    next_scene_02 = choose_option([
        ('I should swimm towards it', continuation_scene_01), # If you want option 1 to lead to a continuation_scene
        ('Maybe i should just leave the water', None)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene_02


def continuation_scene_01():

    print(f"\nyou swimm slowly towards the stick")
    sleep(2.0)
    print(f".....*****.......")
    sleep(2.0)
    print(f"\.........********swimming********............")
    sleep(2.0)
    print(f"\nyou first have a look")
    sleep(2.0)
    print(f"\nwhat would you do ???")
    sleep(1.0)

    # You can add options for the player to choose from like this:
    next_scene_03 = choose_option([
        ('I should try to pickit', continuation_scene_02_02), # If you want option 1 to lead to a continuation_scene
        ('I feel something is not right, i should turn back', continuation_scene_02_01))                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene_03

def continuation_scene_02_01():

    print(f"\nyou decided to leave and swimm back")
    sleep(2.0)
    print(f".....*****.......")
    sleep(2.0)
    print(f"\.........********swimming********............")
    sleep(2.0)
    print(f"\nyou feel like something is following you under the water")
    sleep(2.0)
	print(f"\nyou swimm faster and faster")
	sleep(2.0)
    print(f"\nyou start you realize something comming up from the water on to surface")
    sleep(2.0)
    print(f"\nbefore you could reach the shore a big spike got embedded into you stomach")
    sleep(2.0)
    print(f"\n............we your dead.... try again.....")

def continuation_scene_02_02():

    print(f"\nyou hold the stick")
    sleep(2.0)
    print(f"you feel the vibrations")
    sleep(2.0)
    print(f"\.........***slight panick***...........")
    sleep(2.0)
    print(f"\nyou feel like the stick is pulling you")
    sleep(2.0)



    example_roll = chance_roll(50) # You can use a chance roll like this, where 25 is the probability of success
    
    if example_roll:
        
        print(f"\nThings are happening!")
        sleep(2.0)
		print("the water started to shake and you refuse to let it go")
		sleep(2.0)
		print("you feel like your legs are trembling like things are moving under you feet along with your feet")
		sleep(2.0)
		print("........***you geeting draged********...........")
		sleep(3.0)
	    print(f"\nrolling dexterity check")
    	sleep(2.0)

		
		dexterity_roll = chance_roll(50)
		
		if dexterity_roll:
		
			print(f"\nground started to shake a bit more")
			sleep(2.0)
			print(f"\n.....buch***sssshhhhh...shhhhh.......")
            sleep(2.0)
            print(f"\nyou start to fall")
            sleep(2.0)	
            print(f"\n*******bhaaammmmm..........")
            sleep(4.0)
			print(f"\nyou open your eyes and all you see is you are on an island that appeared from the surface")
			sleep(2.0)
			print(f"\nyou realize you woke up a sea monster")
			slepp(2.0)
			print(f"\n......to be continued......")


        return None
        # When you are ready to end the scene, return:
        #   None:  to continue the game
        #   True:  to win the game
        #   False: to lose the game
    
    else:
		print(f"\nyou left the stick due to lot of pressure ")
		sleep(2.0)
		print(f"\nyou are now in the water and see something rising above the water and you start swimming back")
		

        return None

