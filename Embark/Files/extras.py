import time
import random
from found import *

version = '0.12.1.1'
debug_mode = True
pro_mode = False
giggles = False
universe_data = {}
next_choice = 0
edelay = False
nerd_stats = False

custom_delays = {
    '¡': {'delay': 0.25 if edelay else 0, 'print': False},
    '.': {'delay': 0.125, 'print': True},
    '!': {'delay': 0.135, 'print': True},
    ',': {'delay': 0.075, 'print': True},
    ':': {'delay': 0.075, 'print': True},
    ' ': {'delay': 0.0125, 'print': True}
}

def prints(*args, tod=False):
    default_delay = 0.005
    t = time.localtime(time.time())
    for arg in args:
        text = str(arg)
        for char in text:
            delay_info = custom_delays.get(char, {'delay': default_delay, 'print': True})
            delay = delay_info['delay']
            
            if delay_info['print']:
                time.sleep(delay)
                print(char, end='', flush=True)
            else:
                time.sleep(delay)
        print()
    
def printn(*args, npc):
    npc_delays = {
    '¡': {'delay': 0.25 if edelay else 0, 'print': False},
    '.': {'delay': 0.25, 'print': True},
    '!': {'delay': 0.6, 'print': True},
    ',': {'delay': 0.125, 'print': True},
    ':': {'delay': 0.1, 'print': True},
    ' ': {'delay': 0.0125, 'print': True}
}
    default_delay = 0.007
    t = time.localtime(time.time())
    for arg in args:
        text = f"{npc.name}: {str(arg)}"
        for char in text:
            delay_info = npc_delays.get(char, {'delay': default_delay, 'print': True})
            delay = delay_info['delay']
            
            if delay_info['print']:
                time.sleep(delay)
                print(char, end='', flush=True)
            else:
                time.sleep(delay)
        print()

def inputs(quote='',tab= True, uid= None, character= None):
    global next_choice
    passes = input(f'{quote}')
    if debug_mode:
        if passes == '{00000}':
            prints('Main Menu.')
            print()
            from menus import main_menu
            main_menu()
            return
        elif passes == '{00001}':
            prints('Options Menu.')
            print()
            from menus import options_menu
            options_menu()
            return
        elif passes == '{00002}':
            prints('Cheats.')
            print()
            from cheats import cheats
            cheats()
            return
        elif passes == '{00008}':
            roll_dice('Useless Roll:')
            print()
        elif passes == '{00100}':
            prints('Force Return.')
            print()
            return        
        elif passes == '{00101}':
            prints('Force Integer.')
            print()
            nc = int(input('Next Roll (0 to Cancel): '))
            if nc != 0:
                next_choice = nc
                nc = 0
                if next_choice != 0:
                    prints(f'Next Choice: {next_choice}')
                    print()
        elif passes == '{00102}':
            prints('Force Item.')
            print()
            iuid = int(input('Input Item UID (0 to Cancel): '))
            if iuid != 0:
                sitem = next((item for item in items if item.uid == iuid), None)
                character["Inventory"].append(sitem)
        elif passes == '{00103}':
            if character is None:
                prints('Please load a character first.')
                print()
                pass
            prints('Force Ingredient.')
            print()
            iuid = int(input('Input Ingr UID (0 to Cancel): '))
            if iuid != 0 and character is not None:
                singr = next((Item for item in items if item.uid == iuid), None)
                character["Inventory"].append(singr)
        elif passes == '{00169}' and character is not None:
            prints ('Force Heal')
            print()
            heal = max(int(input('Heal Amount: ')), 0)
            character['Stats']['HP'] += heal
        else:
            if tab:
                print()
            return passes
    else:
        if tab:
            print()
        return passes
        
def roll_dice(quote='', silent=False):
    max_number = 20
    outcome = random.randint(1, max_number)
    if not silent:
        prints(f'{quote}{outcome}')
        if outcome == 1 and giggles is True:
            prints('You Critically Failed..')
        elif outcome == max_number and giggles is True:
            prints("You rolled a Natural 20!")
    return outcome

class Attack:
    def __init__(self, name='', type='', req=8, att=3, crit=5, critm=1.25, spd=20):
        self.name = name
        self.type = type
        self.req = req
        self.attack = att
        self.crit = crit
        self.cm = critm
        self.speed = spd
