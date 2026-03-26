"""
=====================================================================
  Scenes / Dungeon Crawl
  Author:     	Rahul Pinnala
  Date:       	26.03.2026
  Contact:    	pinnala@uni-bremen.de
  Checked:		26.03.2026-16:48 german time
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register
def example_scene():

    print("\nit is a sunny day and something shiny caught your eye")
    sleep(2.0)
    print("\n.....**shiny shiny**", end=' ', flush=True)
    sleep(2.0)
    print("\nyou realized something is there beyond the very thick high bushes")
    sleep(2.0)
    print("\nyou go closer towards it squeezing through the bushes", end=' ', flush=True)
    sleep(2.0)
    print("\nafter passing through enough bushes you open your eyes")
    sleep(2.0)
    print("\nyou see a beautiful crystal clear lake in front of you")
    sleep(2.0)
    print("\ndo you want to swim?")

    next_scene = choose_option([
        ('Yes, I will swim', continuation_scene),
        ('No, it is probably not worth it', None)
    ])

    return next_scene


# -----------------------------------------------

def continuation_scene():

    print("\nyou remove your outer clothes")
    sleep(2.0)
    print("\nyou fold them nicely and place them on a stone")
    sleep(2.0)
    print(".....*****.......")
    sleep(2.0)
    print("\nyou carefully walk into the lake")
    sleep(2.0)
    print(".........********swimming********............")
    sleep(2.0)
    print("\nyou find a stick poking above the water a bit far away")
    sleep(2.0)
    print("\nit feels like it's moving")
    sleep(2.0)
    print("\nwhat would you do???")
    sleep(1.0)

    next_scene_02 = choose_option([
        ('I should swim towards it', continuation_scene_01),
        ('Maybe I should leave the water', None)
    ])

    return next_scene_02


def continuation_scene_01():

    print("\nyou swim slowly towards the stick")
    sleep(2.0)
    print(".....*****.......")
    sleep(2.0)
    print(".........********swimming********............")
    sleep(2.0)
    print("\nyou take a closer look")
    sleep(2.0)
    print("\nwhat would you do???")
    sleep(1.0)

    next_scene_03 = choose_option([
        ('I should try to pick it', continuation_scene_02_02),
        ('I should turn back', continuation_scene_02_01)
    ])

    return next_scene_03


def continuation_scene_02_01():

    print("\nyou decide to swim back")
    sleep(2.0)
    print(".....*****.......")
    sleep(2.0)
    print(".........********swimming********............")
    sleep(2.0)
    print("\nyou feel like something is following you underwater")
    sleep(2.0)
    print("\nyou swim faster and faster")
    sleep(2.0)
    print("\nyou realize something is coming up from the water surface")
    sleep(2.0)
    print("\nbefore you reach the shore, a spike pierces your stomach")
    sleep(2.0)
    print("\n............you're dead.... try again.....")

    return None


def continuation_scene_02_02():

    print("\nyou grab the stick")
    sleep(2.0)
    print("\nyou feel vibrations")
    sleep(2.0)
    print(".........***slight panic***...........")
    sleep(2.0)
    print("\nyou feel like the stick is pulling you")
    sleep(2.0)

    example_roll = chance_roll(50)

    if example_roll:

        print("\nThings are happening!")
        sleep(2.0)
        print("the water starts to shake and you refuse to let go")
        sleep(2.0)
        print("your legs tremble as something moves beneath you")
        sleep(2.0)
        print("........***you are getting dragged********...........")
        sleep(3.0)

        print("\nrolling dexterity check")
        sleep(2.0)

        dexterity_roll = chance_roll(50)

        if dexterity_roll:

            print("\nground starts to shake even more")
            sleep(2.0)
            print("\n.....buch***sssshhhhh...shhhhh.......")
            sleep(2.0)
            print("\nyou start to fall")
            sleep(2.0)
            print("\n*******bhaaammmmm..........")
            sleep(4.0)
            print("\nyou open your eyes and find yourself on an island")
            sleep(2.0)
            print("\nyou realize you woke up a sea monster")
            sleep(2.0)
            print("\n......to be continued......")

            return None

        else:
            print("\nyou lose your grip and fall back into the water")
            sleep(2.0)
            print("\nsomething moves below... and everything goes dark")

            return None

    else:
        print("\nyou let go of the stick due to strong pressure")
        sleep(2.0)
        print("\nyou swim back as something rises behind you...")

        return None
