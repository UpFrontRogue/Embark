from extras import *
from menus import character_menu
Tuttie = Npc('Tuttie', 'AA00000', 'Galactic Embroider', 85, 100)
def tuttie_menu(uid, character):
    cm_tutorial_1()
    while True:
        prints('1. Yeah, no, I got it..')
        prints('2. Repeat it word for word.')
        print()
        choice = inputs('Select an option: ')

        if choice == '1':
            character_menu(uid, character)
            printn
        elif choice == '2':
            cm_tutorial_1()
        else:
            prints("Invalid choice. Please choose again")

def cm_tutorial_1():

    printn("Hey! I'm Tuttie. I'm here to help show you how to play.", npc = Tuttie)
    print()
    printn("We'll start with the character menu!", npc = Tuttie)
    printn("This is this main Character Screen below.", npc = Tuttie)
    print()
    prints('   Character Menu')
    print()
    prints('----------------------')
    print()
    prints('1. Explore¡')
    prints('2. Inventory¡')
    prints('3. Battle Box¡')
    prints('4. Roll Dice¡')
    prints('5. Options¡')
    prints('6. Back')
    print()
    prints('----------------------')
    print()
    printn("Okay, let's take it one by one.", npc = Tuttie)
    print()
    printn("First, there is Explore.", npc = Tuttie)
    printn("That lets you explore the world around you.", npc = Tuttie)
    print()
    printn("Second, is your Inventory.", npc = Tuttie)
    printn("You can view your items, use them, see stats and attributes, and more.", npc = Tuttie)
    print()
    printn("After that, is the Battle Box!", npc = Tuttie)
    printn("It's a really good place to earn xp, and to die...", npc = Tuttie)
    print()
    printn("Next is Roll Dice!", npc = Tuttie)
    printn("It just rolls a dice. for no reason really.", npc = Tuttie)
    print()
    printn("Then there is Options.", npc = Tuttie)
    printn("Change stuff, cheats, the works. Even organized like files.", npc = Tuttie)
    print()
    printn("Finally, there is back.", npc = Tuttie)
    printn("This sends you to the Universe Menu.", npc = Tuttie)
    printn("The screen before making a character...", npc = Tuttie)
    print()
    printn("Sorry if it was a lot, but did you get all of that?", npc = Tuttie)
    printn("If not, I can say it exactly the same way, as if I was programmed to say it.", npc = Tuttie)
    print()