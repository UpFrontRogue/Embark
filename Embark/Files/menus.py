from extras import *
from cheats import cheats
from clasd import create_universe, list_saved_universes, load_universe, save_universe, delete_universe, create_character, load_characters, delete_character, kill_character, save_character
from explore import explore, explore_more
from chard import view_inventory, use_item, toss_item, update_character
from uidd import *
from battle import battle_box
import sys

def main_menu():
    while True:
        print()
        prints("    Embark")
        prints(f'           v{version}')
        prints('----------------------')
        print()
        prints("1. Start New Universe¡")
        prints("2. Load Universe¡")
        prints("3. Options¡")
        prints("4. Leave")
        print()
        prints('----------------------')
        print()
        choice = inputs('Enter a Number: ')

        if choice == "1":
            create_universe()
        elif choice == "2":
            load_universe()
        elif choice == "3":
            options_menu()
        elif choice == "4":
            quit_game()
            break
        else:
            prints("Invalid choice. Please try again")
            print()

def options_menu(uid=None, character=None):
    while True:
        prints(' --Options--')
        print()
        prints('1. Cheats¡')
        prints('2. About¡')
        prints('3. Back')
        print()

        choice = inputs('Select an option:')
        print()

        if choice == '1':
            cheats(uid, character)
        elif choice == '2':
            prints('This is a unique game specially for me and my friends for D&D. Do not judge meanie')
            print()
        elif choice == '3':
            return
        else:
            prints('Invalid choice.')
            print()

def u_options_menu(uid):
    while True:
        prints(f' --Universe Options ({uid})-- ')
        print()
        prints('1. Add Item¡')
        prints('2. Add Enemy¡')
        prints('3. Add NPC¡')
        prints('4. Delete Universe¡')
        prints('5. Options¡')
        prints('6. Back')
        print()
        
        choice = inputs('Select an option: ',True, uid)
        print()
        if choice == '1':
            add_item(uid)
        elif choice == '2':
            add_enemy(uid)
        elif choice == '3':
            add_npc(uid)
        elif choice == '4':
            delete_universe(uid)
            main_menu()
        elif choice == '5':
            options_menu(uid)
        elif choice == '6':
            return
        else:
            prints('Invalid choice. Please choose again.')
            print()
            
def c_options_menu(uid, character):
    while True:
        prints(' --Character Options-- ')
        print()
        prints("1. Save Character¡")
        prints('2. Delete Character¡')
        prints('3. Update Character¡')
        prints('4. Universe Options¡')
        prints('5. Options¡')
        prints('6. Back')
        print()
        choice = inputs('Select an option: ', True, uid, character)
        
        if choice == '1':
            name = character['Name']
            save_character(uid, name, character)
        elif choice == '2':
            delete_character(uid, character['Name'])
            universe_menu(uid)
        elif choice == '3':
            update_character(uid, character)
        elif choice == '4':
            u_options_menu(uid)
        elif choice == '5':
            options_menu(uid, character)
        elif choice == '6':
            return
        else:
            prints('Invalid choice. Please try again.')

def universe_menu(uid):
    while True:
        prints(" --Universe Menu-- ")
        print()
        prints(f"       :{uid}")
        print()
        prints('1. Create New Character¡')
        prints('2. Load Characters¡')
        prints('3. Universal Quests¡')
        prints('4. Universe Options¡')
        prints('5. Main Menu')
        print()

        choice = inputs('Select an option: ', True, uid)

        if choice == '1':
            create_character(uid)
        if choice == '2':
            load_characters(uid)
        elif choice == '3':
            universe_quests(uid)
        elif choice == '4':
            u_options_menu(uid)
        elif choice == '5':
            main_menu()
        else:
            prints('Invalid choice. Please choose again.')

def character_menu(uid, character):
    while True:
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

        choice = inputs('Select an option: ',True, uid, character)

        if choice == '2':
            inventory_menu(uid, character)
        elif choice == '3':
            battle_box(uid, character)
        elif choice == '1':
            explore(uid, character)
        elif choice == '4':
            roll_dice('Useless Roll: ')
            print()
        elif choice == '5':
            c_options_menu(uid, character)
        elif choice == '6':
            universe_menu(uid)
        else:
            prints('Invalid choice. Please choose again.')
            print()
        
def inventory_menu(uid, character):
    while True:
        prints(' --Inventory-- ')
        print()
        prints(f"Name: {character['Name']}")
        prints(f"Level: {character['Stats']['Level']}")
        prints(f"HP: {character['Stats']['HP']} / {character['Stats']['Max HP']}")
        print()
        prints('Inventory:')
        print()
        view_inventory(character)
        print()
        prints('1. Use Items¡')
        prints('2. Toss Item¡')
        prints('3. Stats¡')
        prints('4. Attributes¡')
        prints('5. Back')
        print()
        choice = inputs('Select an option: ',True, uid, character)
        
        if choice == '1':
            use_item(uid, character)        
        elif choice == '2':
            toss_item(character)
        elif choice == '3':
            stats_menu(uid, character)
        elif choice == '4':
            attributes_menu(uid, character)
        elif choice == '5':
            return
        else:
            prints('Invalid choice. Please choose again.')
            print()

def stats_menu(uid, character):
    prints(f"Attack: {character['Stats']['Attack']}")
    prints(f"Defense: {character['Stats']['Defense']}")
    prints(f"Dodge: {character['Stats']['Dodge']}")
    prints(f"Crit: {character['Stats']['Crit']}")
    prints(f"Gold: {character['Stats']['Gold']}")
    print()
        
    if pro_mode:
        prints('1. Change Stats¡')
        prints('2. Back')
        print()
        choice = inputs('Select an Option: ',True, uid, character)
        
        if choice == '1':
            character['Stats']['Attack'] = int(inputs('Attack: ', False))
            character['Stats']['Defense'] = int(inputs('Defense: ', False))
            character['Stats']['Dodge'] = int(inputs('Dodge: ', False))
            character['Stats']['Crit'] = int(inputs('Crit: ', False))
            character['Stats']['Gold'] = int(inputs('Gold: ', False))
        elif choice == '2':
            return
        else:
            prints('Invalid. Returning')
        
def attributes_menu(uid, character): 
    for attribute, value in character['Attributes'].items():
        prints(f"{attribute}: {value}")
    print()
    
    if pro_mode is True:
        prints('1. Change Attributes¡')
        prints('2. Back')
        print()
        choice = inputs('Select an Option: ', True, uid, character)
        
        if choice == '1':
            character['Attributes']['Strength'] = int(inputs('Strength: ', False))
            character['Attributes']['Dexterity'] = int(inputs('Dexterity: ', False))
            character['Attributes']['Constitution'] = int(inputs('Constitution: ',False))
            character['Attributes']['Intelligence'] = int(inputs('Intelligence: ', False))
            character['Attributes']['Wisdom'] = int(inputs('Wisdom: ', False))
            character['Attributes']['Charisma'] = int(inputs('Charisma: ', False))
            name = character['Name']
            save_character(uid, name, character)
        elif choice == '2':
            return
        else:
            prints('Invalid. Returning')
    else:
        return
        
def quit_game():
    sys.exit()       