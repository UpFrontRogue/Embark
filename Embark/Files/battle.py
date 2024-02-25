from found import iequip, Npc, Enemy, Item, items, cingr, enemies, elites, bosses, jbosses, final_boss, names, npcs
from extras import *
from clasd import save_character, kill_character
import random

def update_enemy(uid, character, e):
    benemy = Enemy(e.name, e.race, e.base_level, e.level, e.hp, e.max_hp, e.attack, e.defense, e.sdefense, e.crit, e.speed, e.dodge, e.xp, e.gold, e.rank)
    if benemy.level >= (character['Stats']['Level'] + 2) and benemy.race != 'Boss':
        benemy.level = random.randint(1, character['Stats']['Level'] + 2)
    be_stats = (benemy.level - 1)
    diff = [0, 0.1, 0.25, 0.5, 0.75, 0.95, 1, 1.05, 1.25, 1.35, 1.5, 1.75, 1.85, 1.95, 2, 2.33]
    beinc = int(be_stats * random.choice(diff))
    g = "Godly "
    prefixes = ["Chaotic ", "Wild ", "Timid ", "Cute ", "Tired ", "Strong ", "Weak ", "Giant ", "Towering ", '']
    prefix = random.choice(prefixes)
    gtest = random.randint(0,100)
    if gtest == 69:
        prefix = g
    edif = 0
    if prefix != '':
        if prefix == "Chaotic ":
            benemy.speed += 6
            benemy.attack += random.randint(2,5)
            benemy.sdefense += 4
            benemy.defense -= 4
            beinc += 3
        elif prefix == "Godly ":
            edif += 666
            b1bd = random.randint(4,12)
            newbeinc = int(beinc * b1bd)
            beinc = newbeinc
        elif prefix == "Timid ":
            benemy.attack -= 2
            benemy.speed -= 3
            benemy.defense += 4
            benemy.sdefense += 1
        elif prefix == "Cute ":
            benemy.speed += 2
            benemy.crit += 5
            benemy.defense += 3
        elif prefix == "Tired ":
            benemy.speed -= 4
            benemy.defense -= 2
            benemy.attack -= 1
            beinc -= 1
        elif prefix == "Strong ":
            benemy.attack += random.randint(3, 6)
            benemy.defense += 2
        elif prefix == "Giant ":
            benemy.defense += 4
            benemy.sdefense += 3
            benemy.speed -= 2
            benemy.attack += 2
        elif prefix == "Towering ":
            benemy.defense += 5
            benemy.sdefense += 4
            benemy.speed -= 3
            benemy.attack += 4
        elif prefix == 'Wild ':
            benemy.level += 1
            benemy.hp += 7
            benemy.attack += 3
            
    prints(f"A {prefix}level {benemy.level} {benemy.name} appeared!")
    print()
    if nerd_stats:
        prints(f'Enemy Stats Increased: {beinc}')
    difficulty = [0.9,.95,0.85,1.05,1.1,1.15,1.2,0.8,0.75,0.7,0.65, 1.3, 1.5,1.12]
    if edif == 0:
        edif = random.choice(difficulty)
    lug = int((beinc * edif) / 4.2)
    ainc = [0.5, 1, 1.5, 2, 5]
    xpm = round((beinc * 0.005) + 1, 2)
    newxp = round(benemy.xp * xpm, 1)
    benemy.xp = newxp
    if nerd_stats:
        prints(f'XP Multiplier: {xpm}')
    while beinc > 0:
        outcomes = [
            {'Weight': 2.25, 'Stat': 'HP', 'Inc': 'max_hp', 'Amount': min(random.randint(2,7) + lug, 25)},
            {'Weight': 1.25, 'Stat': 'Attack', 'Inc': 'attack', 'Amount': min(random.choice(ainc) + lug, 5)},
            {'Weight': 1, 'Stat': 'Defense', 'Inc': 'defense','Amount': min(1 + lug, 5)},
            {'Weight': 1, 'Stat': 'Sp Defense', 'Inc': 'sdefense','Amount': min(1 + lug, 5)},
            {'Weight': 2, 'Stat': 'Crit', 'Inc': 'crit', 'Amount': min(random.randint(1,3) + lug, 3)},
            {'Weight': .2, 'Stat': 'Speed', 'Inc': 'speed', 'Amount': min(1 + lug, 3)},
            {'Weight': 2, 'Stat': 'Dodge', 'Inc':'dodge', 'Amount': min(random.randint(1, 2) + lug, 3)}
        ]
        
        outcome = random.choices(outcomes, weights=[o['Weight'] for o in outcomes])[0]
        
        if outcome['Stat']:
            proes = outcome['Stat']
            proea = outcome['Amount']
            einc = getattr(benemy, outcome['Inc'])
            setattr(benemy, outcome['Inc'], einc + outcome['Amount'])
            if outcome['Stat'] == 'HP':
                benemy.hp += outcome['Amount']
            if nerd_stats:
                prints(f'{proes}: {proea}')
        
        beinc -=1
    if benemy.dodge > 80:
        max_dodge = min(benemy.dodge, 80)
        benemy.dodge = max_dodge
    if benemy.speed > 100:
        max_speed = min(benemy.speed, 100)
        benemy.speed = max_speed
    return benemy

