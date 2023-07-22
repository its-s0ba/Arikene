# modules

from sys import exit
import time
import os
from os import system, name

# global variables

has_shotgun = False
obtained_key = False
tester1 = "Chaz Moore"
tester2 = "Claudia Taylor"
tester3 = "Dan Root"
tester4 = "Karen Diggs"
helped = "Kris Wasnidge"

# function for testing purposes

def test(string):
    slow_print(string, "This is a test slow_print!")
    exit(0)

def slow_print(string):
    for x in [*string]:
        print(x, end='', flush=True)
        time.sleep(0.05)
    print("\n")

# clear function

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # everything else...
    else:
        _ = system('clear')

# title screen

def title_screen():
    print("""
       _____        .__ __                         
      /  _  \_______|__|  | __ ____   ____   ____  
     /  /_\  \_  __ \  |  |/ // __ \ /    \_/ __ \ 
    /    |    \  | \/  |    <\  ___/|   |  \  ___/ 
    \____|__  /__|  |__|__|__|\___  >___|  /\___  >
            \/                    \/     \/     \/ 

    """)
    slow_print("Welcome to Arikene.")
    slow_print("What is your name?")
    player_name = input("> ")
    slow_print(f"Welcome, {player_name}!")
    slow_print("Please type 'start' to play, or 'quit' to exit.")
    proper_input = False

    while True:
        choice = input("> ")
        
        if choice == "start":
            clear()
            start()
        elif choice == "skip":
            clear()
            entrance()
        elif choice == "quit":
            exit(0)
        else:
            slow_print("Sorry, that isn't an option here... Please try again.")

# death function

def dead(why):
    slow_print(why, "Good job! You are dead.")
    exit(0)

# start function

def start():
    slow_print("You walk upon the Temple of Arikene...")
    slow_print("The planet itself is a desert with a cream colored sky, with bands of orange and peach. It has no moons, and one high density planetary ring made up of ice and gas.")
    slow_print('It is 1.32x the size of Earth, and is 0.35 AU from its star "Ujothan-387B".')
    slow_print("The temperature ranges from -94F to 243F with an average of 80F. It is unsuitable for earth-based lifeforms without additional assistance from water reclaim suits with protection from extreme temperatures.")
    slow_print("It is 8% water, all subterranean...")
    slow_print("The length of day is 18 Hours, and the length of year is 100 Earth days.")
    slow_print("The planet is inhabited by a race of Humans native to the planet called The Alkahn.")
    slow_print('The Alkahn are a calculating race, that have a social hierarchy that of wolves. Alien species to the planet call them "Al\'it-hakri" which translates to "those who fight like demons".')
    slow_print('The Alkahn have a temple of their God "Ith\'ui Kahn". This temple is frequently subjected to raids from aliens who seek a prize hidden within that only the most creative minded souls could conjure an idea of what it could be.')
    slow_print('The Alkahn have laid traps and a beast within to guard their temple and it\'s prize...')
    slow_print("You are a fixer that lives on a technologically advanced planet, here to gain a quick buck with this rumored prize. You took the long journey across the universe, and are now only left with a broken pistol, and a sharp titanium knife. You must rely on wit and your surroundings if you wish to live.")
    slow_print("You enter the temple... You walk down a set of steps and are immediately graced by a damp darkness, with the only bit of light from the entrance showing the walls of what appears to be a hallway, but it is still much too dark to see ahead of you.")
    slow_print("You can - however, make out the faintness of a hall just off to the left...")
    slow_print("What will you do?")
    looked_around = False
    
    while True:
        choice = input("> ")

        if choice == "go left" or choice == "left":
            room_one()
        elif choice == "go straight" or choice == "straight":
            dark_hallway()
        elif choice == "look around" and not looked_around:
            slow_print("You look around... But nothing has changed.")
        elif choice == "h4ck7h3pl4n37!":
            auto_win()
        else:
            dead("You sit down, filled with disbelief. You think the task is too daunting. You get up and leave the temple, wandering around the desert planet until you starve.")

