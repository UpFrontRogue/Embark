from extras import *
from found import iequip

import re
import random
import os
import pickle

def load_universe_by_uid(uid):
    universe_path = f"Saves/U {uid}/universe_{uid}.dat"
    if os.path.exists(universe_path):
        with open(universe_path, 'rb') as file:
            return pickle.load(file)
    else:
        return None

def create_universe():
    while True:
        prints("Enter A Valid Universe Number.")
        prints("(must be 2 letters followed by 5 numbers)")
        print()
        uid = inputs("Ex: AB12345: ").strip().upper()

        if not re.match(r'^[A-Z]{2}\d{5}$', uid):
            prints("Invalid Universe Number format. Please use 2 letters followed by 5 numbers.")
            print()
            break

        existing_universe = load_universe_by_uid(uid)

        if existing_universe:
            prints("A universe with the same UID already exists.")
            print()
            prints("1. Override the existing universe")
            prints("2. Add a new character to the existing universe")
            prints("3. Choose a new UID")
            print()
            choice = inputs("Select an option: ")

            if choice == "1":
                universe_data[uid] = {} 
                create_character(uid)
            elif choice == "2":
                create_character(uid) 
            elif choice == "3":
                continue
            else:
                prints("Invalid choice. Please try again.")
                print()
        else:
            # Create directory for the new universe
            universe_path = os.path.join("Saves", f"U {uid}")
            os.makedirs(universe_path, exist_ok=True)

            universe_data[uid] = {}
            save_universe(uid)
            create_character(uid)

def list_saved_universes():
    saved_universe_folders = [folder for folder in os.listdir("Saves") if os.path.isdir(os.path.join("Saves", folder))]
    return saved_universe_folders


def load_universe():
    from menus import universe_menu
    while True:
        saved_universes = list_saved_universes()

        if not saved_universes:
            prints("No saved universes found.")
            print()
            return

        prints("Saved Universes:")
        print()
        for i, folder_name in enumerate(saved_universes, start=1):
            uid = folder_name.split()[1]
            prints(f"{i}. Uid: {uid}")
        print()    
        try:
            choice = int(inputs("Enter the number of the universe to load (0 to cancel): "))

            if 1 <= choice <= len(saved_universes):
                selected_folder = saved_universes[choice - 1]
                uid = selected_folder.split()[1]
                universe_path = f"Saves/{selected_folder}/universe_{uid}.dat"
                with open(universe_path, 'rb') as file:
                    universe_data[uid] = pickle.load(file)
                prints(f"Universe: {uid} has been loaded.")
                print()
                universe_menu(uid)
                return
            elif choice == 0:
                return
            else:
                prints("Invalid choice. Please enter a valid number.")
                print()
        except ValueError:
            prints("Invalid input. Please enter a number.")
            print()

def save_universe(uid):
    universe_path = f"Saves/U {uid}/universe_{uid}.dat"
    try:
        with open(universe_path, 'wb') as file:
            pickle.dump(universe_data[uid], file)
        prints(f"Universe {uid} has been updated.")
        print()
    except Exception as e:
        prints(f"Error saving Universe {uid}: {str(e)}")
        print()

def delete_universe(uid):
    from menus import main_menu
    universe_path = f"Saves/U {uid}/universe_{uid}.dat"
    if os.path.exists(universe_path):
        choice = inputs(f"Are you sure you want to remove Universe {uid}? (confirm): ").strip().lower()
        if choice == 'confirm':
            del universe_data[uid]
            os.remove(universe_path)
            prints(f"Universe {uid} has been removed.")
            print()
        else:
            prints(f"Universe {uid} was not removed.")
            print()
    else:
        prints(f"No universe with UID {uid} found.")
        print()
    main_menu()
    
