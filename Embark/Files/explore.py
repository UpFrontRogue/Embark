from extras import *
from battle import battle
from found import *
import random

def item_find(character):
    ocs = [
            {'weight': 0.65, 'action': 'Craft'},
            {'weight': 0.35, 'action': 'Item'}
        ]
        
    outcome = random.choices(ocs, weights=[o['weight'] for o in ocs])[0]
        
    if outcome['action'] == 'Craft':
            item_pot = [i for i in cingr if i.forage and i.level <= character["Stats"]["Level"]]
            item = random.choice(item_pot)
    elif outcome['action'] == 'Item':
            item_pot = [i for i in items if i.forage and i.level <= character["Stats"]["Level"]]
            item = random.choice(item_pot)

    existing_item = next((i for i in character["Inventory"] if hasattr(i, 'name') and i.name == item.name), None)
    prints(f'You found {item.quantity} {item.name}.')

    if existing_item:
            existing_item.quantity += item.quantity
    else:
            prints(f'Description: {item.disc}')
            print()
            character["Inventory"].append(item)

def explore(uid, character):
    from menus import character_menu
    level = character['Stats']['Level']
    eweight = round(max(0.27, min(0.445, (0.27 + (0.0125 * (level - 1)) if level <= 13 else 0.42 - (0.0125 * (level - 14)) if 14 <= level <= 20 else 0.32 + (0.0125 * (level - 21)) if 21 <= level <= 32 else 0.445))), 3)
    bweight = round(max(0, min(0.005 * level, 0.13)), 3)
    fbweight = max(min(0.001 + ((0.001 * level) - 0.029), 0.1), 0)
    eroll = roll_dice(silent=True)
    cweight = round(((eroll * 0.0035) * ((eroll * 0.02) + 1)), 4)
    if debug_mode or pro_mode or giggles:
        prints(f'Enemy: {eweight}')
        prints(f'Boss: {bweight}')
        prints(f'Chest: {cweight}')
        print()
    outcomes = [
        {'weight': eweight, 'action': 'Enemy'},
        {'weight': 0.22, 'action': 'Npc'},
        {'weight': 0.06, 'action': 'Elite'},
        {'weight': bweight, 'action': 'Boss'},
        {'weight': 0.35, 'action': 'Extra'},
        {'weight': 0.01, 'action': 'Egg'},
        {'weight': cweight, 'action': 'Chest'},
        {'weight': fbweight, 'action': 'Final Boss'}
    ]

    outcome = random.choices(outcomes, weights=[o['weight'] for o in outcomes])[0]

    if outcome['action'] == 'Enemy':
        enemy = random.choice(enemies)
        def EnemyTestLevel(uid, character, enemy):
            while True:
                if enemy.base_level <= character['Stats']['Level']:
                    battle(uid, character, enemy)
                    break
                elif enemy.base_level > character['Stats']['Level']:
                    enemy = random.choice(enemies)
                else:
                    prints('Test Fail')
                    explore(uid, character)
        EnemyTestLevel(uid, character, enemy)
    elif outcome['action'] == 'Npc':
        npc = random.choice(npcs)
        def NpcTestLevel(uid, character, npc):
            while True:
                if npc.base_level <= character['Stats']['Level']:
                    talk(uid, character, npc)
                    break
                elif npc.base_level > character['Stats']['Level']:
                    npc = random.choice(npcs)
                else:
                    prints('Test Fail')
                    explore(uid, character)
        NpcTestLevel(uid, character, npc)
    elif outcome['action'] == 'Elite':
        level_req = character['Stats']['Level']
        enemy_pool = []
        for e in elites:
            if e.base_level <= level_req:
                enemy_pool.append(e)
        enemy = random.choice(enemy_pool)
        if character['Stats']['Level'] >= 9:
            prints('Elite Incoming!')
            battle(uid, character, enemy)
        elif character['Stats']['Level'] < 9:
            prints(f'Elite {enemy.name} Ahead! Proceed?')
            prints('(this goes away after level 9.)')
            print()
            prints('1. Yes')
            prints('2. No')
            print()
            choice = inputs('Select an option: ')

            if choice == '1':
                prints('Elite Incoming!')
                print()
                battle(uid, character, enemy)
            elif choice == '2':
                prints('Returning.')
                print()
                character_menu(uid, character)
    elif outcome['action'] == 'Boss':
        enemy = random.choice(bosses)
        if character['Stats']['Level'] >= (enemy.level - 2):
            prints('Boss Incoming!')
            print()
            battle(uid, character, enemy)
        elif character['Stats']['Level'] < (enemy.level - 2):
            enemy = random.choice(bosses)
            prints('High Level Boss Ahead! Proceed?')
            print()
            prints('1. Yes')
            prints('2. No')
            print()
            choice = inputs('Select an option: ')

            if choice == '1':
                prints('Boss Incoming!')
                print()
                battle(uid, character, enemy)
            elif choice == '2':
                prints('Returning.')
                print()
                character_menu(uid, character)
    elif outcome['action'] == 'Extra':
        explore_more(uid, character)
    elif outcome['action'] == 'Egg':
        easter_eggs()
    elif outcome['action'] == 'Final Boss':
        prints('Death-Magedon Ahead! Run or Die!')
        enemy = random.choice(final_boss)
        battle(uid, character, enemy)
    elif outcome['action'] == 'Chest':
        treasure(uid, character)