# entrance_for_skip

def entrance():
    slow_print("You enter the temple... You walk down a set of steps and are immediately graced by a damp darkness, with the only bit of light from the entrance showing the walls of what appears to be a hallway, but it is still much too dark to see ahead of you.")
    slow_print("You can - however, make out the faintness of a hall just off to the left...")
    slow_print("What will you do?")
    looked_around = False
    
    while True:
        choice = input("> ")

        if choice == "go left" or choice == "left":
            room_one()
        elif choice == "go straight" or choice == "straight":
            dark_hallway()
        elif choice == "look around" and not looked_around:
            slow_print("You look around... But nothing has changed.")
        elif choice == "h4ck7h3pl4n37!":
            auto_win()
        else:
            dead("You sit down, filled with disbelief. You think the task is too daunting. You get up and leave the temple, wandering around the desert planet until you starve.")

# Room 1

def room_one():
    slow_print("You turn left down the hall to head into the unknown room.")
    slow_print("Upon entering, you notice that in the back right corner of the room there is a lit torch, spilling a murky mixture of light and shadows on each of the four walls.")
    slow_print("On the back wall, there is a set of steps that lead down roughly two feet deeper into the ground, giving way to another smaller room.")
    slow_print("What do you do?")

    choice = input("> ")

    if choice == "look around":
        slow_print("You look around the room...")
        slow_print("You look back into the smaller room. The light doesn't reach this area, but you can just barely make out a small object on the ground.")
        slow_print("Looking around the main room, you find a piece of paper in one of the corners of the room.")
        slow_print("You walk over to the piece of paper and pick it up. It reads:")
        slow_print(""" 
         _______________________________________________________________________________________
        ( If you're reading this, then someone has taken this challenge, just as I have.        (
        ) I'm not sure if I will make it out alive or not, but I have an upper hand!            )
        ( There is a quirk about the beast within these walls. One of the Alkahn people told    (
        ) me it is easily angered, and you can taunt it into rushing you. If you place yourself )
        ( behind a pillar at the right time, you can cause the beast to crash into it, wounding (
        ) it. I'll try it out, and hopefully the gem will make me very rich!                    )
        (                                                                                       (
        )_______________________________________________________________________________________) 

        """)
        slow_print("You set the paper back down. Maybe someone else can use this.")
        slow_print("You move over to the small room. You poke around the dark and feel your hand come into contact with something dry and smooth. You pick it up and hold it into the light. It's a skull! You decide to take it with you.")
        slow_print("You decide that it's time to move on from this room. You leave into the hallway.")
        dark_hallway()
    elif choice == "leave":
        slow_print("You decide that it's time to move on from this room. You leave into the hallway.")
        dark_hallway()
    else:
        dead("Hey so remember that tuna sandwich you ate on the ship? It was expired.")

# Dark Hallway

def dark_hallway():
    slow_print("You walk into the dark hallway. After fumbling around you find the wall, and start forward letting one hand guide you outstretched, while the other traces the wall.")
    slow_print("You take a moment to pause, and you wonder to yourself about the aforementioned traps you've heard about in this temple. Curious...")
    slow_print("What will you do?")

    choice = input("> ")

    if choice == "look around":
        slow_print("You can't see much. So you get down on your hands and knees and feel around for anything on the ground.")
        slow_print("You feel something slip past your fingers, thin and light. You give it a tug, and hear a large door open in front of you. It must be a pitfall trap.")
        slow_print("You decide to try and jump over the opening in the floor... You make it aross no sweat!")
        item_room()
    elif choice == "continue":
        dead("You press on, but feel something snag around your ankles. You trip and find yourself falling a far distance. You hit the ground.")
    else:
        dead("You slip and fall hitting your head and you bleed out.")

# Item Room