def battle_box(uid, character):
    enemy = random.choice(enemies)
    def EnemyTestLevel(uid, character, enemy):
        while True:
            if enemy.base_level <= character['Stats']['Level']:
                enemy = random.choice(enemies)
                battle(uid, character, enemy)
                another = battle(uid, character, enemy)
                if another == 1:
                    enemy = random.choice(enemies)
            elif enemy.base_level > character['Stats']['Level']:
                enemy = random.choice(enemies)
    EnemyTestLevel(uid, character, enemy)

def battle(uid, character, enemy):
    from menus import character_menu, universe_menu
    global next_choice

    benemy = update_enemy(uid, character, enemy)
    analyzed = False
    damaged = False
    turn = 0
    c_speed = 0
    e_speed = 0
    xpa = 1.00
    cbd = ((character['Attributes']['Strength'] / 2) + character['Stats']['Attack']) - (benemy.defense - (character['Stats']['Attack'] * 0.4))
    cdamage = cbd
    ebd = round((((benemy.attack - character['Stats']['Defense']) / (character['Attributes']['Constitution'] / 5)) - 0.5), 1)
    edamage = ebd
    sbd = round((((character['Attributes']['Intelligence'] / 5) + (character['Attributes']['Wisdom'] / 3)) - (benemy.sdefense - (character['Stats']['Attack'] * 0.4)) - 3), 1)
    sdamage = sbd
    cspd = int(22 - (character['Secret Attributes']['Speed'] / 8))
    if nerd_stats:
        prints(f'C Speed: {cspd}')
    while character['Stats']['HP'] > 0 and benemy.hp > 0:
        turn += 1
        prints(f'     Turn: {turn}')
        if character['Stats']['HP'] >= character['Stats']['Max HP']:
            character['Stats']['HP'] = character['Stats']['Max HP']
        prints(f"Player HP: {character['Stats']['HP']}")
        if analyzed or debug_mode or pro_mode is True:
            prints("Enemy HP:", benemy.hp)
        print()
        
        c_speed += character['Secret Attributes']['Speed']
        
        aps = sdamage
        ps = '?'
        if character['Secret Attributes']['Speed'] > benemy.speed:
            ps = 'Can Outrun'
        else:
            pss = (50 + (character['Secret Attributes']['Speed'] - benemy.speed))
            ps = str(f'{pss}%')
        if aps < 0:
            aps = 0
        if character['Stats']['HP'] > 0 and c_speed >= cspd:
            c_speed -= cspd
            prints(' Characters Turn. ')
            print()
            if cdamage <= 0:
                fd = cdamage
                tr = 5
                while fd <= 0: 
                    rd = ((tr / 2) - 2) + cdamage
                    if rd <= 0:
                        tr += 1
                    fd = rd
                bar = f"[{tr}]"
            else:
                bar = f"({cdamage})"
            if sdamage <= 0:
                md = sdamage
                tr2 = 5
                while md <= 0:
                    rd2 = ((tr2) - 4) + sdamage
                    if rd2 <= 0:
                        tr2 += 1
                    md = rd2
                bar2 = f"[{tr2}]"
            else:
                bar2 = f"({sdamage})"
            prints(f"1. Basic Attack {bar}")
            prints(f"2. MP Attack {bar2}")
            prints(f"3. Block ({character['Attributes']['Constitution']})")
            prints(f"4. Analyze ({character['Attributes']['Intelligence']})")
            prints(f"5. Run ({ps})")
            if analyzed:
                prints(f'   Damage Taking: {edamage}')
            print()    
            choice = inputs("Enter your action: ")
            if choice == "1":
                outcomes = [
                    {'Weight': ((0 + benemy.dodge / 100) * (character['Attributes']['Dexterity'] / 20)), 'Action': 'Dodge'},
                    {'Weight': ((1 - benemy.dodge / 100) / (character['Attributes']['Dexterity'] / 20)), 'Action': 'Hit'}
                ]
            
                outcome = random.choices(outcomes, weights=[o['Weight'] for o in outcomes])[0]
            
                if outcome['Action'] == 'Dodge':
                    prints(f'You missed the {benemy.name}.')
                    e_speed -= 10
                elif outcome['Action'] == 'Hit':
                    if next_choice != 0:
                        base_roll = next_choice
                        prints(f'Next Choice: {next_choice}')
                        next_choice = 0
                    else:
                        base_roll = roll_dice('Strength Roll: ')
                    print()
                    if base_roll == 1:
                        roll_damage = 0
                        prints('You tried to hit them but you fell. You lost the turn.')
                    elif base_roll ==  20:
                        roll_damage = max((base_roll + cdamage), 0)
                        prints('Perfect Attack. They could do nothing.')
                        benemy.hp -= roll_damage
                        prints(f"You dealt {roll_damage} damage to the {benemy.name}.")
                        damaged = True
                    else:
                        roll_damage = max(((base_roll / 2) - 2) + cdamage, 0)
                        benemy.hp -= roll_damage
                        prints(f"You dealt {roll_damage} damage to the {benemy.name}.")
                print()
                pass
            elif choice == "2":
                base_roll = roll_dice('Magic Roll: ')
                print()
                true_roll = ((base_roll ) - 4) + sdamage
                benemy.hp -= true_roll
                if true_roll <= 0:
                    true_roll = 0
                prints(f"You dealt {true_roll} damage to the {benemy.name}.")
                print()
                pass
            elif choice == "3":
                prints('You attempt to block.')
                print()
                base_roll = roll_dice('Constitution Roll: ')
                true_roll = (base_roll - 2) + (character['Attributes']['Constitution'] / 3)
                true_damage = max(edamage - (true_roll * .6), 0)
                if true_damage <= 0:
                    true_damage = 0
                prints(f'Damage Taken: {true_damage}')
                print()
                character['Stats']['HP'] -= round(true_damage, 4)
                damaged = True
                if base_roll == 20:
                    prints(f'Perfect Block. You counter attacked dealing {((cdamage + 5)* 1.5)} damage!')
                    print()
                    benemy.hp -= ((cdamage + 5) * 1.5)
                pass
            elif choice == "4":
                if analyzed:
                    prints(f"Level: {analyzed_details}")
                    
                if not analyzed:
                    prints(f"You analyze the {benemy.name}.")
                    print()
                    total_information = roll_dice('Inetelligence Roll: ') + (character['Attributes']['Intelligence'] / 3)
                
                    if total_information > 6.66: 
                        detail_level = "Minimal"
                        if total_information >= 11:
                            detail_level = "Average"
                            if total_information >= 13.33:
                                detail_level = "Moderate"  
                                if total_information > 17.65:   
                                    detail_level = "Detailed"
                    else:
                        detail_level = "Unknown"
                    analyzed_details = []  

                    if detail_level == "Detailed":
                        analyzed = True
                        if turn != 0:
                            if turn == 1:
                                xpa = 1.75
                            elif turn == 2:
                                xpa = 1.55
                            elif turn == 3:
                                xpa = 1.375
                            else:
                                xpa = 1.35
                        prints(f"Level: {benemy.level}")
                        prints(f"HP: {benemy.hp}/{benemy.max_hp}")
                        prints(f"Attack: {benemy.attack}")
                        prints(f"Defense: {benemy.defense}")
                        prints(f"Crit: {benemy.crit}")
                        prints(f"Speed: {benemy.speed}")
                        prints(f"Dodge: {benemy.dodge}")
                        prints(f"XP: {benemy.xp}")
                        prints(f"Gold: {benemy.gold}")

                        analyzed_details.extend(["Level", "HP", "Attack", "Defense", "Crit", "Speed", "Dodge", "XP", "Gold"])
                    elif detail_level == "Moderate":
                        prints(f"Level: {benemy.level}")
                        prints(f"HP: {benemy.hp}/{benemy.max_hp}")
                        prints(f"Attack: {benemy.attack}")
                        prints(f"Defense: {benemy.defense}")
                        prints(f"Speed: {benemy.speed}")
                        prints(f"XP: {benemy.xp}")

                    elif detail_level == "Average":
                        prints(f"HP: {benemy.hp}/{benemy.max_hp}")
                        prints(f"Attack: {benemy.attack}")
                        prints(f"Defense: {benemy.defense}")
                        prints(f"XP: {benemy.xp}")

                        analyzed_details.extend(["Level", "HP", "Attack", "XP"])
                    elif detail_level == "Minimal":
                        prints(f"HP: {benemy.hp}/{benemy.max_hp}")
                        prints(f"XP: {benemy.xp}")

                        analyzed_details.extend(["Level", "XP"])
                    else:
                        prints('You failed to learn anything useful.')
                        analyzed_details.extend(["?"] * 9)
                    print()
                else:
                    prints("You know everything about this enemy")
            elif choice == "5":
                if character['Secret Attributes']['Speed'] > benemy.speed:
                    prints(f"You outran the {benemy.name}.")
                    print()
                    character_menu(uid, character)
                else:
                    prints("You attempt to run from the battle.")
                    print()
                    outcomes = [
                        {'weight': (50 - character['Secret Attributes']['Speed'] + benemy.speed), 'action': 'Stay'},
                        {'weight': (50 + character['Secret Attributes']['Speed'] - benemy.speed), 'action': 'Run'},
                    ]

                    outcome = random.choices(outcomes, weights=[o['weight'] for o in outcomes])[0]
                
                    if outcome['action'] == 'Stay':
                        prints('You failed to run away.')
                        print()
                    elif outcome['action'] == 'Run':
                        prints(f'You ran away from the {benemy.name}')
                        print()
                        character_menu(uid, character)
        e_speed += benemy.speed                
        if benemy.hp > 0 and e_speed >= 20:   
            if damaged is True:
                e_speed -= 20
                prints('Enemy Turn Used.')
                damaged = False
                next
            else:
                while benemy.hp > 0 and e_speed >= 20:
                    prints("Enemy's Turn")
                    print()
                    edam = round(max(edamage, 0), 3)
                    character['Stats']['HP'] -= edam
                    prints(f'You took {edam} damage')
                    e_speed -= 20
                    if debug_mode is True:
                        prints(f'Benemy Speed: {e_speed}')
                    damaged = False
        if benemy.race is not None and benemy.hp > 0:
            if debug_mode and turn == 1:
                prints(f'Enemy Race: {benemy.race}')
                print()
            if benemy.race == 'Human':
                benemy.hp += .5
                if pro_mode:
                    prints('Enemy healed for 0.5 HP.')
                    print()
            elif benemy.race == 'Morg':
                sdef = [0.5, 1, 3, -1]
                benemy.defense -= 1
                benemy.sdefense -= random.choice(sdef)
                benemy.attack += 3
                if pro_mode:
                    prints('The Morg shifted.')
                    print()
            elif benemy.race == 'Wolf':
                benemy.crit += 2
                benemy.attack +- 2
                benemy.dodge += 1
                if pro_mode:
                    prints('The wolf grew vigorous.')
                    print()
            elif benemy.race == 'Mutant':
                boosts = [
                   {'weight': .15, 'action': 'Atk', 'inc': 'attack', 'amt': 3},
                   {'weight': .30, 'action': 'Def', 'inc': 'defense', 'amt': 2},
                   {'weight': .10, 'action': 'Speed', 'inc': 'speed', 'amt': 2},
                   {'weight': .25, 'action': 'Dodge', 'inc': 'dodge', 'amt': random.randint(1,2)},
                   {'weight': .35, 'action': 'HP', 'inc': 'hp', 'amt': random.randint(7,22)}
                ]
                outcome = random.choices(boosts, weights=[o['weight'] for o in boosts])[0]
                dec = [True, False]
                tdec = random.choice(dec)
                if outcome['action']:
                    einc = getattr(benemy, outcome['inc'])
                    setattr(benemy, outcome['inc'], einc + outcome['amt'])
                    if pro_mode or debug_mode:
                        action = outcome['action']
                        iamt = outcome['amt']
                        prints(f'The Mutant increased {action}: {iamt}')
                        print()
                if tdec:
                    doc = random.choices(boosts, weights=[o['weight'] for o in boosts])[0]
                    amt = [0.5, 1, 1.5, -1]
                    doc['amt'] += random.choice(amt)
                    dinc = getattr(benemy, doc['inc'])
                    setattr(benemy, doc['inc'], dinc - doc['amt'])
                    if pro_mode or debug_mode:
                        dact = doc['action']
                        damt = doc['amt']
                        prints(f'The Mutant decreased {dact}: {damt}')
                        print()
            elif benemy.race == 'Sprigon':
                if turn == 1:
                    sturn = 0
                if sturn == 1:
                    benemy.attack -= 4
                if benemy.sdefense <= 17:
                    sturn = 1
                    benemy.sdefense -= 7
                    benemy.attack += 7
                elif benemy.sdefense > 17:
                    sturn += 1
                    benemy.sdefense += 2.5
                    benemy.attack -= 1
            elif benemy.race == 'Fairy':
                pass
            elif benemy.race == 'Slime':
                pass
            elif benemy.race == 'Troll':
                pass
            elif benemy.race == 'Golem':
                benemy.defense += random.randint(1,3)
                if pro_mode is True:
                    prints('The Golem grew in defense.')
                    print()
            else:
                prints(f'No known enemy race {benemy.race}')
        if benemy.rank == 'Boss':
            boss_heal = (0.5 + (0.25 * benemy.level))
            benemy.hp += boss_heal
            if pro_mode is True:
                prints(f'Boss healed for {boss_heal} hearts.')
                print()
        character['Stats']['HP'] += .5
        pass   
    if character['Stats']['HP'] <= 0:
        prints("You were defeated. Deleting Character. do better")
        print()
        kill_character(uid, character['Name'])
        universe_menu(uid)
    if benemy.hp <= 0:
        prints(f"You defeated the {benemy.name}!")
        print()
        xpl = (1 + (0.05 * benemy.level))
        if analyzed:
            xp_gain = round((benemy.xp * xpl) * xpa, 4)
            show_xp = round((benemy.xp * xpl), 4)
            prints(f'Base XP Gained: {benemy.xp}')
            prints(f'Level Bonus: {benemy.xp} × {xpl}')
            prints(f'Analize Bonus: {show_xp} × {xpa}')
        else:
             xp_gain = round(benemy.xp * (1 + xpl), 3)
        character['Stats']['XP']+= xp_gain
        newxp = round(character['Stats']['XP'], 4)
        character['Stats']['XP'] = newxp
        character['Stats']['Gold'] += benemy.gold
        prints(f'XP Gained: {xp_gain}')
        prints(f"Character XP: {character['Stats']['XP']}")
        print()
        prints(f'Gold Gained: {benemy.gold}')
        prints(f"Character Gold: {character['Stats']['Gold']}")
        print()
        req_xp = ((100 * character['Stats']['Level']) - 100)
        if character['Stats']['XP'] >= (100 + req_xp):
            character['Stats']['Level'] += 1
            prints(f"Congratulations! You've leveled up to level {character['Stats']['Level']}!")
            print()
            character['Stats']['XP'] -= (req_xp + 100)
            if character['Stats']['XP'] < 0:
               character['Stats']['XP'] = 0
            point = 1   
            while point > 0:   
                prints('Select an Attribute to Upgrade.')   
                print()
                prints(f"1. Strength: {character['Attributes']['Strength']}")
                prints(f"2. Dexterity: {character['Attributes']['Dexterity']}")
                prints(f"3. Constitution: {character['Attributes']['Constitution']}")
                prints(f"4. Intelligence: {character['Attributes']['Intelligence']}")
                prints(f"5. Wisdom: {character['Attributes']['Wisdom']}")
                prints(f"6. Charisma: {character['Attributes']['Charisma']}")
                print()
                inc = inputs('Select an Attribute: ')

                if inc == '1':
                    character['Attributes']['Strength'] += 1
                    point -= 1
                    prints('Strength Increased.')
                    pass
                elif inc == '2':
                    character['Attributes']['Dexterity'] += 1
                    point -= 1    
                    prints('Dexterity Increased.')
                    pass
                elif inc == '3':
                    character['Attributes']['Constitution'] += 1
                    point -= 1    
                    prints('Constitution Increased.')
                    pass
                elif inc == '4':
                    character['Attributes']['Intelligence'] += 1
                    point -= 1    
                    prints('Intelligence Increased.')
                    pass
                elif inc == '5':
                    character['Attributes']['Wisdom'] += 1
                    point -= 1    
                    prints('Wisdom Increased.')
                    pass
                elif inc == '6':
                    character['Attributes']['Charisma'] += 1
                    point -= 1    
                    prints('Charisma Increased.')
                    pass
                else:
                    prints('Invalid. Please Choose Again.')    
                print()
                inchp = int((character['Secret Attributes']['Luck'] / 3) + ((character['Attributes']['Constitution'] - 8) / 2) + (character['Stats']['Max HP'] / 7))
                prints(f'Health Increased by {inchp} points')
                
                character['Stats']['Max HP'] += (inchp - 2)
                character['Stats']['HP'] = character['Stats']['Max HP']
                
        name = character['Name']    
        save_character(uid, name, character)    
        return 1        