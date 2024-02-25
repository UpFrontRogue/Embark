import random

iequip = {
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

class Npc:
    def __init__ (self, name, uid, race, base_level, level):
        self.name = name
        self.uid = uid
        self.race = race
        self.base_level = base_level
        self.level = level
        self.iequip = iequip

class Enemy:
    def __init__(self, name = '', race = None, base_level = 1, level = 1, hp = 1, max_hp = 1, attack = 5, defense = 5, sdefense = 5, crit = 5, speed = 20, dodge = 20, xp = 0, gold = 7, rank= None, disc = ''):
        self.name = name
        self.race = race
        self.base_level = base_level
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.sdefense = sdefense
        self.crit = crit
        self.speed = speed
        self.dodge = dodge
        self.xp = xp
        self.gold = gold
        self.rank = rank

class Item:
    def __init__(self, uid, name, level, itype, forage, gold, effect, attribute = {}, amount = None, consume=False, equip=False, equipped=False, quantity=1, disc = ''):
        self.uid = uid
        self.name = name
        self.level = level
        self.itype = itype
        self.forage = forage
        self.gold = gold
        self.effect = effect
        self.attribute = attribute
        self.amount = amount
        self.consume = consume
        self.equip = equip
        self.equipped = equipped
        self.quantity = quantity
        self.disc = disc

class Equipment:
    def __init__(self, uid, name, level, itype, gold, effect, attributes = {}, amounts = {}, equip = True, equipped = False, quantity = 1, disc = ''):
        self.uid = uid
        self.name = name
        self.level = level
        self.itype = itype
        self.gold = gold
        self.effect = effect
        self.attributes = attributes
        self.amount = amounts
        self.equip = equip
        self.equipped = equipped
        self.quantity = quantity
        self.disc = disc

class Weapon:
    def __init__(self, uid, name, level, itype, gold, effect, attributes = {}, amounts = {}, equip = True, equipped = False, quantity = 1, disc = ''):
        self.uid = uid
        self.name = name
        self.level = level
        self.itype = itype
        self.gold = gold
        self.effect = effect
        self.attributes = attributes
        self.amount = amounts
        self.equip = equip
        self.equipped = equipped
        self.quantity = quantity
        self.disc = disc

class Ingr:
    def __init__(self, uid, name, level, forage, gold, effect, time, attribute, amount, consume=False, quantity=1, disc = ''):
        self.uid = uid
        self.name = name
        self.level = level
        self.forage = forage
        self.gold = gold
        self.effect = effect
        self.time = time
        self.attribute = attribute
        self.amount = amount
        self.consume = consume
        self.quantity = quantity
        self.disc = disc
        
            #uid, name, level, itype, forage, gold, effect, attribute, amount, consume, equip, equipped, quantity, disc
items = [
    Item(10000, 'Apple', 1, None, True, 4, 'Heal', None, 3, True, False, False, random.randint(1,3), 'A good looking apple. Good for eating.'),
    Item(10001, 'Banana', 1, None, True, 5, 'Heal', None, random.randint(2,5), True, False, False, random.randint(1,3), 'The Classic Yellow Banana.'),
    Item(10002, 'Carrot', 2, None, True, 7, 'Heal', None, 5, True, False, False, random.randint(1,3), 'A sturdy rodded carrot. good for a delicious stew or a quick snack.'),
    Item(10003, 'Potato', 3, None, True, 9, 'Heal', None, 7, True, False, False, random.randint(1,3), 'The Glorious Potato. Need more be said?'),
    Item(10004, 'Raw Meat', 4, None, False, 15, 'Heal', None, 8, True, False, False, random.randint(1,3), 'Beef? Venison? either way it is edible so do not complain...'),
    Item(10005, 'Fire Scroll', 4, None, True, 20, 'Damage', None, 14, True, False, False, 1, 'A useful scroll for quick damage. (does not do fire damage)'),
    Item(10006, 'Health Vial (2oz)', 5, None, True, 35, 'Heal', None, 25, True, False, False, 1, 'Recovers a small amount of health, for potions..'),
    Item(10007, 'Plantain', 6, None, True, 12, 'Heal', None, random.randint(5,13), True, False, False, random.randint(1,2), 'A bigger, more bitter tropical banana.'),
    Item(10008, 'Cooked Meat', 5, None, False, 25, 'Heal', None, 15, True, False, False, 1, "Whatever it was before... it's cooked now."),
    Item(10009, 'Seared Meat', 7, None, False, 32, 'Heal', None, 28, True, False, False, 1, 'A nicely seared slab of meat.'),
    Item(10010, 'Grilled Meat', 9, None, False, 35, 'Heal', None, 40, True, False, False, 1, 'A grilled slice of meat.'),
    Item(10011, 'Mystery Fruit', 10, None, True, 32, 'Heal', None, random.randint(1,35), True, False, False, random.randint(1,4), 'A red spiky, bitter-sweet fruit with a white inside.'),
    Item(10012, 'Health Vial (8oz)', 10, None, True, 120, 'Heal', None, 100, True, False, False, 1, 'Recovers 100 HP.'),
]

cores = [
    Item(90001, 'Strength Core', 15, None, False, 1080, 'Attribute', 'Strength', 1, True, False, False, 1, 'A Epic Strength Core. Increases Strength by 1.'),
    Item(90002, 'Dexterity Core', 10, None, False, 1080, 'Attribute', 'Dexterity', 1, True, False, False, 1, 'A Epic Dexterity Core. Increases Dexterity by 1.'),
    Item(90003, 'Constitution Core', 11, None, False, 1080, 'Attribute', 'Constitution', 1, True, False, False, 1, 'A Epic Constitution Core. Increases Constitution by 1.'),
    Item(90004, 'Intelligence Core', 12, None, False, 1080, 'Attribute', 'Intelligence', 1, True, False, False, 1, ''),
    Item(90005, 'Wisdom Core', 14, None, False, 1080, 'Attribute', 'Wisdom', 1, True, False, False, 1, ''),
    Item(90006, 'Charisma Core', 13, None, False, 1080, 'Attribute', 'Charisma', 1, True, False, False, 1, ''),
]

           #uid, name, level, forage, gold, effect, time, attribute, amount, consume, quantity, disc       
cingr = [
    Ingr(11000, 'Stick', 1, True, 2, None, None, None, None, False, 1, 'The common twig'),
    Ingr(11001, 'Pebble', 1, True, 2, None, None, None, None, False, 1, 'A pebble off the ground.'),
    Ingr(11002, 'Tartberry', 1, True, 2, 'Heal', 3, 'HP', 1.5, True, 1, 'A tart yet tasty berry.'),
    Ingr(11003, 'Straw', 1, True, 1, None, None, None, None, False, random.randint(2,7), 'Good for starting a fire '),
    Ingr(11004, 'Paper', 1, False, 2, None, None, None, None, False, 1, 'A thin slice of a tree used for writing.'),
    Ingr(11005, 'Wood', 2, True, 3, None, None, None, None, False, random.randint(1,4), 'Good for keeping a fire'),
    Ingr(11006, 'Rock Chunk', 2, True, 3, 'Heal', 2, None, -2.5, True, 1, 'The perfect sized stone for a tool.'),
    Ingr(11007, 'Hay', 2, True, 2, None, None, None, None, False, random.randint(2,5), 'Used for making Flour.'),
    Ingr(11008, 'Flour', 3, False, 3, 'Heal', 1, None, 0.5, True, 3, 'A common cooking ingredient. Not for the gluten free people.'),
    Ingr(11009, 'Chicken Egg', 3, True, 4, 'Heal', 2, None, 0.75, True, 1, 'The egg of a chicken.' ),
    Ingr(11010, 'Wood Plank', 4, False, 10, None, None, None, None, False, 1, 'A fine plank of wood.'),
    Ingr(11011, 'Leather Strap', 4, False, 3, None, None, None,  None, False, 1, 'A small scrap of leather.'),
    Ingr(11012, 'Leather Hide', 4, True, 14, None, None, None, None, False, 1, 'A fresh leather pelt. Do not eat.'),
    Ingr(11013, 'Leather Padding', 5, False, 68, None, None, None, None, False, 1, 'Brased leather padding. Good for making Armor.' ),
    Ingr(11014, 'Iron Ore', 7, False, 18, None, None, None, None, False, 1, 'A good chunk of iron with a little slag.'),
    Ingr(11015, 'Iron Bar', 7, False, 38, None, None, None, None, False, 1, 'The Standardized bar of Iron.'),
    Ingr(11016, 'Copper Ore', 5, False, 12, None, None, None, None, False, 1, 'A raw chunk of copper ore.'),
    Ingr(11017, 'Copper Bar', 5, False, 25, None, None, None, None, False, 1, 'A pure bar of copper. Useful for equipment.')
]

equipment = [
    Item(20000, 'Training Dagger', 1, 'Main Hand', False, 1, 'Equip Weapon', {'Attack', 'Speed'}, {2,8}, False, True, False, 1, 'A simple dagger for training.'),
    Item(21000, 'Leather Helmet', 4,'Head', False, 23, 'Equip Attr', 'Defense', 2, False, True, False, 1, 'A basic leather Helmet.'),
    Item(21001, 'Leather Chest', 4,'Chest', False, 45, 'Equip Attr', 'Defense', 2.5, False, True, False, 1, 'The Sturdy Leather Chestplate.'),
    Item(21002, 'Leather Bracers', 4, 'Arms', False, 15, 'Equip Attr', 'Defense', 1, False, True, False, 1, 'Leather paddings for your arms.'),
    Item(21003, 'Leather Legpads', 4,'Legs', False, 35, 'Equip Attr', 'Defense', 1.5, False, True, False, 1, 'You need a description for leather pads for your legs?'),
    Item(21004, 'Leather Boots', 4,'Feet', False, 20, 'Equip Attr', 'Defense', 1.5, False, True, False, 1, 'Leather. Boots. simple.'),
    Item(21005, 'Copper Brased Chestplate', 6, 'Chest', False, 75, 'Equip Attr', 'Defense', 4, False, True, False, 1, 'A copper plated chestplate.'),
    Item(21006, 'Copper Brasers', 6, 'Arms', False, 63, 'Equip Attr', 'Defense', 2, False, True, False, 1, 'Copper Brasers with leather for comfort.'),
    Item(21007, 'Copper Legpads', 6, 'Legs', False, 69, 'Equip Attr', 'Defense', 2.5, False, True, False, 1, 'Jak style copper legpads.'),
    Item(21008, 'Copper Boots', 6, 'Feet', False, 65, 'Equip Attr', 'Defense', 1.5, False, True, False, 1, 'Boots of copper...'),
    Item(21009, 'Amulet of Protection', 7, 'Neck', False, 75, 'Equip Attr', 'Defense', 5, False, True, False, 1, 'An amulet meant to protect you from damage.'),
    Item(21010, 'Amulet of Speed', 9, 'Neck', False, 85, 'Equip Attr', 'Speed', 4, False, True, False, 1, 'An amulet embewing you with Swiftness.'),
]

enemies = [
    Enemy('Slime', 'Slime', 1, random.randint(1, 8), 17, 17, 6, 4, 3, 5, 14, 2, 3, random.randint(1, 7), None, 'A small green angry blob ready for battle.'),
    Enemy('Fairy Hybrid', 'Fairy', 1, random.randint(1, 10), 14, 14, 5, 3, 11, 7, 14, 4, 4, random.randint(1, 11), None, 'A fairy mixed with a human.'),
    Enemy('Wild Hog', None, 1, random.randint(1, 12), 13, 13, 7, 8, 0, 9, 15, 7, 5, random.randint(3, 12), None, 'A thick skinned pig with tusks.'),
    Enemy('Wolf', 'Wolf', 1, random.randint(2, 13), 25, 25, 8, 6, 3, 7, 17, 9, 7, random.randint(5, 17), None, 'A grey wild canine with intent to kill.'),
    Enemy('Woodland Morg', 'Morg', 1, random.randint(2, 13), 19, 19, 7, 8, 10, 9, 15, 10, 12, 8, None, 'A humanoid creature that protects their land, slightly smaller than a dwarf.'),
    Enemy('Mutated Human', None, 1, random.randint(3, 14), 22, 22, 6, 6, 2, 10, 20, 12, 9, 0, None, 'A human turned Mutant.'),
    Enemy('Preformed Morg', 'Morg', 2, random.randint(3, 16), 21, 21, 8, 7, 11, 12, 18, 14, 13, 10, None, 'A Morg before they evolve.'),
    Enemy('Bandit', 'Human', 2, random.randint(3, 17), 23, 23, 11, 5, 2, 22, 21, 16, 12, random.randint(17, 32)),
    Enemy('Crab Mutant', 'Mutant', 2, random.randint(3, 20), 22, 22, 8, 13, 4, 11, 16, 11, 14, random.randint(13, 42)),
    Enemy('Moddling', None, 2, random.randint(4, 26), 19, 19, 8.5, 9, 7, 23, 24, 25, 13, random.randint(7, 22)),
    Enemy('Greffel', None, 3, random.randint(4, 28), 24, 24, 8, 9, 14, 9, 18, 18, 15, random.randint(6, 32)),
    Enemy('Hog Mutant', 'Mutant', 3, random.randint(5, 29), 36, 36, 13, 13, 4, 18, 22, 18, 14, random.randint(11, 41)),
    Enemy('Feline Mutant', 'Mutant', 3, random.randint(5, 42), 32, 32, 17, 10, 11, 34, 24, 24, 27, random.randint(7, 21)),
    Enemy('Slimora', 'Slime', 4, random.randint(6, 22), 28, 28, 13, 9, 17, 19, 21, 27, 14, random.randint(4, 19)),
    Enemy('Teragon', 'Sprigon', 4, random.randint(5, 38), 32, 32, 13, 13, 19, 17, 18, 22, 28, random.randint(7, 23)),
    Enemy('Elder Wolf', 'Wolf', 5, random.randint(5, 30), 35, 35, 9, 8, 11, 10, 16, 18, 22, random.randint(8, 22)),
    Enemy('Viper Mutant', 'Mutant', 6, random.randint(7, 37), 23, 23, 13, 9, 13, 23, 21, 8, 31, random.randint(13, 64)),
    Enemy('Vitagon', 'Sprigon', 6, random.randint(8, 42), 42, 42, 15, 12, 21, 15, 21, 18, 39, random.randint(7, 41)),
    Enemy('Shifter', 'Mutant', 7, random.randint(9, 82), 83, 103, 10, 11, 18, 8, 28, 18, 18, random.randint(3,7)),
    Enemy('Armoured Bandit', 'Human', 7, random.randint(7, 49), 75, 75, 14, 9, 5, 18, 32, 15, 32, random.randint(17, 78)),
    Enemy('Blade Dancer', 'Human', 7, random.randint(7, 63), 43, 52, 22, 8, 7, 18, 32, 16, 21, 100),
    Enemy('Royal Offender', 'Human', 10, random.randint(15, 52), 35, 40, 17, 15, 5, 15, 22, 16, 32, random.randint(18, 72))
]
#              Name, Type, BaseL, Level, BaseHP, MaxHP, Att, Def, SDef, Crit, Speed, Dodge, XP, Gold, Rank, Disc
elites = [
    Enemy('Troll', 'Troll', 1, random.randint(7, 21), 45, 45, 12, 15, 0, 12, 21, 7, 40, 24, 'Elite'),
    Enemy('Golem', 'Golem', 3, random.randint(9, 27), 65, 65, 14, 17, 0, 0, 11, 7, 24, 32, 'Elite'),
    Enemy('Serpant Mutant', 'Mutant', 9, random.randint(11, 49), 59, 59, 16, 7, 5, 16, 20, 18, 27, 52, 'Elite')
]

bosses = [
    Enemy('Slime Lord', 'Slime', 7, 15, 100, 100, 10, 10, 6, 22, 22, 17, 650, random.randint(95, 216), 'Boss'),
    Enemy('King of Mutants', 'Mutant', 15, 25, 150, 175, 12, 9, 10, 20, 27, 20, 2000, 650, 'Boss'),
]

jbosses = [
    Enemy('Bazooka Fish', 'Fish', 1, 16, 150, 200, 17, 23, 11, 5, 14, 6, 150, 85, 'Boss'),
    Enemy('G.R.Duck', 'Rubber Duck', 25, 50, 450, 450, 23, 22, 1, 17, 21, 16, 350, 475, 'Boss')
]

final_boss = [
    Enemy('Death-Magedon', 'Sprigon', 100, 69420, 999999999999999, 9999999999999999, 999999999999999, 999999999999999, 999999999999999, 100, 100, 69, 999999999999999, 1, 'Boss')
]

names = [
    'Adam',
    'Alphonzo',
    'Aimes',
    'Brittany',
    'Brandon',
    'Cameron',
    'Carson',
    'Celo',
    'Charles',
    'Damien',
    'Diamity',
    'Edward',
    'Flemble',
    'Freddie',
    'Gregory',
    'Goku',
    'Hephe',
    'Hermione',
    'Indigo',
    'Itachi',
    'Jykle',
    'Josef',
    'Kammie',
    'Lindsey',
    'Micheal',
    'Nicholas',
    'Ophilia',
    'Peaches',
    'Quentin',
    'Rasta',
    'Samuel',
    'Sir Lance',
    'Teppe',
    'Terry',
    'Unã Anú',
    'Victor',
    'Windago',
    'Xyla',
    'Yasolda',
    'Zaberath',
    
    'Light Yagami', 
    'Ryūk',
    'Cole',
    'Joe',
    'Ron',
    'Bagel',
    'Jacob',
    'Charlie',
    'Mud',
    'Emily',
    'Ind icka',
    'Sat Eeva',
    'The Game...r',
    'Aurora',
    'Lucey',
    'Papi',
    'Gran Gran',
    'Uldavier',
    'Joey',
    'Gringdlr',
    'Kainalu',
    'Lauwie',
    
    'Renee',
    'Shaniqua',
    'Sam',
    'Stanford',
    'Joe',
    'Ron',
    'Joey',
    'Mufasa',
    'Jackie',
    'Marie-Anne',
    'Jacob',
    'Arnold',
    'Pussé',
    'Jimmy',
    'Jill',
    'Jeremiah',
    'Delilah',
    'Kris',
    'Margaret',
    'Potaté'
]

npcs = [
    Npc('Greg', None, 'Human', 1, 4),
    Npc('Taz', 'QY10458', 'Morg', 5, 8),
    Npc('Terry', 'AA00000', 'Goblin', 25, 50),
    Npc('Gibbity Arms Jr.', 'FD69370', 'Morg',  7, 7),
    Npc(random.choice(names), None, 'Human', 2, 4),
    Npc(random.choice(names), None, 'Human', 1, 2),
    Npc(random.choice(names), None, 'Human', 4, 7),
    Npc(random.choice(names), 'JT30542', 'Human', 7, 10)
]

class BeastEntry:
    def __init__(self, name, encountered = 0, slain = 0, damage_taken = 0, damage_dealt = 0):
        self.name = name
        self.encountered = encountered
        self.slain = slain
        self.damage_taken = damage_taken
        self.damage_dealt = damage_dealt

    def upd_enc(self, encountered = 1):
        self.encountered += encountered

    def upd_slain(self, slain = 1):
        self.slain += slain

    def upd_dmgt(self, damage):
        self.damage_taken += damage

    def upd_dmgd(self, damage):
        self.damage_dealt += damage
    
    def upd_all(self, dmgt, dmgd):
        self.encountered += 1
        self.slain += 1
        self.damage_taken += dmgt
        self.damage_dealt += dmgd
        
    def details(self):
        return {
            "Name: ": self.name,
            "Encountered: ": self.encountered,
            "Slain: ": self.slain,
            "Damage Taken: ": self.damage_taken,
            "Damage Dealt: ": self.damage_dealt
        }
    