def item_room():
    slow_print("After walking for what has felt like an enormous amount of time. You find that a dim glow has graced you with its soft presence.")
    slow_print("You notice another offshoot hall to your left, the light is coming from this hallway. The way forward is still dark.")
    slow_print("What will you do?")
    looked_around_2 = False
    
    while True:
        choice = input("> ")

        if choice == "look around" and not looked_around_2:
            slow_print("You look around, but nothing has changed.")
        elif choice == "go left" or choice == "left":
            slow_print("You turn left, and walk down the corridor and come across a door. The door has an opening for a window, and there is light coming from the inside. You peer in, and notice a shotgun laying in the corner of the room.")
            slow_print("What will you do?")
            used_knife = False
            global has_shotgun

            while True:
                choice = input("> ")

                if choice == "open door" and not used_knife:
                    slow_print("You try the door, but it doesnt budge. It looks like you might be able to pry it open with something sharp.")
                elif choice == "use knife" and not used_knife:
                    slow_print("You press the tip of the blade between the door and its threshold. Giving a quick downward jolt. The door budges slightly.")
                    used_knife = True
                elif choice == "open door" and used_knife:
                    try_door = "You try the door..."
                    for i in range(19):
                        slow_print(try_door[i], end='', flush=1)
                    door_opens = " The door swings open!"
                    for i in range(22):
                        slow_print(door_opens[i], end='', flush=1)
                    slow_print("You walk inside and collect the shotgun. It looks old, and the wood has dry rot, but it looks like it might still fire.")
                    slow_print("You check for ammo, opening its break. It has only one shell. Better use it wisely.")
                    has_shotgun = True
                elif choice == "leave" and not has_shotgun:
                    slow_print("You decide you don't need that old shotgun, and you leave the room.")
                    center_room()
                elif choice == "leave" and has_shotgun:
                    slow_print("With the shotgun strapped to your back, you leave the room.")
                    center_room()
                else:
                    slow_print("I've got no idea what that means.")

        elif choice == "go straight" or choice == "straight":
            slow_print("You decide that your time won't be wasted exploring that area. You press on into the next room.")
            center_room()
        else:
            dead("Ever heard of an aneurysm? Yeah they're real.")

# Center Room

def center_room():
    slow_print("You travel down the dark hallway once more and walk into a room. It's dark, but you can make out three corridors leading out of the room.")
    slow_print("There is a corridor on your left, one on your right, and one in front of you.")
    slow_print("What will you do?")

    choice = input("> ")

    if choice == "go left" or choice == "left":
        slow_print("Stumbling around, you find a wall. You turn and walk to the left.")
        boss_room()
    elif choice == "go right" or choice == "right":
        slow_print("Stumbling around, you find a wall. You turn and walk to the right.")
        pitfall_death()
    elif choice == "go straight" or choice == "straight":
        slow_print("You walk deadpan straight forward, at least as straight forward as you possibly can in the dark.")
        flooded_corridor()
    else:
        dead("You trip over your feet falling face first on the ground. The impact breaks your nose and shoves it into your brain (Thanks Anthony).")

# Pitfall death

def pitfall_death():
    slow_print("You wander into the right corridor as blind as any bat. You think to yourself 'Man, why can't I see anything still?', and while you're thinking this, you start freefalling.")
    dead("You start to panic, but it's short lived because you are impaled by spikes before you can even consider having a panic attack.")

# Boss Room