def create_character(uid):
    from menus import character_menu
    prints("Character Creation")
    print()
    name = inputs("Enter your character's name: ")
    if name == '':
        prints('Returning')
        return
    secret_attributes = {
                "Luck": 5,
                "Speed": 20
            }
    while True:
        prints("Basic Setup or Setup with a Dice Roll?")
        print()
        prints('1. Basic Setup')
        prints("2. Dice Setup")
        if pro_mode is True:
            prints("3. Manual Setup")
        prints('9. What do these mean?')    
        print()
    
        choice = inputs('Select an Option:')
    
        if choice == '1':
            a1 = random.randint(7, 17)
            prints(f'Strength: {a1}')
            a2 = random.randint(7, 17)
            prints(f'Dexterity: {a2}')
            a3 = random.randint(7, 17)
            prints(f'Constitution: {a3}')
            a4 = random.randint(7, 17)
            prints(f'Intelligence: {a4}')
            a5 = random.randint(7, 17)
            prints(f'Wisdom: {a5}')
            a6 = random.randint(7, 17)
            prints(f'Charisma: {a6}')
            attributes = {
                "Strength": a1,
                "Dexterity": a2,
                "Constitution": a3,
                "Intelligence": a4,
                "Wisdom": a5,
                "Charisma": a6
            }

            stats = {
                "HP": 15,
                "Max HP": 15,
                "Level": 1,
                "Gold": int(random.randint(1, 7) * random.randint(1, 5) * random.randint(1, 4)),
                "Attack": 5,
                "Defense": 5,
                "Dodge": 5,
                "Crit": 5,
                "XP": 0
            }
        
        elif choice == '2':
            attributes = {
                "Strength": roll_dice('Strength: '),
                "Dexterity": roll_dice('Dexterity: '),
                "Constitution": roll_dice('Constitution: '),
                "Intelligence": roll_dice('Intelligence: '),
                "Wisdom": roll_dice('Wisdom: '),
                "Charisma": roll_dice('Charisma: ')
            }

            stats = {
                "HP": 15,
                "Max HP": 15,
                "Level": 1,
                "Gold": int(roll_dice('Gold: ') * random.randint(2, 7)),
                "Attack": 5,
                "Defense": 5,
                "Dodge": 0,
                "Crit": 5,
                "XP": 0
            }        
        
        elif choice == '3' and pro_mode is True:
            attributes = {
            "Strength": int(inputs('Strength: ', False)),
            "Dexterity": int(inputs('Dexterity: ', False)),
            "Constitution": int(inputs('Constitution: ', False)),
            "Intelligence": int(inputs('Intelligence: ', False)),
            "Wisdom": int(inputs('Wisdom: ', False)),
            "Charisma": int(inputs('Charisma: ', False))
                }
            
            if debug_mode is True:
                prints('Please Enter Numbers for the following: ')
                print()
            
                stats = {
                    "HP": int(inputs('Starting HP: ', False)),
                    "Max HP": int(inputs('Max HP: ', False)),
                    "Level": int(inputs('Level: ', False)),
                    "Gold": int(inputs('Dabloons: ', False)),
                    "Attack": int(inputs('Attack: ', False)),
                    "Defense": int(inputs('Defense: ', False)),
                    "Dodge": int(inputs('Dodge: ', False)),
                    "Crit": int(inputs('Crit: ', False)),
                    "XP": 0
                }
                secret_attributes = {
                    "Luck": int(inputs('Luck: ', False)),
                    "Speed": int(inputs('Speed: ', False))
                }
            else:
                stats = {
                    "HP": int(inputs('Starting HP: ', False)),
                    "Max HP": int(inputs('Max HP: ', False)),
                    "Level": int(inputs('Level: ', False)),
                    "Gold": int(inputs('Dabloons: ', False)),
                    "Attack": 5,
                    "Defense": 5,
                    "Dodge": 0,
                    "Crit": 5,
                    "XP": 0
                }            
            
        elif choice =='9':
            prints('Automatic rolls a number between 7 and 17 for your Attributes.')
            prints('Max HP: 15. Starting gold Randomized')
            print()
            prints("Zachery's way rolls a number between 1 and 20 for your Attributes.")
            prints('Starting HP is 15 and Max HP is 25.')
            print()
            prints('if you know how to turn on pro mode... manual mode lets you put in numbers youself.')
            print()
        else:
            prints('Invalid. Returning.')
            print()
            return
        
        inventory = []
    
        while True:
            prints("Want a Tutorial?")
            print()
            prints('1. Yes')
            prints('2. No')
            print()
            choice = inputs('Select an option: ')
            print()
            if choice == '1':
                tutorial = True
                break
            elif choice == '2':
                tutorial = False
                break
            else:
                prints('Invalid choice. Choose again')   
                pass
    
        if tutorial:
            tutorials = {
                'CMT': True,
                'CT1': True,
                'BBT1': True
            }
        elif not tutorial:
            tutorials = {
                'CMT': False,
                'CT1': False,
                'BBT1': False
            }
        
        character = {
            "Name": name,
            "Stats": stats,
            "Attributes": attributes,
            "Secret Attributes": secret_attributes,
            "Equipment": iequip,
            "Inventory": inventory,
            "Tutorial" : tutorial,
            "Tutorials": tutorials
        }
        name = character['Name']
        save_character(uid, name, character)

        prints("Character Created:")
        print()
        prints(f"Name: {character['Name']}")
        prints(f"Level: {character['Stats']['Level']}")
        prints(f"HP: {character['Stats']['HP']}/{character['Stats']['Max HP']}")
        print()
        prints(f"Attack: {character['Stats']['Attack']}")
        prints(f"Defense: {character['Stats']['Defense']}")
        prints(f"Dodge: {character['Stats']['Dodge']}")
        prints(f"Crit: {character['Stats']['Crit']}")
        prints(f"Gold: {character['Stats']['Gold']}")
        print()
        prints('Inventory:')
        print()
        from chard import view_inventory
        view_inventory(character)
        print()
        prints("Attributes:")
        print()
        for attribute, value in character['Attributes'].items():
            prints(f"{attribute}: {value}")
        print()    
        prints('Do you want to choose a class?')
        prints('If not, you will get basic stats.')
        choice = inputs('Select an option: ')
        if character['Tutorials']['CT1'] is True:
            from tutorials import tuttie_menu
            tuttie_menu(uid, character)
        elif character['Tutorials']['CT1'] is False:
            character_menu(uid, character)