def explore_more(uid, character):
    level = character['Stats']['Level']
    eweight = round(max(0.19, min(0.27, (0.19 + (0.005 * (level - 1))))), 3)
    if giggles:
        prints(f'Enemy: {eweight}')
        print()
    outcomes = [
        {'weight': eweight, 'action': 'Enemy'},
        {'weight': 0.35, 'action': 'Item'},
        {'weight': 0.15, 'action': 'Merchant'},
        {'weight': 0.075, 'action': 'Shop'},
        {'weight': 0.15, 'action': 'Encounter'},
        {'weight': max(0.08 - (0.01 * level), 0) , 'action': 'Fail'}
    ]
    
    outcome = random.choices(outcomes, weights=[o['weight'] for o in outcomes])[0]

    if outcome['action'] == 'Enemy':
        enemy = random.choice(enemies)
        def EnemyTestLevel(uid, character, enemy):
            while True:
                if enemy.base_level <= character['Stats']['Level']:
                    battle(uid, character, enemy)
                    break
                elif enemy.base_level > character['Stats']['Level']:
                    enemy = random.choice(enemies)
                else:
                    prints('Test Fail')
                    explore(uid, character)
        EnemyTestLevel(uid, character, enemy)
    elif outcome['action'] == 'Item':
        item_find(character)
    elif outcome['action'] == 'Merchant':
        merchant(uid, character)
    elif outcome['action'] == 'Shop':
        shop(uid, character)
    elif outcome['action'] == 'Encounter':
        npc = random.choice(npcs)
        encounter(uid, character, npc)
    elif outcome['action'] == 'Fail':
        prints('You failed to find anything. Shame really')
        print()

def encounter(uid, character, npc):
    if npc.uid is None:
        npc.uid = uid
    if npc.name == 'Sir Lance':
        printn(f"WHY HELLO! Fellow Traveler!", npc = npc)
        print()
        prints('You go to start making conversation, and then realize they were talking to someone else behind you.')
        print()
        prints('Actually upon further inspection they are talking to no one behind you, like a loonie.')
    else:
        printn(f"Hello I'm a level {npc.level}.", npc = npc)
        printn(f"I come from the universe {npc.uid}", npc = npc)
        print()
        prints('You watch as they walk away, like you knew what that mean.')
        print()

def easter_eggs():
    eggs = [
        {'weight': 1, 'description': 'A fiery yellow and orange headed precursor walks past you.', 'follow_up': 'Stranger: They say he has dark eco in him...'},
        {'weight': 1, 'description': 'You see a really small man running, almost like an ant or ladybug.'},
        {'weight': 1, 'description': 'Farmer: Hey, watch me eat this.', 'follow_up': 'You watch them eat a purple star-shaped fruit, starting to glow purple for a moment. They '}
    ]

    selected_egg = random.choice(eggs)
    description = selected_egg['description']
    follow_up = selected_egg.get('follow_up', None)

    prints(description)
    print()

    if follow_up:
        prints(follow_up)
        print()

def talk(uid, character, npc):
    while True:
        printn(f'Hello', npc= npc)
        print()
        prints('1. Hey')
        prints('2. *walk off*')
        print()
        choice = inputs('Select an option: ')

        if choice == '1':
            printn(f'congrats on getting this far', npc = npc)
            printn(f'keep it up!', npc = npc)
            character['Stats']['XP'] += 3
            print()
            break
        elif choice == '2':
            prints('You walked away from them.')
            print()
            break

def buy_item(character, item, price, merch):
    if character['Stats']['Gold'] >= price:
        character['Stats']['Gold'] -= price
        character['Inventory'].append(item)
        item.quantity -= 1
        if item.quantity <= 0:
            merch.pop(merch.index(item))
        prints(f"You bought {item.name} for {price} gold.")
    else:
        prints("You don't have enough gold to buy this item.")