def boss_room():
    slow_print("You enter the corridor, and you are immediately tripped by a wire. You hear a click to your right, and a click to your left. An arrow hit's you in the left leg just above the knee.")
    slow_print("You stumble forward in immense pain, and step on a panel that sinks into the ground. It's a pressure plate.")
    slow_print("You are immediately blinded with torch light in each corner of an enormous room, with four very fragile looking pillars. Looking behind you, there are two arrow traps: one on the left, which is the one responsible for the arrow in your leg, and one on the right, which appears to have been fired a long time ago.")
    slow_print("You hear a loud series of noises in front of you, where a large stone gate is sinking into the ground. A large beast emerges from a dark room. A horrifying monster, with the head of a abominable bull, the body of an ape, but five times the normal size of one, arms like frieght trains and fists like wrecking balls, legs like super colossus redwood trees, and a tail of a scorpion. A truly horrifying beast.")
    slow_print("It starts toward you. What will you do?")
    beast_taunted = False
    beast_wounded_shotgun = False

    while True:
        choice = input("> ")

        if choice == "run":
            dead("You try running from the beast, but you're slow with that arrow in your leg, and you take two steps before it charges you. It isn't long until it snatches you...")
        elif choice == "taunt beast" and not beast_taunted:
            slow_print("You start shouting at the beast. It shouts an ear piercing gutteral roar just before charging you.")
            slow_print("What will you do now?")

            choice = input("> ")

            if choice == "hide behind pillar" and has_shotgun:
                slow_print("You duck behind a pillar just as the beast reaches you, and he crashes into it staggering him.")
                slow_print("You take out your shotgun and aim at his head. You pull the trigger.")
                slow_print("The beast cries in pain, what will you do now?")
                beast_wounded_shotgun = True
                global obtained_key

                while True:
                    choice = input("> ")

                    if choice == "stab beast" and beast_wounded_shotgun:
                        slow_print("You sink your blade into the neck of the beast, killing it instantly. You must've struck an artery, blood is spraying everywhere.")
                        slow_print("You take a moment to rest and catch your breath on the base of the broken pillar. You notice the room the beast came out of, and decide to hobble your way over to it.")
                        slow_print("You make your way inside, and you're immediately hit with the smell. You notice a half eaten body in the corner, with an arrow in their right leg, just above the knee. They also have a key in their hand. You take the key.")
                        obtained_key = True
                        slow_print("You make your way out of the room, into the dark center room with all the corridors. (and this time you decide to go straight *ahem* *ahem*)")
                        center_room()
                    elif choice == "run":
                        dead("Why would you think running would help you here? Even after a shotgun blast to the face this thing is a brute.")
                    else:
                        slow_print("You have to make a desicion I can understand here.")
            elif choice == "hide behind pillar" and not has_shotgun:
                slow_print("You duck behind a pillar just as the beast reaches you, and he crashes into it staggering him.")
                slow_print("You duck behind another pillar, the beast crashes into it too. This process is repeated for all four pillars in the room.")
                slow_print("The beast is now crawling on the ground towards you. You hobble over to it, and you sink your blade into the neck of the beast, killing it instantly. You must've struck an artery, blood is spraying everywhere.")
                slow_print("You take a moment to rest and catch your breath on of the bases of a broken pillar. You notice the room the beast came out of, and decide to hobble your way over to it.")
                slow_print("You make your way inside, and you're immediately hit with the smell. You notice a half eaten body in the corner, with an arrow in their right leg, just above the knee. They also have a key in their hand. You take the key.")
                obtained_key = True
                slow_print("You make your way out of the room, into the dark center room with all the corridors.")
                center_room_after_boss_battle()
            else:
                dead("The beast charges you, and you don't have time to react.")

        elif choice == "shoot beast" and has_shotgun:
            dead("You've only got one bullet dude, did you really think that would work?")
        elif choice == "stab beast":
            dead("Really? A knife? ONLY a knife..? What is you're deal man? There are literally items around the temple you can use.")
        elif choice == "taunt beast" and beast_taunted:
            dead("Why in the WORLD would you try taunting it AGAIN?? The beast charges at you even more pissed off than before. He rips you in half.")
        else:
            slow_print("Please type something that's an actual choice here.")

# center room after boss battle

def center_room_after_boss_battle():
    slow_print("You travel down the dark hallway once more and walk into a room. It's dark, but you can make out three corridors leading out of the room.")
    slow_print("There is a corridor on your left, one on your right, and one in front of you.")
    slow_print("What will you do?")
    from_left = False

    while True:
        choice = input("> ")

        if choice == "go left" or choice == "left" and from_left:
            slow_print("You just came from this direction. You don't need to go back in there.")
        elif choice == "go right" or choice == "right":
            slow_print("Stumbling around, you find a wall. You turn and walk to the right.")
            pitfall_death()
        elif choice == "go straight" or choice == "straight":
            slow_print("You walk deadpan straight forward, at least as straight forward as you possibly can in the dark.")
            flooded_corridor()

