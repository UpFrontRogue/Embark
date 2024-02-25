class Attack:
    def __init__(self, name = '', type = '', req = 8, att = 3, crit = 5, critm = 1.25, spd = 20):
        self.name = name
        self.type = type
        self.req = req
        self.attack = att
        self.crit = crit
        self.cm = critm
        self.speed = spd

character = {
    "Name": "Level 0",
        
    "Attributes": {
        "Strength": 7,
        "Dexterity": 7,
        "Constitution": 7,
        "Intelligence": 7,
        "Wisdom": 7,
        "Charisma": 7
    },
    
    "Secret Attributes": {
        "Luck": 5,
        "Speed": 20
    },
    
    "Stats": {
        "HP": 15,
        "Max HP": 15,
        "Level": 0,
        "Gold": 0,
        "XP": 0
    },
    
    "Inventory": {
        "Items": [],
        #additional slots if applicable (backpack, coin purse, etc)
        "Food": [],
        "Equipment": [],
        "Runes": [],
        "Misc": []
    },
    
    "Battle Stats": {
        "Attack": 2,
        "Defense": 5,
        "SDefense": 5,
        "Dodge": 5,
        "Crit": 5,
    },
    
    "Attacks": {
        Attack('Punch', 'Physical', 8, 3, 5, 1.5, 20),
        Attack('Slap', 'Physical', 1, 0, 2, 2, 12),
        Attack('Magic Bolt', 'Magical', 10, 4, 1, 3.25, 18),
    },
    
    "Extra Details": {
        "UID": None,
        "Handed": "Right",
        "Eyes": "Brown",
        "Hair": "Blonde",
        "Skin": "Pale",
        "Class": None,
        "Race": "Human",
        "Gender": "Non-Binary",
        "Features": ""
    },
    
    "Beastiary": {
        #name, number encountered as enc, slain amount as slain, damage taken, damage delt
    },
    
    "Equipment": {
        "Head": None,
        "Neck": None,
        "Chest": None,
        "Arms": None,
        "Main Hand": None,
        "Off Hand": None,
        "Ring": None,
        "Legs": None,
        "Feet": None
    },
}