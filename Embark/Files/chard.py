from extras import *
from clasd import save_character

def use_item(uid, character, enemy=None):
    n = True
    inventory = view_inventory(character, n)
    print()
    prints('Choose a number of the item to use.')
    choice = int(inputs('Select an Item to use (0 to cancel): '))

    if 1 <= choice <= len(inventory):
        uitem = inventory[choice - 1]
        if isinstance(uitem, Item):
            if uitem.consume or uitem.equip:
                prints(f"You used {uitem.name}.")
                if uitem.consume:
                    apply_item_effect(uitem, character)
                    uitem.quantity -= 1
                    if uitem.quantity == 0:
                        character['Inventory'].remove(uitem)
                elif uitem.equip:
                    if not uitem.equipped:
                        uitem.quantity -= 1
                        uitem.equipped = True
                        apply_item_effect(uitem, character)
                    elif uitem.equipped:
                        uitem.quantity += 1
                        uitem.equipped = False
                        apply_item_effect(uitem, character)
        elif isinstance(uitem, Ingr):
            if uitem.consume:
                prints(f"You used {uitem.name}.")
                apply_item_effect(uitem, character, enemy=None)
                uitem.quantity -= 1
                if uitem.quantity == 0:
                    character['Inventory'].remove(uitem)
            from clasd import save_character
            save_character(uid, character['Name'], character)

    elif choice == 0:
        return
    else:
        prints('Invalid choice. Please choose a valid item.')

def apply_item_effect(item, character, enemy=None):
    if item.effect == 'Heal':
        maxhp = character["Stats"]["Max HP"]
        character['Stats']['HP'] += item.amount
        character['Stats']['HP'] = min(character['Stats']['HP'], maxhp)
    elif item.effect == 'Damage':
        if enemy is not None:
            enemy.hp -= item.amount
            prints(f"You Damaged {enemy.name} for {item.amount} Damage.")
        else:
            prints("Are you Sure?")
            print()
            choice = inputs('Yes or No: ')
            if choice.lower() == "yes":
                character["Stats"]["HP"] -= item.amount
    elif item.effect == 'Equip Attr':
        if item.attribute == 'Defense':
            iattribute = character['Stats']['Defense']
            if item.equipped:
                iattribute += item.amount
            else:
                iattribute -= item.amount
            character['Stats']['Defense'] = max(0, iattribute)  # Ensure attribute doesn't go below 0

def toss_item(character):
    n = True
    inventory = view_inventory(character, n)
    print()
    if inventory:
        prints('Choose a number of the item to throw out.')
        print()
        choice = int(inputs('Select an Item to toss (0 to cancel): '))
        if 1 <= choice <= len(inventory):
            tItem = inventory[choice - 1]
            character['Inventory'].remove(tItem)
        
def view_inventory(character, n=False):
    inventory = character['Inventory']
    if not inventory:
        prints("Your inventory is empty.")
        print()
    else:
        for i, item in enumerate(inventory, start=1):
            if isinstance(item, dict):
                prints(f'{i}. {item["name"]}')
                if giggles:
                    prints("[]")
            else:
                quantity = item.quantity
                name = item.name
                if quantity == 1 and n:
                    prints(f'{i}. {name}')
                elif quantity == 1:
                    prints(f'{name}')
                elif quantity >= 2 and n:                    
                    prints(f'{i}. {name} * {quantity}')
                elif quantity >= 2:
                    prints(f'{name} * {quantity}')
                if giggles:
                     prints(".")
        return inventory
        print()

def update_character(uid, character):
    # Updating Equipment
    if 'Equipment' in character:
        if 'Hand_1' in character['Equipment']:
            character['Equipment']['Main Hand'] = character['Equipment'].pop('Hand_1')
        if 'Hand_2' in character['Equipment']:
            character['Equipment']['Off Hand'] = character['Equipment'].pop('Hand_2')
        if 'Boots' in character['Equipment']:
            character['Equipment']['Feet'] = character['Equipment'].pop('Boots')
        if 'Necklace' in character['Equipment']:
            character['Equipment']['Neck'] = character['Equipment'].pop('Necklace')
        if 'Ring' not in character['Equipment']:
            character['Equipment']['Ring'] = None
    if 'Equipment' not in character:
        character['Equipment'] = {
            "Head": None,
            "Neck": None,
            "Chest": None,
            "Arms": None,
            "Main Hand": None,
            "Off Hand": None,
            "Ring": None,
            "Legs": None,
            "Feet": None
        }

    # Updating missing attributes
    if 'Secret Attributes' not in character:
        character['Secret Attributes'] = {
            "Luck": 5,
            "Speed": 20
        }

    if 'Tutorial' not in character:
        character['Tutorial'] = False

    if 'Tutorials' not in character:
        character['Tutorials'] = {
            'CT1': False,
            'BBT1': False
        }

    if 'Beastiary' not in character:
        character['Beastiary'] = []

    if 'Extra Details' not in character:
        character['Extra Details'] = {
        "UID": uid,
        "Handed": "Right",
        "Eyes": "Brown",
        "Hair": "Blonde",
        "Skin": "Pale",
        "Class": None,
        "Race": "Human",
        "Gender": "Non-Binary",
        "Features": ""
    }

    if 'Attacks' not in character:
        character['Attacks'] = [
            Attack('Punch', 'Physical', 8, 3, 5, 1.5, 20),
            Attack('Slap', 'Physical', 1, 0, 2, 2, 12),
            Attack('Magic Bolt', 'Magical', 10, 4, 1, 3.25, 18),
        ]

    # Save the updated character
    save_character(uid, character['Name'], character)