# Flooded Corridor

def flooded_corridor():
    slow_print("You approach the corridor directly ahead of you, at least you assume so, it's still really dark in here.")
    slow_print("You find the opening of the corridor by feeling around, and take a step. You fall into water. This corridor is flooded.")
    slow_print("What will you do?")

    choice = input("> ")

    if choice == "swim":
        slow_print("You start swimming in the only direction there is to swim: Forward.")
        slow_print("The corridor has a left turn, that of which you swim gracefully through, and you reach a set of steps leading out of the water.")
        slow_print("Climbing out of the water, you come face to face with a door.")
        slow_print("What will you do?")

        while True:
            choice = input("> ")

            if choice == "open door" and not obtained_key:
                slow_print("The door is locked, it looks like it takes some kind of key.")
                slow_print("You decide to backtrack, and you swim back the way you came.")
                center_room()
            elif choice == "open door" and obtained_key:
                slow_print("The door unlocks, and you push it open.")
                gem_room()
            else:
                slow_print("That's not an option here.")
    elif choice == "leave":
        slow_print("You climb out of the water and head back the way you came.")
        center_room()
    else:
        dead("You get tired, and your head dips below the water. You struggle to keep yourself afloat. You never resurface.")

# Gem Room

def gem_room():
    slow_print("You walk into a large room, well lit by the torches in both far back corners of the room. In the center is an altar, with a giant emerald gemstone sitting atop.")
    slow_print("You approach the altar, and notice the gemstone is sitting on what looks like another pressure plate, similar to the one you missed in the last room. It's another trap.")
    slow_print("What will you do?")
    skull_used = False

    while True:
        choice = input("> ")

        if choice == "take gemstone" and not skull_used:
            slow_print("You hastily take the gemstone, thinking you can move faster than whatever trap is used to guard this precious stone.")
            dead("You were wrong, hindsight is always 20/20 when you're crushed by a giant rock trap.")
        elif choice == "use skull":
            slow_print("The pressure plate seems to be wide enough to set the skull you saved just beside the gemstone.")
            slow_print("You place it on the altar.")
            skull_used = True
        elif choice == "take gemstone" and skull_used:
            slow_print("You carefully pick up the gemstone, you catch yourself holding your breath.")
            slow_print("The pressure plate stays depressed. And you breath a sigh of relief.")
            slow_print(f"Congratulations! You leave the temple with the gemstone, and head offworld smuggled on a tradeship to sell your prize.")
            slow_print("You Win!")
            clear()
            credits()
            exit(0)
        else:
            slow_print("Please type something that makes sense dude.")

# auto_win()

def auto_win():
    l337 = "The world around you suddenly freezes, and your surroundings turn into glitchy code raining down from somewhere incomprehensible."
    slow_print(l337)
    h4x0r = "You start getting dizzy, and you pass ou"
    slow_print(h4x0r)
    l337_h4x = "t..."
    slow_print(l337_h4x)
    r3b007 = "Rebooting"
    slow_print(r3b007)
    w4k3_up = ".........."
    slow_print(w4k3_up)
    clear()
    slow_print("You suddenly come to.")
    slow_print("You look down and the gemstone is in your hands, and you're back in your apartment on your homeworld.")
    slow_print("You would ask yourself what the hell happened, but something tells you it was cool and badass so you don't care.")
    slow_print("You Win!")
    clear()
    credits()
    exit(0)

# Credits

def credits():
    slow_print("Thank you for playing!")
    slow_print("This game was built in a week, involving sleepless nights and a lot of bugged out logic.")
    slow_print(f"Special thanks to: {tester1}, {tester2}, {tester3}, {tester4}, and {helped}!")
    slow_print("I hope you enjoyed!")
    slow_print("- G.D. A.K.A 'S0ba'")
    exit(0)

# Game's official Start Sequence

title_screen()