def load_characters(uid):
    from menus import character_menu
    if uid not in universe_data:
        prints(f"Universe {uid} was not found.")
        return

    characters = universe_data[uid].get('Characters', {})

    if not characters:
        prints(f"Universe {uid} has no characters.")
        return

    prints("Characters in this Universe:")
    print()
    for i, (char_name, char_data) in enumerate(characters.items(), start=1):
        level = char_data.get('Stats', {}).get('Level', 'Unknown') 
        prints(f"{i}. {char_name} (Level: {level})")
    print()
    
    try:
        choice = int(inputs("Enter the number of the character to load (0 to cancel): "))

        if 1 <= choice <= len(characters):
            char_names = list(characters.keys())
            selected_char_name = char_names[choice - 1]
            selected_character = characters[selected_char_name]
            prints(f"Character {selected_char_name} has been loaded.")
            print()
            character_menu(uid, selected_character)
        elif choice == 0:
            return
        else:
            prints("Invalid choice. Please enter a valid number.")
            print()
    except ValueError:
        prints("Invalid input. Please enter a number.")
        print()

def delete_character(uid, character_name):
    confirm = inputs(f"Are you sure you want to delete '{character_name}'? (yes/no): ").strip().lower()

    if confirm == 'yes':
        try:
            del universe_data[uid]['Characters'][character_name]  
            save_universe(uid)  
            prints(f"Character '{character_name}' has been deleted.")
            print()
        except KeyError:
            prints(f"Character '{character_name}' not found in universe '{uid}'.")
            print()

def kill_character(uid, character_name):
    try:
        del universe_data[uid]['Characters'][character_name]  
        save_universe(uid)  
        prints(f"'{character_name}' has been Terminated.")
        print()
    except KeyError:
        prints(f"Character '{character_name}' not found in universe '{uid}'.")

def save_character(uid, name, character):
    if uid not in universe_data:
        prints(f"No universe with UID {uid} found.")
        return

    characters = universe_data[uid].get('Characters', {})
    characters[name] = character

    universe_data[uid]['Characters'] = characters

    try:
        os.makedirs(f"Saves\\U {uid}", exist_ok=True)
        with open(f"Saves\\U {uid}\\universe_{uid}.dat", 'wb') as file:
            pickle.dump(universe_data[uid], file)
        prints(f"{name} has been saved.")
        print()
    except Exception as e:
        prints(f"Error saving character {name} in Universe {uid}: {str(e)}")
        print()