def merchant(uid, character):
    m_class = random.randint(1, 3)
    prints(f'A Class {m_class} Merchant walks by you.')
    prints('Buy from them?')
    print()
    prints('1. Yes')
    prints('2. No')
    print()
    choice = inputs('Select an Option: ')

    if choice == '1':
        merch = []
        for item0 in items:
            if item0.level <= character['Stats']['Level']:
                merch.append(item0)
        if m_class >= 2:
            for item1 in equipment:
                if item1.level <= character['Stats']['Level']:
                    merch.append(item1)
        if m_class >= 3:
            for item2 in cores:
                if item2.level <= character['Stats']['Level']:
                    merch.append(item2)

        ints = [3, 4, 5, 6, 7, 9, 13]
        cint = min(random.choice(ints), len(merch))
        minv = random.sample(merch, cint)
        qc = [0.25, 0.35, 0.55, 0.85, 1.15, 1.35, 1.45, 1.65, 1.85, 5.67]
        for item in minv:
            quant = int(random.choice(qc) * item.quantity)
            item.quantity = max(quant, 1)
            gold = item.gold
            char = character['Attributes']['Charisma']
            inflate = round((char * (-0.05)) + 1.65, 2)
            sellp = int(round(gold * inflate, 0))
            item.gold == sellp


        while minv:
            cgold = character['Stats']['Gold']
            prints(f'Gold: {cgold}')
            print()
            for i, item in enumerate(minv, start=1):
                prints(f'{i}. {item.name} ({item.quantity}) [{sellp}] ')
                if debug_mode:
                    prints(f'   Gold: {gold}, Inflate: {inflate}')
            print()
            choice = inputs('Select an item to buy (0 to cancel): ')
            if choice.isdigit():
                choice = int(choice)
                if 0 < choice <= len(minv):
                    selected_item = minv[choice - 1]
                    gold_cost = int(selected_item.gold)
                    minv == buy_item(character, selected_item, gold_cost, minv)
                elif choice == 0:
                    prints("You and the Merchant parted.")
                    break
                else:
                    prints("Invalid choice. Please try again.")
            else:
                prints("Invalid input. Please enter a number.")
    
def shop(uid, character):
    founds = ['found', 'located', 'come across', 'stop at']
    fc = random.choice(founds)
    shop_types = ['pop-up','wooden','quaint','lively']
    stype = random.choice(shop_types)
    prints(f'You {fc} a {stype} Shop.')
    print()
    merch = []
    for item0 in items:
        sip = random.randint(2, 4)
        if item0.level <= (character['Stats']['Level'] + sip):
            merch.append(item0)
    for item1 in cores:
        if item1.level <= (character['Stats']['Level'] - 4):
            merch.append(item1)
    for item2 in equipment:
        if item2.level <= character['Stats']['Level']:
            merch.append(item2)

    ints = [6, 7, 9, 10, 11, 13, 17]
    cint = min(random.choice(ints), len(merch))
    minv = random.sample(merch, cint)
    qc = [0.55, 0.5, 0.65, 0.75, 0.95, 1.05, 1.15, 0.85, 1.15, 1.35, 1.45, 1.65, 1.85, 1.95, 2.1, 2.25, 4.25]
    for item in minv:
        quant = int(random.choice(qc) * item.quantity)
        item.quantity = max(quant, 1)
        gold = item.gold
        char = character['Attributes']['Charisma']
        shop_pot = [-0.05, -0.06, -0.07]
        shop_diff = random.choice(shop_pot)
        if shop_diff == -0.05:
            shop_neg_inflate = 1.65
        elif shop_diff == -0.06:
            shop_neg_inflate = 1.78
        elif shop_diff == -0.07:
            shop_neg_inflate = 1.91
        inflate = round((char * (shop_diff)) + shop_neg_inflate, 2)
        sellp = max(int(round(gold * inflate, 0)), 1)
        item.gold == sellp


    while minv:
        cgold = character['Stats']['Gold']
        prints(f'Gold: {cgold}')
        print()
        for i, item in enumerate(minv, start=1):
            prints(f'{i}. {item.name} ({item.quantity}) [{item.gold}] ')
        print()
        choice = inputs('Select an item to buy (0 to cancel): ')
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(minv):
                selected_item = minv[choice - 1]
                gold_cost = int(selected_item.gold)
                minv == buy_item(character, selected_item, gold_cost, minv)
            elif choice == 0:
                prints("You walked away from the shop.")
                break
            else:
                prints("Invalid choice. Please try again.")
        else:
            prints("Invalid input. Please enter a number.")

def treasure(uid, character):
    prints('You Found a Treasure.')
    print()
    titem = random.randint(2,5)
    tcore = random.randint(0,1)
    tingr = random.randint(3,5)
    tequip = random.randint(1,3)
    treasure_pool = []
    treasure_pool.extend(random.sample(items, titem))
    if tcore == 1:
        treasure_pool.append(random.choice(cores))
    treasure_pool.extend(random.sample(cingr, tingr))
    treasure_pool.extend(random.sample(equipment, tequip))
    prints('Items in Chest')
    print()
    amount = random.randint(3, 7)
    treasure = random.sample(treasure_pool, amount)
    
    for i, item in enumerate(treasure, start=1):
        prints(f'{i}. {item.name}')
        existing_item = next((i for i in character["Inventory"] if hasattr(i, 'name') and i.name == item.name), None)
        if existing_item:
            existing_item.quantity += item.quantity
        else:
            character["Inventory"].append(item)
    print()
    prints('Items added to your inventory.')
    print()